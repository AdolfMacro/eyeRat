from importlib_metadata import version
from time import sleep
from tools import generator,updater
from colorama import Back , Fore
from tools import launcher
from os import system
from platform import system as osType 
from subprocess import getoutput
from os.path import isfile
from requests import get
from tools.MNLauncher import main as miniRats
def chdps():
  QModules=['opencv','numpy','pyautogui','pyaudio','cryptography','pymsgbox','pillow','psutil','colorama','pyinstaller']
  ntInstall=[]
  pipList=getoutput(("pip list")).lower()
  for pkg in QModules:
    if not pkg in pipList:
      ntInstall.append(pkg)
  if len(ntInstall):
    for NTpkg in ntInstall:
      print(f"{Fore.LIGHTRED_EX}[ ! ] Module {NTpkg} not found !\nTry with : pip3 install {NTpkg}\n\n")
    exit()
def clear():
    if "windows" in osType().lower():
        system("cls")
    else :
        system("clear")
def msgs():
  clear()
  msg=f"{Fore.LIGHTGREEN_EX}Be {Fore.LIGHTWHITE_EX}our {Fore.LIGHTRED_EX}voice 🇮🇷\n{Fore.GREEN}#opIRAN  {Fore.LIGHTWHITE_EX}#free_jadi  {Fore.LIGHTRED_EX}#mahsaamini\n\n{Fore.LIGHTCYAN_EX}-Adolf Macro"
  buff=""
  for i in msg:
    clear()
    buff+=i
    print(buff)
    sleep(0.1)
def main():
  msgs()
  sleep(3)
  clear()
  selection=input(f"""
         ____                                                               
        |{Back.RED} {Fore.BLACK}卐{Fore.RESET} {Back.RESET}|                                                              
        |{Back.RED}____{Back.RESET}|                                                              
       _|{Back.RED}____{Back.RESET}|_                                                             
      {Fore.LIGHTBLACK_EX}  /  @@`.                                                             
      .<     __O                                                            
     {Fore.LIGHTBLACK_EX}/\ \.-.' \     {Fore.CYAN}███████╗██╗   ██╗███████╗   ██████╗  █████╗ ████████╗{Fore.RESET}
    {Fore.LIGHTBLACK_EX}J  `.|`.\/ \    {Fore.CYAN}██╔════╝╚██╗ ██╔╝██╔════╝   ██╔══██╗██╔══██╗╚══██╔══╝{Fore.RESET}
    {Fore.LIGHTBLACK_EX}| |_.|  | | |   {Fore.CYAN}█████╗   ╚████╔╝ █████╗     ██████╔╝███████║   ██║   {Fore.RESET}
     {Fore.LIGHTBLACK_EX}\__.'`.|-' /   {Fore.CYAN}██╔══╝    ╚██╔╝  ██╔══╝     ██╔══██╗██╔══██║   ██║   {Fore.RESET}
     {Fore.LIGHTBLACK_EX}L   /|o`--'\   {Fore.CYAN}███████╗   ██║   ███████╗   ██║  ██║██║  ██║   ██║   {Fore.RESET}
     {Fore.LIGHTBLACK_EX}|  /\/\/\   \  {Fore.CYAN}╚══════╝   ╚═╝   ╚══════╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   {Fore.RESET}
{Fore.LIGHTBLACK_EX}     J /      `.__\                                                         
{Fore.LIGHTBLACK_EX}     |/         /  \                                                        
      \\      .'`.  `.                                            .'         
    ____)_/\_(____`.  `-._______________________________________.'/         
   (___._/  \_.___) `-.________________________________________.-'          

                 {Fore.RED}[ {Fore.CYAN}1 {Fore.RED}]{Fore.CYAN}Client launcher{Fore.RED}                      [ {Fore.CYAN}2 {Fore.RED}] {Fore.CYAN}Generate normal connection rat
                                                                                                   
                 {Fore.RED}[ {Fore.CYAN}3 {Fore.RED}]{Fore.CYAN}Server launcher(Multiple clients){Fore.RED}    [ {Fore.CYAN}4 {Fore.RED}] {Fore.CYAN}Generate reverse connection rat 

                 {Fore.RED}[ {Fore.CYAN}5 {Fore.RED}] {Fore.CYAN}Mini Rats{Fore.RED}                           [ {Fore.CYAN}6 {Fore.RED}] {Fore.CYAN}Developer information
                 
                 {Fore.RED}[ {Fore.CYAN}7 {Fore.RED}] {Fore.CYAN}Check for updates
                  
                  {Fore.LIGHTGREEN_EX}Enter your selection :{Fore.MAGENTA} """)
  clear()
  if selection=='1':
    try:
      launcher.main("client")
    except KeyboardInterrupt:
      pass
  elif selection == '2':
    try:
      generator.main("server",None)
    except KeyboardInterrupt:
      pass
  elif selection=='3':
    try:
      launcher.main("server")
    except KeyboardInterrupt:
      pass
  elif selection == '4':
    try:
      generator.main("client",None)
    except KeyboardInterrupt:
      pass
  elif selection=="5":
    try:
      miniRats()
    except KeyboardInterrupt:
      pass
  elif selection=='6':
    input("""
      _---~~(~~-_.
    _{        )   )         
  ,   ) -~~- ( ,-' )_       Hi, I'm Mani
 (  `-,_..`., )-- '_,)      You can get my complete information from this site:
( ` _)  (  -~( -_ `,  }     https://adolfmacro.github.io/mani/
(_-  _  ~_-~~~~`,  ,' )     
  `~ -^(    __;-,((()))     My GitHub Address: https://github.com/adolfmacro
        ~~~~ {_ -_(())      E-mail : m4nikamran@gmail.com
               `\  }        Telegram : https://t.me/manikamran
                 { }      
    
    
    Enter to exit : """)
  elif selection=="7":
    updater.mainUpdater()
if __name__=='__main__':
  chdps()
  while 1:
    try:
      main()
    except KeyboardInterrupt:
      print(f"\n\n{Fore.RED}ヽ(･_･)/{Fore.CYAN} CTR-C {Fore.RED}\(･_･)/{Fore.RESET}")
      break
