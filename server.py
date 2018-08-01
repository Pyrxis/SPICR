
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
import socket,pickle
import os
import sys
import re
import signal

def handler(signum,frame): #for detecting when 1 minute has passed
    print("TIMES UP!!!! 2 MINUTE ALREADY PASSED! exiting now....")
    s.close()
    sys.exit()
    
done = False
s = socket.socket()

host = socket.gethostname()
port = 12345
s.bind(('', port))


def imagetobyte(imagename):     #This func takes in original img and returns bytearray of it
   with open(imagename, "rb") as imageFilex:
      f = imageFilex.read()
      b = bytearray(f)
      return b



s.listen(5)                
signal.signal(signal.SIGALRM,handler)
signal.alarm(60)
while True:
   c, addr= s.accept() 
   print ('Got connection from', addr)

   file_no_safe = []
   file_no_problem = []
   regex = re.compile(r'\d+')

   for t in os.listdir('./result/safe'):
      x = int(regex.findall(t)[0])
      file_no_safe.append(x)
   for t in os.listdir('./result/problem'):
      x = int(regex.findall(t)[0])
      file_no_problem.append(x)


   
   a = []
   a.append(file_no_safe)
   a.append(file_no_problem)
   for i in file_no_safe:
      if(os.path.isfile('./result/safe/panel'+str(i)+'.jpg')):
 
         a.append( b"" + (imagetobyte('./result/safe/panel'+str(i)+'.jpg')))
      else:
         pass
   for i in file_no_problem:
      if(os.path.isfile('./result/problem/panel'+str(i)+'.jpg')):
         a.append( b"" + (imagetobyte('./result/problem/panel'+str(i)+'.jpg')))
      else:
         pass

   print(type(a))
   print(len(a))
   c.sendall(pickle.dumps(a))
   
   
   c.close()


