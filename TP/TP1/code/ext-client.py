#!/usr/bin/python3
import socket
import sys

BUFSIZE = 1024
def client (host, donnee, port ):
    sock = socket.socket(type=socket.SOCK_DGRAM )
    addr = (host , port)
    if (donnee=="user"):
        sock.sendto(b"user", addr)
    else:
        sock.sendto(b"date", addr)
    data = sock.recv( BUFSIZE )
    print (data.decode(), end="")

client(sys.argv[1],sys.argv[2], 5555)
