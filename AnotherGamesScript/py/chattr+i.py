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



def doEnumerateDir(dirName):
    subdirs = os.listdir(dirName)
    subdirs.sort()

    for i, subDirName in enumerate(subdirs):
        subDirName = os.path.join(dirName, subDirName)

        try:
        
            if os.path.isdir(subDirName):
                doEnumerateDir(subDirName)
            else:
                process = subprocess.run(["chmod", "a-w", subDirName])
                process = subprocess.run(["sudo", "chattr", "+i",  "--", subDirName])

        except Exception as e:
            exception_traceback = traceback.format_exc()
            print()
            print("------------------------------------------------")
            print("Error for " + subDirName)
            print(exception_traceback)
            print()


doEnumerateDir(os.getcwd())

