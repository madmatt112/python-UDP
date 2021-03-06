#!/bin/python

import socket, sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = str(" ".join(sys.argv[1:]))

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, #Internet
                     socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
