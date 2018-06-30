#!/usr/bin/python           # This is server.py file
import io
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
def imagenamechanger(imagename):
   return imagename
def imagetobytes(imagename):
   with open(imagename, "rb") as imageFile:
      f = imageFile.read()
      b = bytearray(f)
      return b

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send(bytes(imagetobytes("fire.png")))



   c.close()                # Close the connection
