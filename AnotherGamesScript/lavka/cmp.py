#!/usr/bin/python3

import argparse
import datetime
import os
#import subprocess
import time

current_datetime = datetime.datetime.now()
print(current_datetime)
print(os.path.realpath(__file__))

#parser = argparse.ArgumentParser()
#parser.add_argument('file1')
#parser.add_argument('file2')
#args = parser.parse_args()
#print(args.file1)
#print(args.file2)
#print()
#print()

file1 = "s1"
file2 = "s2"
filer = "sr"


def ReadFile(FileName):
    with open(FileName, 'r') as file:
        logsLines = file.read().splitlines()
    
    return doFiltrateArray(logsLines)

def WriteToLog(fr, FileName):

    with open(FileName, 'w', encoding='utf-8') as f:
        for (i, e) in enumerate(fr):
            f.write(e + "\n")


def doFiltrateArray(array):
    i = 0
    while i < len(array):
        str = array[i]
        if str.startswith("https://"):
            i += 1
            continue
        
        array.pop(i)
    
    return array

# f1 - должен быть старым файлом, f2 - новым файлом
f1 = ReadFile(file1)
f1.sort()
f2 = ReadFile(file2)
f2.sort()

f3 = []

i = 0
j = 0
while i < len(f2) and j < len(f1):
    if f1[j] < f2[i]:
        j += 1
        continue
    if f1[j] > f2[i]:
        f3.append(f2[i])
        print(f2[i])
        i += 1
        continue

    i += 1
    j += 1


WriteToLog(f3, filer)
