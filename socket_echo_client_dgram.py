#socket_echo_client_dgram.py
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
sock.bind(server_address)

while True:
	data, server = sock.recvfrom(10000)
	print('received {!r}'.format(data))
	
		
