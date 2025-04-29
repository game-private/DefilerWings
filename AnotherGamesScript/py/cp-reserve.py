# https://github.com/CloudPolis/webdav-client-python
# https://github.com/ezhov-evgeny/webdav-client-python-3
# https://pypi.org/project/webdavclient3/
# sudo -u webdav python3 /inRamS/mounts/records/_sh/startup/cp-reserve.py

print("sudo -u webdav python3 /inRamS/mounts/records/_sh/startup/cp-reserve.py")

from enum import Enum
import webdav3
import webdav3.client as wc
import getpass
import copy
import random
import time
import datetime
import os
import threading
from concurrent.futures import ThreadPoolExecutor

class PrintCommandState(Enum):
    ERROR  = 0
    NONE   = 1
    NEW    = 2
    DONE   = 3
    SHORT  = 4
    FULL   = 5

class Statistic():
    def __init__(self):
        self.allFiles         = 0
        self.updloadedFiles   = 0
        self.skippedFiles     = 0
        self.failedFiles      = 0
        self.CheckedOldFiles  = 0
    
class State():
    def __init__(self):
        # Настройки скрипта
        # max_workers = 16 лучше, но если сеть не хочется перегружать, то лучше 4. 1 - если сервером выдаётся "Request per second limit exceeded for user"
        self.max_workers    = 1
        self.sleepForTask   = 60
        self.doPrintFiles   = PrintCommandState.NONE
        self.doPrintSubdirs = False
        self.oldstat        = []
        # Если True, то обновление файла будет всегда только одно (стоит в блокировке)
        self.doSingleUpdate = True
        self.singleUpdLock  = threading.Lock()
        # Должно быть положительное значение в часах (давность файлов, которые всё ещё проверяются)
        self.lastHours      = 720
        self.DateFileName   = "/Arcs/Disks/Reserve/date.cp-reserve.log"
        self.DateFileFormat ='%Y.%m.%d %H:%M'

        self.threadPool     = ThreadPoolExecutor(self.max_workers)
        self.start_time     = datetime.datetime.now()
        #self.min_modified_time  = self.start_time
        #self.min_modified_time += datetime.timedelta(hours=-self.lastHours)

        # Раскомментировать, если необходимо принудительно проверить все файлы на дату
        # min_modified_time  = False
        # Раскомментировать, если необходимо пропускать файлы, старше последней загрузки с сервера (должна быть верно установлена дата последней загрузки с сервера)
        # self.min_modified_time_min  = datetime.datetime.strptime('2025.03.24 09:00', '%Y.%m.%d %H:%M')
        if not os.path.isfile(self.DateFileName):
            self.min_modified_time = False
        else:
            try:
                with open(self.DateFileName, 'r') as file:
                    dateLine = file.read().strip()
                
                self.min_modified_time = datetime.datetime.strptime(dateLine, self.DateFileFormat)

            except Exception as e:
                self.min_modified_time = False
                print(f"Произошла ошибка при попытке инициализации программы: {str(e)} [файл {self.DateFileName} некорректен или недоступен для чтения]")
        

        #if self.min_modified_time_min and self.min_modified_time_min > self.min_modified_time:
        #    self.min_modified_time = self.min_modified_time_min
        
        self.tasks            = []
        
        self.stat             = Statistic()
        self.FailTimeout      = [300, 120]
        self.progressInterval = 30
        self.lock             = threading.Lock()
        self.lastProgressDate = datetime.datetime.now()

        self.checkInLoop_printed = False

    # Возвращает контрольную сумму: если в программе всё в порядке, то сумма на момент завершения всех загрузок должна быть равна нулю
    def getCheckSumm(self):
        return self.stat.updloadedFiles + self.stat.skippedFiles + self.stat.CheckedOldFiles - self.stat.allFiles

    
    def check(self, noPrint=False):
        try:
            # Проверка подключения
            if self.client.check():
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

    def printBadNetwork(self):
        try:
            self.lock.acquire()

            if not self.checkInLoop_printed:
                print("bad network " + datetime.datetime.now().strftime("%H:%M:%S"))
                self.checkInLoop_printed = True

        finally:
            self.lock.release()

    def checkInLoop(self):
        while not self.check(True):
            self.printBadNetwork()
            time.sleep(60)

        # Окончание функции - связь восстановилась
        try:
            self.lock.acquire()

            if self.checkInLoop_printed:
                self.checkInLoop_printed = False
                print("network restored " + datetime.datetime.now().strftime("%H:%M:%S"))
        finally:
            self.lock.release()

    def printProgress(self, i, lenDir):
        try:
            if len(self.oldstat) <= 0:
                return

            old = self.oldstat[0]

            self.lock.acquire()
            progress = (i+1)*100/lenDir
            curTime = datetime.datetime.now()
            if (curTime - self.lastProgressDate).total_seconds() > self.progressInterval:
                #if progress < 0:
                #    progress = 0

                # {progress:3.0f}% \t
                print(f"up {self.stat.updloadedFiles - old.updloadedFiles},\tchecked {self.stat.CheckedOldFiles - old.CheckedOldFiles},\tsk {self.stat.skippedFiles - old.skippedFiles}\t{curTime.strftime("%H:%M:%S")}")


                self.lastProgressDate = datetime.datetime.now()
        finally:
            self.lock.release()

    def doUpdateFile(self, rFileName, lFileName, threadPool, doPrint, index, lenDir, isFailed=False):
        try:
            self._doUpdateFile(rFileName, lFileName, threadPool, doPrint, index, lenDir, isFailed)
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            print(type(e))

            try:
                self.lock.acquire()
                self.stat.failedFiles += 1
            finally:
                self.lock.release()

    # client.info(...):
    # {'created': '2025-03-19T05:40:04Z', 'name': '0000000001', 'size': '65536', 'modified': 'Wed, 19 Mar 2025 05:40:04 GMT', 'etag': '6c1249976b5f15b6b517e6a147ca0dbf', 'content_type': 'application/octet-stream'}

    # rFileName - имя удалённого файла
    # lFileName - имя локального файла
    def _doUpdateFile(self, rFileName, lFileName, threadPool, doPrint, index, lenDir, isFailed=False):

        if doPrint.value >= PrintCommandState.FULL.value:
            print("Проверка файла " + rFileName)

        strNewFile = ""
        try:
            mtime     = os.path.getmtime(lFileName)
            lmodified = datetime.datetime.fromtimestamp(mtime)

            if self.min_modified_time:
                if self.min_modified_time > lmodified:
                    if doPrint.value >= PrintCommandState.FULL.value:
                        print("Пропущен файл (слишком старый): " + rFileName)

                    try:
                        self.lock.acquire()
                        self.stat.skippedFiles += 1
                    finally:
                        self.lock.release()

                    self.printProgress(index, lenDir)
                    return

            # Ожидаем блокировку и сразу её освобождаем:
            # чтобы не мешать файлу загружаться, просто ждём блокировку и отпускаем
            try:
                if self.doSingleUpdate:
                    self.singleUpdLock.acquire()
            finally:
                if self.doSingleUpdate:
                    self.singleUpdLock.release()
        
            if self.sleepForTask:
                time.sleep(self.sleepForTask)

            info = self.client.info(rFileName)

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
            self.printBadNetwork()
            time.sleep(random.randint(0, 60))
            self.checkInLoop()
            res = threadPool.submit(self.doUpdateFile, rFileName, lFileName, threadPool, doPrint, index, lenDir, False)
            self.tasks.append(res)
            return

        except webdav3.exceptions.ConnectionException:
            self.printBadNetwork()
            time.sleep(random.randint(0, 60))
            self.checkInLoop()
            res = threadPool.submit(self.doUpdateFile, rFileName, lFileName, threadPool, doPrint, index, lenDir, False)
            self.tasks.append(res)
            return

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            print(type(e))

            if isFailed:
                try:
                    self.lock.acquire()
                    self.stat.failedFiles += 1
                finally:
                    self.lock.release()
            else:
                time.sleep(self.FailTimeout[0] + random.randint(0, self.FailTimeout[1]))
                self.checkInLoop()
                res = threadPool.submit(self.doUpdateFile, rFileName, lFileName, threadPool, doPrint, index, lenDir, True)
                self.tasks.append(res)

            return


        if rmodified <= lmodified:
            try:
                try:
                    if self.doSingleUpdate:
                        self.singleUpdLock.acquire()

                    if doPrint.value >= PrintCommandState.SHORT.value or rmodified == 0 and doPrint.value >= PrintCommandState.NEW.value:
                        print("Обновление файла " + rFileName + f" [remote {rmodified}, local {lmodified}; {datetime.datetime.now().strftime("%H:%M:%S")}]")

                    def progress_update(current, total):
                        print(f"{current} / {total}")

                    # В общем, ничего не работает по частям всё равно
                    # force - кажется, не работает в этой функции
                    # progress нужен для передачи файла по частям
                    self.client.upload_sync(remote_path=rFileName, local_path=lFileName, progress=progress_update)
                finally:
                    if self.doSingleUpdate:
                        self.singleUpdLock.release()

                if doPrint.value >= PrintCommandState.DONE.value:
                    print("Обновление файла " + rFileName + " закончилось успешно." + strNewFile)

                try:
                    self.lock.acquire()
                    self.stat.updloadedFiles += 1
                finally:
                    self.lock.release()

            except webdav3.exceptions.NoConnection:
                if doPrint.value >= PrintCommandState.SHORT.value:
                    print("Разрыв соединения с сетью при обновлении файла " + rFileName + f"; {datetime.datetime.now().strftime("%H:%M:%S")}")
                self.printBadNetwork()
                self.checkInLoop()
                res = threadPool.submit(self.doUpdateFile, rFileName, lFileName, threadPool, doPrint, index, lenDir, False)
                self.tasks.append(res)

                return
            except webdav3.exceptions.ConnectionException:
                if doPrint.value >= PrintCommandState.SHORT.value:
                    print("Разрыв соединения с сетью при обновлении файла " + rFileName + f"; {datetime.datetime.now().strftime("%H:%M:%S")}")
                self.printBadNetwork()
                self.checkInLoop()
                res = threadPool.submit(self.doUpdateFile, rFileName, lFileName, threadPool, doPrint, index, lenDir, False)
                self.tasks.append(res)

                return
            except Exception as e:
                print("------------------------------------------------")
                print("Обновление файла " + rFileName + " ПРОВАЛИЛОСЬ!")
                print(f"Произошла ошибка: {str(e)}")
                print(type(e))
                print("------------------------------------------------")

                if isFailed:
                    try:
                        self.lock.acquire()
                        self.stat.failedFiles += 1
                    finally:
                        self.lock.release()
                else:
                    time.sleep(self.FailTimeout[0] + random.randint(0, self.FailTimeout[1]))
                    self.checkInLoop()
                    res = threadPool.submit(self.doUpdateFile, rFileName, lFileName, threadPool, doPrint, index, lenDir, True)
                    self.tasks.append(res)

                return

        # Если файл уже обновлён (судя по дате)
        else:
            try:
                self.lock.acquire()
                self.stat.CheckedOldFiles += 1
            finally:
                self.lock.release()

        self.printProgress(index, lenDir)

    def push(self, remote, local, name, doPrintFiles=PrintCommandState.NONE, recurse=""):

        self.tasks = []
        oldstat    = copy.deepcopy(self.stat)
        self.checkInLoop()

        current_time = datetime.datetime.now()
        if len(recurse) == 0 or self.doPrintSubdirs:
            self.oldstat.insert(0, oldstat)
            print()
            print("Обновление " + name + recurse)
            print(current_time.strftime("%Y.%m.%d %H:%M:%S"))

        # dirList = client.list(remote)
        dirList = os.listdir(local)
        for i, file in enumerate(dirList):

            rFileName = os.path.join(remote, file)
            lFileName = os.path.join(local,  file)

            if os.path.isdir(lFileName):
                # Ждём завершения задач
                for i, task in enumerate(self.tasks):
                    task.result()

                # print(f"ОШИБКА: в директории найдена папка '{lFileName}'. Папки не сихронизируются, только отдельные файлы!")
                # break
                successDir = False
                while not successDir:
                    try:
                        info = self.client.info(rFileName)
                        successDir = True
                    except webdav3.exceptions.RemoteResourceNotFound:
                        self.client.mkdir(rFileName)
                        successDir = True

                        if doPrintFiles.value >= PrintCommandState.NONE.value:
                            print(f"Создана директория " + rFileName)

                    except webdav3.exceptions.ConnectionException:
                        self.checkInLoop()
                        continue
                    except Exception as e:
                        try:
                            self.lock.acquire()
                            self.stat.failedFiles += 1
                        finally:
                            self.lock.release()

                        print(f"Произошла ошибка: {str(e)}")
                        print(type(e))
                        print(f"Пропущена директория {rFileName} | {lFileName}")
                        break

                if successDir:
                    self.push(rFileName, lFileName, name,  doPrintFiles, f" [{rFileName}]")
                continue

            try:
                #print(dir(self.stat))
                #print(self.stat.allFiles)
                
                self.lock.acquire()
                self.stat.allFiles += 1
            finally:
                self.lock.release()

            # doUpdateFile(rFileName, lFileName, doPrintFiles)
            res = self.threadPool.submit(self.doUpdateFile, rFileName, lFileName, self.threadPool, doPrintFiles, i, len(dirList))
            self.tasks.append(res)

        # Ждём завершения задач
        for i, task in enumerate(self.tasks):
            task.result()

        if len(recurse) == 0 or self.doPrintSubdirs:
            print()
            #if len(recurse) == 0:
            print("Закончено " + name + recurse + f" [up {self.stat.updloadedFiles - oldstat.updloadedFiles}, checked {self.stat.CheckedOldFiles - oldstat.CheckedOldFiles}, sk {self.stat.skippedFiles - oldstat.skippedFiles}, all {self.stat.allFiles - oldstat.allFiles}]")
            #else:
                #print("Закончено " + name + recurse + f" [all {self.stat.allFiles - oldstat.allFiles}]")
            current_time = datetime.datetime.now()
            print(current_time.strftime("%Y.%m.%d %H:%M:%S"))

            self.oldstat.pop(0)


