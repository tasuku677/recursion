import socket
import os
from faker import Faker
fake = Faker()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((socket.gethostname(), 1235))
server_address = "/socket_file"
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass
print('Starting up on {}'.format(server_address))

while True:
    print("\n wating to receive message")
    data, address = sock.recvfrom(4096)
    print("received {} bytes from {}".format(len(data), address))
    print(data)
    if data:
        response = data.decode() + "lives" + fake.address()
        sent = sock.sendto(response.encode(), (address, 2000))
    
