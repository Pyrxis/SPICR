#!/usr/bin/python           # This is client.py file
import io
import socket               # Import socket module
import sys
s = socket.socket()         # Create a socket object
num = 1
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
#fh = open("imageToSave.png", "wb")
#fh.write(s.recv(400000000).decode('utf-8'))
#fh.close()


x= s.recv(40000000000)
name = "newfire"+str(num)+".png"
f = open("newfire1.png", "wb")
f.write(bytearray(x))
f.close

s.close                     # Close the socket when done