state = State()

authLines = []
with open("/home/main/users/webdav/pwd", 'r') as file:
    authLines = file.read().splitlines()

options = {
    'webdav_hostname': "https://webdav.yandex.ru/",
    'webdav_login'   : authLines[0].strip(),
    'webdav_password': authLines[1].strip(),
    'verbose'        : True,                    # Похоже, этих опций тут нет
    'chunk_size'     : 1024*1024,
    'webdav_chunk_size' : 1024*1024,            # Не работает
    'webdav_timeout' : 20
}


# options['webdav_login']    = input("Введите имя пользователя: ")
# options['webdav_password'] = getpass.getpass(f"Введите пароль для пользователя {options['webdav_login']}:\n")


state.client = wc.Client(options)

# print(f"chunk_size: {state.client.chunk_size}")

state.checkInLoop()


state.push('/Arcs/reserve/keys/',    '/Arcs/Disks/Reserve/keys',    "keys",    state.doPrintFiles)
state.push('/Arcs/reserve/records/', '/Arcs/Disks/Reserve/records', "records", state.doPrintFiles)
state.push('/Arcs/reserve/books3/',  '/Arcs/Disks/Reserve/books3',  "books3",  state.doPrintFiles)
state.push('/Crypto/',               '/Arcs/Disks/ya/Crypto/',      "Crypto",  state.doPrintFiles)
state.push('/Ключи/',                '/Arcs/Disks/ya/Ключи/',       "Ключи",   state.doPrintFiles)
state.push('/Arcs/TorBrowser/',      '/Arcs/Disks/ya/Arcs/TorBrowser/', "TorBrowser",  state.doPrintFiles)
#state.push('/',                     '/Arcs/Disks/ya/',             "/",   state.doPrintFiles)


