# Накладывает на все файлы (но не директории) chattr +i, удаляет чтение для others и запись для всех
# +t на директории
# Зайти в директорию и вызвать (без sudo; отдельные команды sudo уже должны быть разрешены в sudoers)
# python3 /inRamS/mounts/records/_sh/py/chattr+i.py

import argparse
import datetime
import os
import subprocess
import time
import random
import traceback

current_datetime = datetime.datetime.now()
print(current_datetime)

# scriptPath = '/inRamS/mounts/records/_sh/py/yt-dlp.py'
# print(scriptPath)
print(os.path.realpath(__file__))

# ownerString = "undelete:arcs-read"
groupString = ":arcs-read"
ownerString = "undelete"


def doEnumerateDir(dirName):
    subdirs = os.listdir(dirName)
    subdirs.sort()

    for i, subDirName in enumerate(subdirs):
        subDirName = os.path.join(dirName, subDirName)
        
        if os.path.islink(subDirName):
            return

        try:

            if os.path.isdir(subDirName):
                process = subprocess.run(["chmod", "+t", subDirName])
                process = subprocess.run(["chmod", "o-rwX", subDirName])
                process = subprocess.run([         "chown", groupString, "--", subDirName])
                process = subprocess.run(["sudo",  "chown", ownerString, "--", subDirName])
                doEnumerateDir(subDirName)
            else:
                process = subprocess.run(["chmod", "o-r", subDirName])
                process = subprocess.run(["chmod", "a-w", subDirName])
                process = subprocess.run(["sudo",  "chown",  ownerString, "--", subDirName])
                process = subprocess.run(["sudo",  "chattr", "+i",        "--", subDirName])

        except Exception as e:
            exception_traceback = traceback.format_exc()
            print()
            print("------------------------------------------------")
            print("Error for " + subDirName)
            print(exception_traceback)
            print()


doEnumerateDir(os.getcwd())

