import common

import socket
import sys
import os

if len(sys.argv) != 2:
    print("Invalid argument")
    print(f"Syntax: {sys.argv[0]} [File name]")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(common.ADDR)

file_name = sys.argv[1]
file_stats = os.stat(file_name)
file = open(file_name, "rb")
file_size = file_stats.st_size

print(f"File name: {file_name}")
print(f"File size: {file_size}")

client.send(file_name.encode())
client.send(str(file_size).encode())
client.sendall(file.read())

file.close()
client.close()