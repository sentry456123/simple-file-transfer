import common

import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(common.ADDR)

server.listen()

client, addr = server.accept()

file_name = client.recv(common.MAX_SIZE).decode()
file_size = client.recv(common.MAX_SIZE).decode()

file = open(file_name, "wb")
file_data = b""
progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

size = int(file_size)

while size < 0:
    data = client.recv(common.clamp(size, 0, common.MAX_SIZE))
    size -= common.MAX_SIZE
    file_data += data
    progress.update(common.MAX_SIZE)

file.write(file_data)

print(f"File name: {file_name}")
print(f"File size: {file_size}")

file.close()
client.close()
server.close()