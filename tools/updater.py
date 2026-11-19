from colorama import Fore
from os.path import isfile
from requests import get
from requests.exceptions import ConnectionError
from os import system, chdir
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
VERSION_FILE = BASE_DIR / "VERSION.txt"


def mainUpdater():
    UPtDATE = None
    try:
        vsersionNum = get(
            "https://raw.githubusercontent.com/AdolfMacro/eyeRat/main/VERSION.txt"
        ).text
    except ConnectionError:
        print(f"{Fore.RED}[*] Connection Error !")
        return 1
    if not vsersionNum.strip() == open(f'{VERSION_FILE}', 'r').read().strip():
        UPtDATE = False
    else:
        UPtDATE = True
    if isfile("/usr/src/eyerat/VERSION.txt"):
        if UPtDATE:
            input(f"{Fore.LIGHTGREEN_EX}Your version is up to date!\n\nEnter to continue : {Fore.RESET}")
            return
        WtUpDate = input(f"{Fore.LIGHTRED_EX}Your version is not up to date!\n\nDo you want to be updated [y/n]? : {Fore.RESET}").lower()
        if WtUpDate == 'y':
            chdir(BASE_DIR / "tools")
            system("bash updater.sh")
        else:
            input(f"{Fore.LIGHTCYAN_EX}\n\nEnter to continue : {Fore.RESET}")
    else:
        upErr = input(f"""{Fore.LIGHTRED_EX}Error: You did not install the tool! \nIf you are using Linux based systems, please install the tool with the tools/installer.sh file, or download the update manually.
    \nDo you want to check the version of your tool [y/n] ? {Fore.RESET}""").lower()
        if upErr == 'y':
            if UPtDATE:
                input(f"{Fore.LIGHTGREEN_EX}Your version is up to date!\n\nEnter to continue : {Fore.RESET}")
            else:
                input(f"{Fore.LIGHTRED_EX}Your version is not up to date!\n\nEnter to continue : {Fore.RESET}")