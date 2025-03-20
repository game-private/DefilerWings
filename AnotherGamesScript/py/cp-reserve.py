# https://github.com/CloudPolis/webdav-client-python

import webdav3.client as wc
import getpass
import time
import datetime
import os
import threading


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
files1 = client.list()

# for file in enumerate(files1):
#     print(file)


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

while not check(True):
    print("bad network")
    time.sleep(60)

# info
# {'created': '2025-03-19T05:40:04Z', 'name': '0000000001', 'size': '65536', 'modified': 'Wed, 19 Mar 2025 05:40:04 GMT', 'etag': '6c1249976b5f15b6b517e6a147ca0dbf', 'content_type': 'application/octet-stream'}

# datetime.datetime.strptime('Wed, 19 Mar 2025 05:40:04 GMT', '%a, %d %b %Y %H:%M:%S %Z')
# current_time = datetime.datetime.now()
# x = current_time.strftime("%a, %d %b %Y %H:%M:%S %z %Z")
# print(x)

def push(remote, local, name):
    current_time = datetime.datetime.now()
    print(current_time)

    while not check(True):
        print("bad network")
        time.sleep(60)
    
    print("Синхронизация " + name)
    result = client.push(remote_directory=remote, local_directory=local)
    print("Обновление " + name)
    
    current_time = datetime.datetime.now()
    print(current_time)
    
    dir = client.list(remote)
    for i, file in enumerate(dir):
        while not check(True):
            print("bad network")
            time.sleep(60)
        
        rFileName = f"{remote}/{file}"
        lFileName = f"{local}/{file}"
        info = client.info(rFileName)
        
        # print("Проверка файла " + rFileName)

        # Плюс три часа, т.к. время передаётся по гринвичу
        rmodified = datetime.datetime.strptime(info['modified'], '%a, %d %b %Y %H:%M:%S %Z')
        mtime     = os.path.getmtime(lFileName)
        lmodified = datetime.datetime.fromtimestamp(mtime)
        
        rmodified += datetime.timedelta(hours=3)

        # print(rmodified)
        # print(lmodified)
        
        if rmodified < lmodified:
            print("Обновление файла " + rFileName + f" [remote {rmodified}, local {lmodified}]")

            try:
                client.upload_sync(remote_path=rFileName, local_path=lFileName)
                print("Обновление файла " + rFileName + " закончилось успешно")
            except Exception as e:
                print("Обновление файла " + rFileName + " ПРОВАЛИЛОСЬ!")
                print(f"Произошла ошибка: {str(e)}")
                time.sleep(60)
    
    print("Закончено " + name)
    current_time = datetime.datetime.now()
    print(current_time)
    
    #if result:
    #    print("Синхронизация " + name + " успешно завершена")
    #else:
    #    print("Синхронизация " + name + " провалена")

# push('/Arcs/keys/',    '/Arcs/Disks/Reserve/keys',    "keys")
# push('/Arcs/records/', '/Arcs/Disks/Reserve/records', "records")
# push('/Arcs/books3/',  '/Arcs/Disks/Reserve/books3',  "books3")

thread1 = threading.Thread(target=push, args=('/Arcs/keys/',    '/Arcs/Disks/Reserve/keys',    "keys"))
thread2 = threading.Thread(target=push, args=('/Arcs/records/', '/Arcs/Disks/Reserve/records', "records"))
thread3 = threading.Thread(target=push, args=('/Arcs/books3/',  '/Arcs/Disks/Reserve/books3',  "books3"))
thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()

current_time = datetime.datetime.now()
print(current_time)
