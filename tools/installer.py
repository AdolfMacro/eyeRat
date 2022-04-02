from os import system ,getcwd
from colorama import Fore
from platform import system as osName
from subprocess import getoutput

nsPkgs=[]
try:
    import cv2
except ModuleNotFoundError:
    nsPkgs.append("python-opencv")
if "windows" in osName().lower():
    print(f"{Fore.LIGHTRED_EX} ¯\_( ͡° ͜ʖ ͡°)_/¯ This option is not available for Windows operating system!")
    exit()
selection=input(f"""{Fore.LIGHTGREEN_EX}
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \\
\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/ /
 \/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /
 / /\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\/ /\\
/ /\ \/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\ \/\ \\
\ \/\ \                                                    /\ \/ /
 \/ /\ \ [ 1 ] Installation with dependencies             / /\/ /
 / /\/ /                                                  \ \/ /\\
/ /\ \/                                                    \ \/\ \\
\ \/\ \                                                    /\ \/ /
 \/ /\ \         [ 2 ] Installation without dependencies  / /\/ /
 / /\/ /                                                  \ \/ /\\
/ /\ \/                                                    \ \/\ \\
\ \/\ \.--..--..--..--..--..--..--..--..--..--..--..--..--./\ \/ /
 \/ /\/ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ /\/ /
 / /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\\
/ /\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \\
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'

{Fore.LIGHTMAGENTA_EX}Enter your selection : {Fore.RESET}""")
if selection=='1':
    dependencies=['clipboard','opencv-python','PyAudio','PyAutoGUI','cryptography','PyMsgBox','Pillow','psutil','colorama']
    insPkgs=getoutput("pip freeze")
    nsPkgs=[]
    for i in dependencies:
        if not i in insPkgs:
            nsPkgs.append(i)
    if nsPkgs:
        for j in nsPkgs:
            system(f"pip3 install {i}")
elif selection=='2':
    errcode = system("sudo mkdir /usr/src/eyerat/")
    pathF="/usr/src/eyerat/"
    path=getcwd().replace("tools","")
    system(f"sudo cp -R {path}/* {pathF}")
    system(f"sudo echo 'python3 {pathF}eyeRat.py' > /usr/local/bin/eyerat")
    system(f"sudo chmod +x /usr/local/bin/eyerat")