# Ждём завершения задач
for i, task in enumerate(state.tasks):
    task.result()

state.threadPool.shutdown(True)

#thread1 = threading.Thread(target=push, args=('/Arcs/keys',    '/Arcs/Disks/Reserve/keys',    "keys"))
#thread2 = threading.Thread(target=push, args=('/Arcs/records', '/Arcs/Disks/Reserve/records', "records"))
#thread3 = threading.Thread(target=push, args=('/Arcs/books3',  '/Arcs/Disks/Reserve/books3',  "books3"))
#thread1.start()
#thread2.start()
#thread3.start()


#thread1.join()
#thread2.join()
#thread3.join()

print()
print()

current_time = datetime.datetime.now()
print(current_time.strftime("%Y.%m.%d %H:%M:%S"))
if state.stat.failedFiles > 0:
    print()
    print("----------------------------------------------------------------------------------------")
    print(f"!!! При работе программы были обнаружены неустранимые ошибки в количестве {state.stat.failedFiles} !!!")
    print("          Попробуйте запустить синхронизацию повторно")
    print("----------------------------------------------------------------------------------------")
    print()

if state.stat.failedFiles == 0 and state.getCheckSumm() == 0:
    with open(state.DateFileName, "w") as file:
        state.start_time += datetime.timedelta(seconds=-1)
        file.write(state.start_time.strftime(state.DateFileFormat))
