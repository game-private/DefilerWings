# python3 /inRamS/mounts/records/_sh/py/yt-dlp.py

import argparse
import datetime
import os
import subprocess
import time

current_datetime = datetime.datetime.now()
print(current_datetime)

print('/inRamS/mounts/records/_sh/py/yt-dlp.py')

# parser = argparse.ArgumentParser()
# parser.add_argument('filename')
# args = parser.parse_args()
# print(args.filename)
# print()
# print()

log  = '/Arcs/tmp/youtube/log'
dirs = [['/Arcs/tmp/youtube/144/', "144"], ['/Arcs/tmp/youtube/360/', "360"], ['/Arcs/tmp/youtube/480/', "480"]]

newUrlsCount = 0
successfullDownloaded = 0
logsLines = []


def ReadLog():
    global logsLines
    with open(log, 'r') as file:
        logsLines = file.read().splitlines()

ReadLog()


def getUrls(FileName):
    with open(FileName, 'r') as file:
        content = file.read().splitlines()

    r = []
    for i, line in enumerate(content):
        line = line.strip()
        if len(line) <= 0:
            continue
        if line.startswith("#"):
            continue
        
        r.append(line)

    return r

def WriteToLog(pi, dirName, url):
    global successfullDownloaded

    successfullDownloaded += 1
    with open(log, 'a', encoding='utf-8') as f:
        f.write(dirName + "\n" + url + "\n\n")

    ReadLog()

def downloadUrl(url, dirName):
    pi = subprocess.run(["yt-dlp", url])
    # pi = subprocess.run(["yt-dlp", "--cookies-from-browser", "firefox", url])

    # Ниже такой же фрагмент кода
    if pi.returncode == 0:
        WriteToLog(pi, dirName, url)
        print(f"Download successfully ended: {url}")
        print()
        return True

    print(f"returned {pi.returncode}")
    print()

    pi = subprocess.run(["yt-dlp", "--cookies-from-browser", "firefox", "-R 1", "--extractor-retries", "1", "--fragment-retries", "1", "--file-access-retries", "1", url])

    if pi.returncode == 0:
        WriteToLog(pi, dirName, url)
        print(f"Download successfully ended: {url}")
        print()
        return True
    else:
        print(f"returned {pi.returncode}")
        print()
        time.sleep(15)
        return False


# Если прошло больше указанного времени, то программа возвращается в цикл проверки корневых каталогов
# Время указывается в секундах
MAX_TIME_WITHOUT_CHECKING = 60 * 60

def isCheckingTimeOutExpired():
    global last_date
    global MAX_TIME_WITHOUT_CHECKING

    return datetime.datetime.now().timestamp() - last_date > MAX_TIME_WITHOUT_CHECKING


def downloadUrls(ulrs, dirName):
    global newUrlsCount
    global successfullDownloaded

    for i, url in enumerate(ulrs):
        if isCheckingTimeOutExpired():
            return

        # Прерываем цикл закачки, чтобы проверить списки с самого начала
        if successfullDownloaded > 0:
            return
        
        if url in logsLines:
            print(f"Skip {url}")
            continue

        newUrlsCount += 1
        print(f"Try to get {url}")

        triesCount = 0
        while triesCount < 2:
            triesCount += 1
            if triesCount >= 2:
                print("Try second time")
            if downloadUrl(url, dirName):
                break


def enumerateDirs(dirs, RecurseCnt):
    global successfullDownloaded
    global RecurseTarget
    global RecurseMax

    if isCheckingTimeOutExpired():
        return

    if RecurseCnt > RecurseTarget:
        RecurseMax += 1
        return

    for i, (dirName, fileName) in enumerate(dirs):
        # Прерываем цикл закачки, чтобы проверить списки с самого начала
        if successfullDownloaded > 0:
            return

        dirPrinted = False
        def printDir():
            nonlocal dirPrinted

            if dirPrinted:
                return

            print()
            print("------------------------------------------------")
            print(f"Work with directory {dirName} ({fileName})")
            print()
            
            dirPrinted = True
        
        os.chdir(dirName)

        # Парсим url из файла и скачиваем их
        if os.path.isfile(fileName):
            urls = getUrls(fileName)

            if len(urls) > 0:
                printDir()
                downloadUrls(urls, dirName)


        # Проверяем поддиректории
        subdirs  = os.listdir(dirName)
        subdirs.sort()
        subDescs = []


        for i, subDirName in enumerate(subdirs):
            subDirName = os.path.join(dirName, subDirName)

            if os.path.isdir(subDirName):
                subDescs.append([subDirName, "all"])

        # if len(subDescs) > 0:
        #    printDir()

        enumerateDirs(subDescs, RecurseCnt + 1)



RecurseMax    = 0
RecurseTarget = 0
while True:
    newUrlsCount = 0
    successfullDownloaded = 0
    last_date = datetime.datetime.now().timestamp()
    
    enumerateDirs(dirs, 0)
    ReadLog()

    if newUrlsCount <= 0:
        if RecurseMax <= 0:
            break;
        else:
            RecurseTarget += 1
            print(f"Recurse added: {RecurseTarget}")
            # time.sleep(15)
    else:
        RecurseTarget = 0


print()
print()
print(f"See result in {log}")
