# python3 /inRamS/mounts/records/_sh/py/torcheck.py
# sudo -u torcheck python3 /inRamS/mounts/records/_sh/py/torcheck.py
# watch -n 2 'sudo cat "/inRam-Logs/tor-8080.log" | fgrep -i boot | tail'


import argparse
import datetime
import threading
import subprocess
import random
import signal
import shutil
import time
import stat
import sys
import os
# apt install python3-dnspython
# import dns.resolver
import dns.query

def reRun():
    wellUser = 'torcheck'
    process  = subprocess.Popen(["whoami"], stdout=subprocess.PIPE)
    output, error = process.communicate()
    user = output.decode().splitlines()[0]
    if user != wellUser:
        print(f"rerun for user {wellUser}")
        subprocess.run(["sudo", '-u', wellUser, 'python3', os.path.realpath(__file__)])
        sys.exit(1)


reRun()

# current_datetime = datetime.datetime.now()
# print(current_datetime)

current_datetime = datetime.datetime.now()
print(current_datetime.strftime("%H:%M:%S"))

# parser = argparse.ArgumentParser()
# parser.add_argument('filename')
# args = parser.parse_args()
# print(args.filename)
class Args:
    pass

args=Args()
args.filename = "/inRam-Logs/tor-8080.log"
logFile = args.filename

print("python3 " + os.path.realpath(__file__))

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
        # "[warn]"
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
   
    if "packet loss" not in outputLine:
        return True
    
    return False
    
def beep(note, vol = "0.1"):
    process = subprocess.run(["play", "-q", "-n", "synth", "1.5", "pluck", note, "vol", vol])
    pass


class State:
    def __init__(self):
        minus = 0
        ADDS  = 2
        self.sleeps      = { "connected": 1, "disconnected": 1 }
        self.timeouts    = { "0": 48-minus, "10": 61-minus+ADDS, "15": 122-minus*2, "25": 122, "30": 604, "100": -1 }
        
        self.LastLogLen  = 0
        self.sleep       = self.sleeps["disconnected"]
        self.isConnected = False
        self.isError     = False
        self.timeout     = self.timeouts["0"]

        self.ConnectedPercent      = 0
        self.lastStatusChangedTime = datetime.datetime.now()
        self.dns_id                = 0
        self.isTerminated          = False
        
        # Подготовка файла, который будет создаваться, если tor успешно запустился
        # /inRamA/torstate/up
        self.torStateDir = "/inRamS/torstate"
        self.torUpFile   = os.path.join(self.torStateDir, "", "up")
        os.makedirs(self.torStateDir, exist_ok=True)
        os.chmod(self.torStateDir, stat.S_IRWXU | stat.S_IXGRP | stat.S_IRGRP | stat.S_IROTH | stat.S_IXOTH | stat.S_IRGRP)
        shutil.chown(self.torStateDir, group='forall')
        self.setTorUpFile(False)


    def setTorUpFile(self, isTorUp):
        if isTorUp:
            with open(self.torUpFile, 'a') as file:
                pass
        else:
            try:
                os.remove(self.torUpFile)
            except FileNotFoundError:
                pass

    def toConnectedState(self):
        self.isConnected = True
        self.isError     = False
        self.sleep       = self.sleeps["connected"]
        
        self.setTorUpFile(True);
        
        print()
        print("connected")
    
    def toDisconnectedState(self):
        self.isConnected = False
        self.sleep       = self.sleeps["disconnected"]
        self.lastStatusChangedTime = datetime.datetime.now()
        
        self.setTorUpFile(False);
        
        
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
        
        print("timeout: " + str(self.timeout) + f" ({self.ConnectedPercent}%)")

    def isErrorLine(self, line):
        ErrorTemplate = ["Problem bootstrapping", "connections have failed", "connections died in state"]
        # , "unable to connect OR connection"
        
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
            line  = line[btEnd:].strip()
            if "%" not in line:
                return False
            
            btEnd = line.index("%")
            line  = line[:btEnd]

            newVal = int(line)
            if newVal == 100 and newVal != self.ConnectedPercent:
                # Если в первый раз лог уже не пустой,
                # то мы можем много раз пройти не нужные нам линии успешного подключения
                if state.LastLogLen > 0:
                    beep("A5", "0.07")
            
            self.ConnectedPercent = newVal
            self.toRightConnetionState()
            return self.ConnectedPercent
        
        return False
        
