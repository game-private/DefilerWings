import argparse
import datetime
import os
import subprocess

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

with open(log, 'r') as file:
    logsLines = file.read().splitlines()


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

def downloadUrls(ulrs, dirName):
    global newUrlsCount
    global successfullDownloaded

    for i, url in enumerate(ulrs):
        
        if url in logsLines:
            print(f"Skip {url}")
            continue

        newUrlsCount += 1
        print(f"Try to get {url}")

        pi = subprocess.run(["yt-dlp", url])
        # pi = subprocess.run(["yt-dlp", "--cookies-from-browser", "firefox", url])

        if pi.returncode == 0:
            successfullDownloaded += 1
            with open(log, 'a', encoding='utf-8') as f:
                f.write(dirName + "\n" + url + "\n\n")

            continue

        print(f"returned {pi.returncode}")
        pi = subprocess.run(["yt-dlp", "--cookies-from-browser", "firefox", "-R 1", "--extractor-retries", "1", "--fragment-retries", "1", "--file-access-retries", "1", url])


def enumerateDirs(dirs, RecurseCnt):
    global successfullDownloaded
    global RecurseTarget
    global RecurseMax
    
    if RecurseCnt > RecurseTarget:
        RecurseMax += 1
        return

    for i, (dirName, fileName) in enumerate(dirs):
        # Прерываем цикл закачки, чтобы проверить списки с самого начала
        if successfullDownloaded > 0:
            return

        print()
        print("------------------------------------------------")
        print(f"Work with directory {dirName} ({fileName})")
        print()
        
        os.chdir(dirName)

        # Парсим url из файла и скачиваем их
        if os.path.isfile(fileName):
            urls = getUrls(fileName)

            downloadUrls(urls, dirName)


        # Проверяем поддиректории
        subdirs  = os.listdir(dirName)
        subDescs = []
        for i, subDirName in enumerate(subdirs):
            subDirName = os.path.join(dirName, subDirName)
            subDescs.append([subDirName, "all"])

        enumerateDirs(subDescs, RecurseCnt + 1)



RecurseMax    = 0
RecurseTarget = 0
while True:
    newUrlsCount = 0
    successfullDownloaded = 0
    
    enumerateDirs(dirs, 0)

    if newUrlsCount <= 0:
        if RecurseMax <= 0:
            break;
        else:
            RecurseTarget += 1
    else:
        RecurseTarget = 0


print()
print()
print(f"See result in {log}")

