import socket
import os
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DIGRAM)
server_address = "/socket_file"
client_address = "/client_socket_file"

inputstr = input("input a name of friend who you wanna meet")
message = inputstr.encode()

sock.bind(client_address)

try:
    print("sending {}".format(message))
    sent = sock.sendto(message, server_address)
    print("waiting to receive")
    data, server = sock.recvfrom(4096)
    print("received {}".format(data))
finally:
    print("closing socket")
    sock.close()