def doRestartTor():
    global state

    state.toDisconnectedState()
    state.ConnectedPercent = 0

    process = subprocess.run(["sudo", "systemctl", "restart", "tor.service"])
    
    current_datetime = datetime.datetime.now()
    print()
    print()
    print("--------------------------------------------------")
    print("TOR restarted at " + current_datetime.strftime("%H:%M:%S"))
    time.sleep(7)


state = State()


def checkDNS(timeout = 240, domain_name = 'youtube.com.'):
    global state
    state.dns_id += 1

    nameserver  = '127.0.0.53'
    port        = 5353
    query       = dns.message.Message()
    query.id    = state.dns_id
    query.flags |= dns.flags.RD

    try:
        query.question.append(dns.rrset.from_text(domain_name, 0, dns.rdataclass.IN, 'A'))
        response = dns.query.udp(query, nameserver, port=port, timeout=timeout)
        # print(f"IP-адрес: {response.answer.to_text()}")
        if response.rcode() != dns.rcode.NOERROR:
            return False
        
        for rrset in response.answer:
            if rrset.rdtype == dns.rdatatype.A:
                for rdata in rrset:
                    # print(f"IP-адрес: {rdata.address}")
                    return True

    except dns.exception.Timeout:
        # print("Превышено время ожидания")
        pass
    except dns.exception.DNSException as e:
        pass
    
    return False
    

def checkDNS_cycle():
    global state

    while not state.isTerminated:
        time.sleep(1)
        if not state.isConnected or state.isTerminated:
            continue

        time.sleep(15 + random.randint(0, 15))
        if not state.isConnected or state.isTerminated:
            continue

        last = datetime.datetime.now()
        if checkDNS(180):
            interval = datetime.datetime.now() - last
            time.sleep(180 - interval.seconds + random.randint(0, 120))
            continue

        if not state.isConnected or state.isTerminated:
            continue

        print("checkDNS_cycle: first check has failed. " + datetime.datetime.now().strftime("%H:%M:%S"))
        if checkDNS(90, 'google.com.'):
            print("checkDNS_cycle: second check has succeeded. " + datetime.datetime.now().strftime("%H:%M:%S"))
            continue

        if state.isConnected:
            print("checkDNS_cycle: has a failed DNS check. Restarted. " + datetime.datetime.now().strftime("%H:%M:%S"))
            doRestartTor()


def checkLog():
    global state
    
    pingCount = 1
    isNoHavePingFlag = False
    if isNoHavePing(1):
        print("bad ping")
        if state.isConnected:
            pingCount = 2

        sleep = 0
        while isNoHavePing(pingCount):
            print("no ping")
            isNoHavePingFlag = True
            state.toDisconnectedState()
            state.ConnectedPercent = 0
            time.sleep(state.sleep + sleep)
            pingCount = 1
            sleep += 1
            if sleep > 15:
                sleep = 15


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

thread1 = threading.Thread(target=checkDNS_cycle, args=())
thread1.start()

def signal_handler(sig, frame):
    global state
    state.isTerminated=True
    state.setTorUpFile(False)
    print(f'Получен сигнал: {sig}')
    if sig == signal.SIGINT:
        # print('Программа прервана пользователем')
        sys.exit(0)
    elif sig == signal.SIGTERM:
        # print('Программа завершена по SIGTERM')
        sys.exit(0)

# Регистрация обработчиков сигналов
signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C
signal.signal(signal.SIGTERM, signal_handler)

while checkLog() and not state.isTerminated:
    if not state.isConnected or state.isError:
        interval = datetime.datetime.now() - state.lastStatusChangedTime
        current_datetime = datetime.datetime.now()
        # print("time " + current_datetime.strftime("%H:%M:%S") + " / " + str(interval.seconds))
        if state.isError or interval.seconds > state.timeout:
            doRestartTor()

    time.sleep(state.sleep)
    
state.isTerminated=True
state.setTorUpFile(False)

# Включая границы интервала
# random.randint(0, 15)


