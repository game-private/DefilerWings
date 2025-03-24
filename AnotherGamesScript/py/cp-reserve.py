# https://github.com/CloudPolis/webdav-client-python
# sudo -u webdav python3 /inRamS/mounts/records/_sh/startup/cp-reserve.py

from enum import Enum
import webdav3
import webdav3.client as wc
import getpass
import random
import time
import datetime
import os
import threading
from concurrent.futures import ThreadPoolExecutor

class PrintCommandState(Enum):
    ERROR = 0
    NONE  = 1
    DONE  = 2
    NEW   = 3
    SHORT = 4
    FULL  = 5


# Настройки скрипта
max_workers  = 16
doPrintFiles = PrintCommandState.NONE
# Должно быть положительное значение в часах (давность файлов, которые всё ещё проверяются)
lastHours    = 720

start_time         = datetime.datetime.now()
min_modified_time  = start_time
min_modified_time += datetime.timedelta(hours=-lastHours)

# Раскомментировать, если необходимо принудительно проверить все файлы на дату
# min_modified_time  = False
# Раскомментировать, если необходимо пропускать файлы, старше последней загрузки с сервера (должна быть верно установлена дата последней загрузки с сервера)
min_modified_time_min  = datetime.datetime.strptime('2025.03.22 15:00', '%Y.%m.%d %H:%M')

if min_modified_time_min > min_modified_time:
    min_modified_time = min_modified_time_min


progressInterval = 60

updloadedFiles = 0
skippedFiles   = 0
failedFiles    = 0
lock = threading.Lock()

lastProgressDate = datetime.datetime.now()


authLines = []
with open("/home/main/users/webdav/pwd", 'r') as file:
    authLines = file.read().splitlines()

options = {
    'webdav_hostname': "https://webdav.yandex.ru/",
    'webdav_login'   : authLines[0].strip(),
    'webdav_password': authLines[1].strip(),
    'verbose'        : True
}


# options['webdav_login']    = input("Введите имя пользователя: ")
# options['webdav_password'] = getpass.getpass(f"Введите пароль для пользователя {options['webdav_login']}:\n")


client = wc.Client(options)


def check(noPrint=False):
    global client
    try:
        # Проверка подключения
        if client.check():
            if not noPrint:
                print("Подключение успешно установлено!")
            return True
        else:
            if not noPrint:
                print("Не удалось установить подключение")
            return False
            
    except Exception as e:
        if not noPrint:
            print(f"Произошла ошибка: {str(e)}")
        return False


checkInLoop_printed = False
def printBadNetwork():
    global checkInLoop_printed

    try:
        lock.acquire()

        if not checkInLoop_printed:
            print("bad network " + datetime.datetime.now().strftime("%H:%M:%S"))
            checkInLoop_printed = True

    finally:
        lock.release()


def checkInLoop():
    global checkInLoop_printed

    while not check(True):
        printBadNetwork()
        time.sleep(60)

    # Окончание функции - связь восстановилась
    try:
        lock.acquire()

        if checkInLoop_printed:
            checkInLoop_printed = False
            print("network restored " + datetime.datetime.now().strftime("%H:%M:%S"))
    finally:
        lock.release()

checkInLoop()

# info
# {'created': '2025-03-19T05:40:04Z', 'name': '0000000001', 'size': '65536', 'modified': 'Wed, 19 Mar 2025 05:40:04 GMT', 'etag': '6c1249976b5f15b6b517e6a147ca0dbf', 'content_type': 'application/octet-stream'}

# datetime.datetime.strptime('Wed, 19 Mar 2025 05:40:04 GMT', '%a, %d %b %Y %H:%M:%S %Z')
# current_time = datetime.datetime.now()
# x = current_time.strftime("%a, %d %b %Y %H:%M:%S %z %Z")
# print(x)

FailTimeout = [300, 120]

