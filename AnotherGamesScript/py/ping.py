# python3 /inRamS/mounts/records/_sh/py/ping.py

import argparse
import datetime
import os
import subprocess
import time
import random

# current_datetime = datetime.datetime.now()
# print(current_datetime)

current_datetime = datetime.datetime.now()
print(current_datetime.strftime("%H:%M:%S"))

# parser = argparse.ArgumentParser()
# parser.add_argument('filename')
# args = parser.parse_args()
# print(args.filename)

print("python3 " + os.path.realpath(__file__))

def isNoHavePing(cnt):
    process = subprocess.Popen(["ping", "77.88.8.88", "-s 16", "-O", "-c " + str(cnt), "-i 2.0"], stdout=subprocess.PIPE)
    output, error = process.communicate()

    outputLine = output.decode()
    
    if "100% packet loss" in outputLine or "packet loss" not in outputLine:
        return True
    
    return False
    

def beep(note, vol = "0.1"):
    process = subprocess.run(["play", "-q", "-n", "synth", "1.5", "pluck", note, "vol", vol])
    
class State:
    def __init__(self):
        self.sleeps      = { "connected": 5, "disconnected": 5 }
        
        self.sleep       = self.sleeps["disconnected"]
        self.isConnected = False
        self.isError     = False
        
        self.lastStatusChangedTime = datetime.datetime.now()
        
    def toConnectedState(self):
        
        if self.isConnected:
            return

        beep("%-9")
        self.isConnected = True
        self.isError     = False
        self.sleep       = self.sleeps["connected"]
        self.lastStatusChangedTime = datetime.datetime.now()
        print("connected " + self.lastStatusChangedTime.strftime("%H:%M:%S"))
    
    def toDisconnectedState(self):
        
        if not self.isConnected:
            return
        
        beep("%-21")
        self.isConnected = False
        self.sleep       = self.sleeps["disconnected"]
        self.lastStatusChangedTime = datetime.datetime.now()
        print("disconnected " + self.lastStatusChangedTime.strftime("%H:%M:%S"))
        



state = State()

def checkLog():
    global state

    if isNoHavePing(1):
        print("bad ping " + datetime.datetime.now().strftime("%H:%M:%S"))
        pingCount = 1
        if state.isConnected:
            pingCount = 3

        while isNoHavePing(1):
            while isNoHavePing(pingCount):
                state.toDisconnectedState()
                time.sleep(state.sleep)
                pingCount = 1

    state.toConnectedState()
            
    return True

while checkLog():
    time.sleep(state.sleep)
    


# Bootstrapped 15% Bootstrapped 75%

# Включая границы интервала
# random.randint(0, 15)


