import io
import socket
import os
import sys


s = socket.socket()
num = 0
host = socket.gethostname()
port = 12345
newpath = r'C:\Users\hajun_dg9ntlr\Desktop\result'
s.connect((host, port))

try:     #tries to make folder result, if it can't (exists) then pass
    os.makedirs(newpath)
except:
    pass

numfiles = len([t for t in os.listdir('./Picture')]) #this /Picture is dir that contains initial images

while (num <= numfiles-1):
    x= s.recv(9999999979)
    f = open("result\\newfire"+str(num)+".png", "wb")
    bytearr = bytearray(x)
    f.write(bytearr)
    num+=1




f.close

s.close
