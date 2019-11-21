import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = int(10000)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sock.bind(UDP_IP,UDP_PORT)

message = "Hello world !"

while True:
	sock.sendto(bytes(message, "utf-8"), (UDP_IP, UDP_PORT))
	time.sleep(2)

