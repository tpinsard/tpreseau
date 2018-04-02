#!/usr/bin/python3

import socket
import datetime

BUFSIZE = 1024
def server (port ):
    sock = socket.socket (type= socket.SOCK_DGRAM )
    sock.bind(("0.0.0.0", port ))
    while True:
        data , addr = sock.recvfrom ( BUFSIZE )
        data = datetime.datetime.now ()
        data = "%s\n" % data
        sock. sendto (data.encode (), addr)
        
server(5555)
        