# rFileName - имя удалённого файла
# lFileName - имя локального файла
def doUpdateFile(rFileName, lFileName, threadPool, doPrint, index, lenDir, isFailed=False):
    global threadsCount
    global updloadedFiles
    global skippedFiles
    global failedFiles
    global checkInLoop_printed
    global lock

    if doPrint.value >= PrintCommandState.FULL.value:
        print("Проверка файла " + rFileName)

    strNewFile = ""
    try:
        mtime     = os.path.getmtime(lFileName)
        lmodified = datetime.datetime.fromtimestamp(mtime)

        if min_modified_time:
            if min_modified_time > lmodified:
                if doPrint.value >= PrintCommandState.FULL.value:
                    print("Пропущен файл (слишком старый): " + rFileName)

                try:
                    lock.acquire()
                    skippedFiles += 1
                finally:
                    lock.release()

                printProgress(lock, index, lenDir)
                return
        

        info = client.info(rFileName)

        # Время передаётся по гринвичу
        rmodified = datetime.datetime.strptime(info['modified'], '%a, %d %b %Y %H:%M:%S %Z')
        # Приводим время от гринвича к Москве
        rmodified += datetime.timedelta(hours=3)

        # print(rmodified)
        # print(lmodified)
        
    except webdav3.exceptions.RemoteResourceNotFound:
        rmodified = 0
        lmodified = 1
        strNewFile = " (новый файл)"
        if doPrint.value >= PrintCommandState.NEW.value:
            print(f"Новый файл: " + rFileName)

    except webdav3.exceptions.NoConnection:
        printBadNetwork()
        time.sleep(random.randint(0, 60))
        checkInLoop()
        threadPool.submit(doUpdateFile, rFileName, lFileName, threadPool, doPrint)
        return
    
    except webdav3.exceptions.ConnectionException:
        printBadNetwork()
        time.sleep(random.randint(0, 60))
        checkInLoop()
        threadPool.submit(doUpdateFile, rFileName, lFileName, threadPool, doPrint)
        return
    
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        print(type(e))
        
        if isFailed:
            try:
                lock.acquire()
                failedFiles += 1
            finally:
                lock.release()
        else:
            time.sleep(FailTimeout[0] + random.randint(0, FailTimeout[1]))
            checkInLoop()
            threadPool.submit(doUpdateFile, rFileName, lFileName, threadPool, doPrint, True)

        return


    if rmodified < lmodified:
        if doPrint.value >= PrintCommandState.SHORT.value:
            print("Обновление файла " + rFileName + f" [remote {rmodified}, local {lmodified}]")

        try:
            client.upload_sync(remote_path=rFileName, local_path=lFileName)
            if doPrint.value >= PrintCommandState.DONE.value:
                print("Обновление файла " + rFileName + " закончилось успешно." + strNewFile)
            
            try:
                lock.acquire()
                updloadedFiles += 1
            finally:
                lock.release()

        except webdav3.exceptions.NoConnection:
            if doPrint.value >= PrintCommandState.SHORT.value:
                print("Разрыв соединения с сетью при обновлении файла " + rFileName)
            printBadNetwork()
            checkInLoop()
            threadPool.submit(doUpdateFile, rFileName, lFileName, threadPool, doPrint)
            return
        except webdav3.exceptions.ConnectionException:
            if doPrint.value >= PrintCommandState.SHORT.value:
                print("Разрыв соединения с сетью при обновлении файла " + rFileName)
            printBadNetwork()
            checkInLoop()
            threadPool.submit(doUpdateFile, rFileName, lFileName, threadPool, doPrint)
            return
        except Exception as e:
            print("------------------------------------------------")
            print("Обновление файла " + rFileName + " ПРОВАЛИЛОСЬ!")
            print(f"Произошла ошибка: {str(e)}")
            print(type(e))
            print("------------------------------------------------")

            if isFailed:
                try:
                    lock.acquire()
                    failedFiles += 1
                finally:
                    lock.release()
            else:
                time.sleep(FailTimeout[0] + random.randint(0, FailTimeout[1]))
                checkInLoop()
                threadPool.submit(doUpdateFile, rFileName, lFileName, threadPool, doPrint, True)

            return

    printProgress(lock, index, lenDir)


def printProgress(lock, i, lenDir):
    global lastProgressDate
    global progressInterval
    global updloadedFiles
    global skippedFiles

    try:
        lock.acquire()
        progress = (i+1)*100/lenDir
        curTime = datetime.datetime.now()
        if (curTime - lastProgressDate).total_seconds() > progressInterval:
            if progress >= 0:
                print(f"{progress:3.0f}%\tup {updloadedFiles}, sk {skippedFiles}\t{curTime.strftime("%H:%M:%S")}")
            else:
                print("0%")

            lastProgressDate = datetime.datetime.now()
    finally:
        lock.release()


