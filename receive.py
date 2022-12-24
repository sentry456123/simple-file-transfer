import common

import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(common.ADDR)

server.listen()

client, addr = server.accept()

file_name = client.recv(common.MAX_SIZE).decode()
file_size = client.recv(common.MAX_SIZE).decode()

print(f"File name: {file_name}")
print(f"File size: {file_size}")

file = open(file_name, "wb")
progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))
# file_data = b""
size = int(file_size)

print(size)

while size >= 0:
    data = client.recv(common.clamp(size, 0, common.MAX_SIZE))
    size -= common.MAX_SIZE
    file.write(data)
    progress.update(common.MAX_SIZE)

file.close()
client.close()
server.close()