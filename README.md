<p align="center">
  <img 
    width="150"
    height="150"
    src="https://github.com/AdolfMacro/AdolfMacro/blob/main/logo.png"
  >
</p>


## EyeRat 🐁
### Options :

- Voice recording 🎤
- Take photos 📷
- Live stream from camera 👀
- Take screenshot 🖼️
- File explorer 📁
- CLI remote command shell 🚀
- Make custom popup box 📦
- R/W clipboard 📋
- Manage multiple RATs 🌱
- Other ...
-------
###  Dependencies :
#### Libraries :
- clipboard
- socket
- openCV
- pyaudio
- pyautogui
- cryptography
- pymsgbox
- Pillow
- psutil
- wave
- colorama
- pyinstaller
-------
### How it works :
#### General description :
This program generally has two parts RAT and user side program. Whenever the user has an instruction to send to RAT, the user's application sends a special command to RAT such as: Tpict (to take a photo from the camera). After receiving the command, a function is executed to execute the user command in the victim system. At the same time, a user-side function starts receiving client/server information and displaying or saving it.

#### Code description :

1.Voice recording :


Command :
```
Rsound
```

- RAT.recSound(connection):
First set CHUNK to 1024 and RATE (fs variable) to 44,100 . It then receives the recording time from the client/server . Finally, it opens a stream and saves the frames in a list with a loop and sends the list items that are in bytes.


 -  .getSound(connection,time) :
First, we send the recording time to the client/server (target) through the socket connection ; Then in the current path create a file called Voice.wav and set its [channel](https://www.wildlifeacoustics.com/resources/faqs/what-is-an-audio-channel "channel") to 2 , then we get [sampwidth](https://www.phonetik.uni-muenchen.de/forschung/BITS/TP1/Cookbook/node62.html "sampwidth") from the client/server (target) and finally, we receive and save the recorded audio frames from the target .



2.Take photos :


Command :
```
Tpict
```

- RAT.getPict(connection):
Reads a frame from camera number 0 using the vid object (cv2.VideoCapture (0)) .Converts it to list from numpy.array and then converts it to str using json.dumps.

- .getPict(connection):
Receives the frame and converts it to numpy.array and finally saves it to image.jpg.


3.Live stream :


Command :
```
Glive
```

- RAT.live(connection) :
Reads frames from camera number 0 using the vid object (cv2.VideoCapture (0)). Converts it from numpy.array to list and then converts it to str using json.dumps and sends them.
This cycle continues as long as it is connected.

- .getLive(connection) :
Converts submitted frames to numpy.array and displays them one after the other.

4.Take screenshot :


Command :
```
Tscr
```

- RAT.takeScr(connection) :
Takes a screenshot using pyautogui.screenshot and converts it to numpy.array then converts it to a list finally convert the list to str and send it.

- .getScr(connection) :
Receives the frame and converts it to numpy.array and finally saves it to screenshot.jpg.

5.File explorer :


- Search in current path :
Searches for current path files.

- Redirect .

-  Current path files :
List of  current path files (ls OR dir command).

- Edit file :
Downloads it using the file name and after downloading you have to edit the downloaded file and enter the Enter key to apply the changes.

- Download file .

- Remove file/folder.

- Upload file.
Uploads a file to the desired system (current path).


6.CLI remote command shell :


Command :
```
RMCM
```

- What is encryption/decryption key ?
Execution of remote commands must be encrypted because firewalls and Windows Defender can detect commands and close processes.
This is why for every RAT that is created, a key is needed to decrypt / encrypt it.


**NOTE** : Try not to enter commands that cause the program to crash, for example: Commands that ask the user to enter something and such commands.

7.Make custom popup box :



- Alert window:
Display a window with OK and Cancel buttons

- Confirm window :
A window to receive confirmation from the user.

- Question window
Ability to ask multiple choice questions (buttons) from the user.

- Password window :
A window to get the password from the user .

8.Other :


- Fun hacked alert :


Command :
```
HDalert
```
This section receives a photo from the user and sends it to the client/server (target) (like the frame sending methods described earlier).
The RAT then opens the image 1000 times in different windows and the victim system crashes.

- Target system info :
Receives and displays some victim system information.

-------

### Usage :
```
git clone https://github.com/AdolfMacro/eyeRat.git
cd eyeRat
python3 eyeRat.py
```
### Installation(linux) :
#### How to install on **Linux**:
```
git clone https://github.com/AdolfMacro/eyeRat.git
cd eyeRat/tools/
bash installer.sh
```
**Please run with normal user (do not run with root user)**

-------

### General instructions for use:

You must first obtain the victims IP address.
Then you have to create an executable file (depending on the type of your operating system) using the generator option.
Finally, the executable file must be executed on the target system.
Now you need to go to the client launcher section and enter the IP address and port
Now the usage menu and commands open, you can use them according to your needs.

In version 1.0.0, there is no need to find the victim's IP and the tool can also be used as a reverse connection.

--------
The use of the eyeRat(all versions) COMPLETE RESPONSIBILITY of the END-USER. Developers assume NO liability and are NOT responsible for any misuse or damage caused by this program.

--------
### Screenshots :
![menu1](https://github.com/AdolfMacro/eyeRat/blob/main/screenshots/1.png?raw=true)


![menu2](https://github.com/AdolfMacro/eyeRat/blob/main/screenshots/2.jpg?raw=true)


![menu3](https://github.com/AdolfMacro/eyeRat/blob/main/screenshots/3.jpg?raw=true)


![menu4](https://github.com/AdolfMacro/eyeRat/blob/main/screenshots/4.png?raw=true)


![menu5](https://github.com/AdolfMacro/eyeRat/blob/main/screenshots/5.png?raw=true)
--------

#### Upcoming update schedule 🌱 :

- **I will add the UDP connection option.**

- **I will optimize the code .**

- **And  ...**

