import socket
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((socket.gethostname(), 2001))
server_address = socket.gethostname()
client_address = socket.gethostname()

inputstr = input("input a name of friend who you wanna meet")
message = inputstr.encode()

# sock.bind(client_address)

try:
    print("sending {}".format(message))
    sent = sock.sendto(message, (server_address, 2002))
    
    print("waiting to receive")
    data, server = sock.recvfrom(40)
    print("received {}".format(data))
finally:
    print("closing socket")
    sock.close()