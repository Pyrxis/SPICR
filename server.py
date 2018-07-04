#basic folder/img information:

#Original images are in Desktop/Pictures
#Cloned images will be saved in Desktop/result
#10 images in /Pictures numbered fire1.png ~ fire10.png
#10 images will be in /result numbered newfire0.png ~ newfire9.png

#what needs to be fixed

#currently, it creates a "result" folder with 10 images labled "newfire0" ~ "newfire9", however,
#only newfire0 is "loaded" meaning it is the only openable img that is cloned from the first picture
#in the original /Pictures folder. The others are just image files without any data


import io
import socket               
import os
import sys


num=1
done = False
s = socket.socket()
a = b""
host = socket.gethostname()
port = 12345
s.bind((host, port))


def imagetobyte(imagename):     #This func takes in original img and returns bytearray of it
   with open(imagename, "rb") as imageFile:
      f = imageFile.read()
      b = bytearray(f)
      return b



s.listen(5)                

while True:
   c, addr= s.accept()

   
   
   print ('Got connection from', addr)
   numfiles = len([t for t in os.listdir('./Picture')]) #this /Picture is dir that contains initial images

   while(num<=numfiles):
      a = b"" + (imagetobyte('.\\Picture\\fire'+str(num)+'.png'))
      num+=1
      
   c.send(bytes(a)) # if i put this line inside the while loop, none of the images get loaded. 
      
   
   c.close()
