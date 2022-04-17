echo -E """
         ___           _        _ _           
        |_ _|_ __  ___| |_ __ _| | | ___ _ __ 
         | || '_ \/ __| __/ _\` | | |/ _ \ '__|
         | || | | \__ \ || (_| | | |  __/ |   
        |___|_| |_|___/\__\__,_|_|_|\___|_|
        _____________________________________
    Installer for eyeRat tool , Start installation
    

"""
pip install clipboard
pip install opencv-python
pip install PyAudio
pip install PyAutoGUI
pip install cryptography
pip install PyMsgBox
pip install Pillow
pip install psutil
pip install colorama
sudo -u root mkdir /usr/src/eyerat/
line="$0"
replace="/tools/installer.sh"
replacewith=""
temp=$( realpath "$0"  )
line=$(dirname "$temp")
replace="/tools"
replacewith=""
line="${line/${replace}/${replacewith}}"
echo $line
sudo -u root cp -R $line/* /usr/src/eyerat/
sudo sh -c 'echo "python3 /usr/src/eyerat/eyeRat.py" > /usr/local/bin/eyerat'
sudo -u root chmod +x /usr/local/bin/eyerat
echo """
██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║  ██║██║   ██║██╔██╗ ██║█████╗  
██║  ██║██║   ██║██║╚██╗██║██╔══╝  
██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""
