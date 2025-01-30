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

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
# print(args.filename)

print(os.path.realpath(__file__) + " " + args.filename)

# "/inRam-Logs/tor-8080.log"
logFile = args.filename

def getLogLines():
    process = subprocess.Popen(["sudo", "cat", logFile], stdout=subprocess.PIPE)
    output, error = process.communicate()

    logLines = output.decode().splitlines()
    # logLines.reverse()
    
    return logLines


def isSignificantLine(line):
    SignificantTemplate = [
        "Problem bootstrapping",
        "connections died",
        "connections have failed",
        "Bootstrapped"
    ]
    
    for i, template in enumerate(SignificantTemplate):
        if template in line:
            return True
    
    return False

def isNoHavePing(cnt):
    process = subprocess.Popen(["ping", "77.88.8.88", "-s 16", "-O", "-c " + str(cnt), "-i 2.0"], stdout=subprocess.PIPE)
    output, error = process.communicate()

    outputLine = output.decode()
    
    if "100% packet loss" in outputLine:
        return True
    
    return False
    

class State:
    def __init__(self):
        self.sleeps      = { "connected": 15, "disconnected": 1 }
        self.timeouts    = { "0": 30, "10": 30, "15": 120, "25": 120, "30": 600, "100": -1 }
        
        self.LastLogLen  = 0
        self.sleep       = self.sleeps["disconnected"]
        self.isConnected = False
        self.isError     = False
        self.timeout     = self.timeouts["0"]

        self.ConnectedPercent      = 0
        self.lastStatusChangedTime = datetime.datetime.now()
        
    def toConnectedState(self):
        self.isConnected = True
        self.sleep       = self.sleeps["connected"]
    
    def toDisconnectedState(self):
        self.isConnected = False
        self.sleep       = self.sleeps["disconnected"]
        
    def toRightConnetionState(self):
        self.lastStatusChangedTime = datetime.datetime.now()

        if self.ConnectedPercent == 100:
            self.toConnectedState()
        else:
            self.toDisconnectedState()
        
        for i, percent in enumerate(self.timeouts):
            iPer = int(percent)
            if self.ConnectedPercent >= iPer:
                self.timeout = self.timeouts[percent]
        
        print("timeout: " + str(self.timeout))

    def isErrorLine(self, line):
        ErrorTemplate = ["Problem bootstrapping", "connections have failed", "connections died in state"]
        
        for i, template in enumerate(ErrorTemplate):
            if template in line:
                return True

        return False
                

    # isinstance(SetConnectedPercent(line), int)
    # isinstance(SetConnectedPercent(line), bool)
    def SetConnectedPercent(self, line):

        self.isError = False
        if self.isErrorLine(line):
            self.ConnectedPercent = 0
            self.toRightConnetionState()
            self.isError = True

            return 0

        BootstrappedString = "Bootstrapped "
        if BootstrappedString in line:
            btEnd = line.index(BootstrappedString) + len(BootstrappedString)
            line  = line[btEnd:]
            if "%" not in line:
                return False
            
            btEnd = line.index("%")
            line  = line[:btEnd]

            self.ConnectedPercent = int(line)
            self.toRightConnetionState()
            return self.ConnectedPercent
        
        return False
        
def doRestartTor():
    process = subprocess.run(["sudo", "systemctl", "restart", "tor.service"])
    time.sleep(2)

state = State()

def checkLog():
    global state
    
    isNoHavePingFlag = False
    while isNoHavePing(1):
        while isNoHavePing(7):
            print("no ping")
            isNoHavePingFlag = True
            state.toDisconnectedState()
            state.ConnectedPercent = 0

    if isNoHavePingFlag:
        doRestartTor()

    logLines = getLogLines()

    for i, line in enumerate(logLines):
        # Пропускаем уже просмотренные строки
        if i < state.LastLogLen:
            continue

        # Пропускаем все строки, которые не являются существенными
        if not isSignificantLine(line):
            continue

        print(line)
        if state.SetConnectedPercent(line) > 0:
            pass
        
    
    state.LastLogLen = len(logLines)
    return True

while checkLog():
    if not state.isConnected or state.isError:
        interval = datetime.datetime.now() - state.lastStatusChangedTime
        if state.isError or interval.seconds > state.timeout:
            doRestartTor()

    time.sleep(state.sleep)
    


# Bootstrapped 15% Bootstrapped 75%

# Включая границы интервала
# random.randint(0, 15)


