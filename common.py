import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDR = (IP, PORT)
MAX_SIZE = 1024
FMT = "utf-8"

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))