def push(remote, local, name, doPrintFiles=PrintCommandState.NONE, max_workers=16):
    # current_time = datetime.datetime.now()
    # print(current_time.strftime("%Y.%m.%d %H:%M:%S"))
    global updloadedFiles, skippedFiles

    oldUpdloadedFiles = updloadedFiles
    oldSkippedFiles   = skippedFiles
    
    threadPool = ThreadPoolExecutor(max_workers)

    checkInLoop()
    
    # print("Синхронизация " + name)
    # result = client.push(remote_directory=remote, local_directory=local)
    # result=True
    # if not result:
    #    print("Синхронизация " + name + " ПРОВАЛЕНА! ")
    print()
    print("Обновление " + name)
    
    current_time = datetime.datetime.now()
    print(current_time.strftime("%Y.%m.%d %H:%M:%S"))

    # dir = client.list(remote)
    dir  = os.listdir(local)
    for i, file in enumerate(dir):

        rFileName = os.path.join(remote, file)
        lFileName = os.path.join(local, file)

        if os.path.isdir(lFileName):
            print(f"ОШИБКА: в директории найдена папка '{lFileName}'. Папки не сихронизируются, только отдельные файлы!")
            break
    
        #if i % 16 == 0:
        #    checkInLoop()
        
        # doUpdateFile(rFileName, lFileName, doPrintFiles)
        threadPool.submit(doUpdateFile, rFileName, lFileName, threadPool, doPrintFiles, i, len(dir))

        

    threadPool.shutdown(True)
    print()
    print("Закончено " + name + f" [{updloadedFiles - oldUpdloadedFiles}, {skippedFiles - oldSkippedFiles}]")
    current_time = datetime.datetime.now()
    print(current_time.strftime("%Y.%m.%d %H:%M:%S"))
    
    #if result:
    #    print("Синхронизация " + name + " успешно завершена")
    #else:
    #    print("Синхронизация " + name + " провалена")

    
push('/Arcs/keys/',    '/Arcs/Disks/Reserve/keys',    "keys",    doPrintFiles, max_workers)
push('/Arcs/records/', '/Arcs/Disks/Reserve/records', "records", doPrintFiles, max_workers)
push('/Arcs/books3/',  '/Arcs/Disks/Reserve/books3',  "books3",  doPrintFiles, max_workers)

#thread1 = threading.Thread(target=push, args=('/Arcs/keys',    '/Arcs/Disks/Reserve/keys',    "keys"))
#thread2 = threading.Thread(target=push, args=('/Arcs/records', '/Arcs/Disks/Reserve/records', "records"))
#thread3 = threading.Thread(target=push, args=('/Arcs/books3',  '/Arcs/Disks/Reserve/books3',  "books3"))
#thread1.start()
#thread2.start()
#thread3.start()


#thread1.join()
#thread2.join()
#thread3.join()

current_time = datetime.datetime.now()
print(current_time.strftime("%Y.%m.%d %H:%M:%S"))
if failedFiles > 0:
    print()
    print("----------------------------------------------------------------------------------------")
    print(f"!!! При работе программы были обнаружены неустранимые ошибки в количестве {failedFiles} !!!")
    print("          Попробуйте запустить синхронизацию повторно")
    print("----------------------------------------------------------------------------------------")
    print()

if min_modified_time:
    
    print(f"Программа завершена. Загружено {updloadedFiles} файлов. Пропущено (слишком старые) {skippedFiles} файлов. Комментарий: старые файлы не будут пропускаться, если min_modified_time  = False. Сейчас пропускаются файлы старше {lastHours} часов (либо старше абсолютной даты {min_modified_time_min.strftime("%Y.%m.%d")}).")

    totalDays = (start_time - min_modified_time).total_seconds()/3600/24
    print(f"Обновлялись только файлы новее, чем {min_modified_time.strftime("%Y.%m.%d %H:%M:%S")}  ({totalDays:.0f} дней)")

else:
    print(f"Программа завершена. Загружено {updloadedFiles} файлов. Все файлы проверены по дате.")

print("sudo -u webdav python3 /inRamS/mounts/records/_sh/startup/cp-reserve.py")
