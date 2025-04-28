# Запускать из директории .git
# Даёт права a1 и устанавливает права на запись пользователю и группе, если "w" есть у пользователя или у группы

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


def getProcessOutput(params):
    process = subprocess.Popen(params, stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    outputLine = output.decode()
    return outputLine

def getLsOutputForCurDir(lsOutput, lineEnd = " ."):
    ls      = lsOutput.split('\n')
    result  = [False, False, False, False, False, False]
    pattern = 'rwxrwx'
    # Ищем первую точку в конце строки - это сведения о текущей директории
    for _,line in enumerate(ls):
        if line.endswith(lineEnd):
            for i in range(len(pattern)):
                result[i] =   line[i+1] == pattern[i]

            return result

    raise ValueError("getLsOutputForCurDir: not found line ' .'")

def doEnumerateDir(dirName):
    subdirs = os.listdir(dirName)
    subdirs.sort()

    for i, subDirName in enumerate(subdirs):
        subDirName = os.path.join(dirName, subDirName)
        
        if os.path.islink(subDirName):
            return

        try:

            if os.path.isdir(subDirName):
                ls     = getProcessOutput(['ls', '-al', subDirName])
                rights = getLsOutputForCurDir(ls)

                # Если хоть где-то стоит "w" (на группе или на пользователе) - добавляем "w" везьде
                if rights[1] or rights[4]:
                    process = subprocess.run(["chmod",          "ug+rwX",     subDirName])
                    process = subprocess.run(["chmod",          "a-t",        subDirName])
                    process = subprocess.run(["setfacl", "-dm", "u:a1:rwX",   subDirName])
                    process = subprocess.run(["setfacl", "-dm", "u:inet:rwX", subDirName])
                    process = subprocess.run(["setfacl", "-m",  "u:inet:rwX", subDirName])
                    process = subprocess.run(["setfacl", "-m",  "u:a1:rwX",   subDirName])
                else:
                    process = subprocess.run(["chmod",          "ug+rwX",    subDirName])
                    process = subprocess.run(["chmod",          "a-t",       subDirName])
                    process = subprocess.run(["setfacl", "-dm", "u:a1:rX",   subDirName])
                    process = subprocess.run(["setfacl", "-dm", "u:inet:rX", subDirName])
                    process = subprocess.run(["setfacl", "-m",  "u:inet:rX", subDirName])
                    process = subprocess.run(["setfacl", "-m",  "u:a1:rX",   subDirName])

                doEnumerateDir(subDirName)
            else:
                ls     = getProcessOutput(['ls', '-al', subDirName])
                rights = getLsOutputForCurDir(ls, "")

                if rights[1] or rights[4]:
                    process = subprocess.run(["chmod", "ug+rw", subDirName])
                    process = subprocess.run(["setfacl", "-m",  "u:a1:rw", subDirName])
                else:
                    process = subprocess.run(["chmod", "ug+rw", subDirName])
                    process = subprocess.run(["setfacl", "-m",  "u:a1:rw", subDirName])


        except Exception as e:
            exception_traceback = traceback.format_exc()
            print()
            print("------------------------------------------------")
            print("Error for " + subDirName)
            print(exception_traceback)
            print()


doEnumerateDir(os.getcwd())

