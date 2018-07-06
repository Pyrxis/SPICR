import io
import socket,pickle
import os
import sys
from tkinter import *


s = socket.socket()

host = socket.gethostname()
port = 12345
newpath = r'C:\Users\hajun_dg9ntlr\Desktop\resultimg'
newpath2 = r'C:\Users\hajun_dg9ntlr\Desktop\resultimg\safe'
newpath3 = r'C:\Users\hajun_dg9ntlr\Desktop\resultimg\problem'
s.connect((host, port))


try:     #tries to make folder result, if it can't (exists) then pass
    os.makedirs(newpath)
except:
    pass
try:     
    os.makedirs(newpath2)
except:
    pass
try:     
    os.makedirs(newpath3)
except:
    pass


bytearr = b''
datax = s.recv(16777216)
dataofimg = pickle.loads(datax)
num = 2
for i in dataofimg[0]:
    f = open("resultimg\\safe\\panel"+str(i)+".png", "wb")
    bytearr = bytearray(dataofimg[num])
    f.write(bytearr)
    num+=1
for i in dataofimg[1]:
    f = open("resultimg\\problem\\panel"+str(i)+".png", "wb")
    bytearr = bytearray(dataofimg[num])
    f.write(bytearr)
    num+=1

f.close

root = Tk()

button = Button(root, text="hi", bg = "blue", width=5)

button.pack()

root.mainloop()

s.close