else:
    print()
    print("----------------------------------------------------------------------------------------")
    print(f"!!! Контрольная сумма не сошлась! !!!")
    print(f"Загружено на сервер {state.stat.updloadedFiles}, проверено и пропущено {state.stat.CheckedOldFiles}, пропущено без проверки {state.stat.skippedFiles}, всего: {state.stat.allFiles}, должно быть всего: {state.stat.updloadedFiles+state.stat.CheckedOldFiles+state.stat.skippedFiles}")
    print("----------------------------------------------------------------------------------------")
    print()

if state.min_modified_time:
    
    print(f"Программа завершена. Загружено {state.stat.updloadedFiles} файлов. Проверено по дате и пропущено {state.stat.CheckedOldFiles} файлов. Всего файлов обработано: {state.stat.allFiles}. Пропущена проверка (слишком старые) {state.stat.skippedFiles} файлов. Комментарий: старые файлы не будут пропускаться, если файл {state.DateFileName} удалён или дата в этом файле поставлена ранее, чем время создания самых старых файлов.")

    totalHours = (state.start_time - state.min_modified_time).total_seconds()/3600
    print(f"Обновлялись только файлы новее, чем {state.min_modified_time.strftime("%Y.%m.%d %H:%M:%S")}  ({totalHours:.0f} часов)")

else:
    print(f"Программа завершена. Загружено {state.stat.updloadedFiles} файлов. Проверено по дате и пропущено {state.stat.CheckedOldFiles} файлов. Всего файлов обработано: {state.stat.allFiles}. Все файлы проверены по дате.")

print("sudo -u webdav python3 /inRamS/mounts/records/_sh/startup/cp-reserve.py")
