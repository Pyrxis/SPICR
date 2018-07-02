#!/usr/bin/python
import cv2
import numpy as mp
import shutil
import os 

def ftest( img_url ):
  base = cv2.imread(img_url)
  img = cv2.resize(base, (410, 308))
  
  error_pixel_detected = 0
  h, w, channels = img.shape
  
  #threshold = int((h * w) / 15)
  threshold = 30
  
  blr, bhr = [1, 150]
  glr, ghr = [1, 150]
  rlr, rhr = [150, 255]
  
  for x in range(0, w-1):
    for y in range(0, h-1):
      red, green, blue = img[y, x]
      
      if blr <= blue <= bhr:
        if glr <= green <= ghr:
          if rlr <= red <= rhr:
            error_pixel_detected += 1
       
  if error_pixel_detected > threshold:
    return True
  else:
    return False

shutil.rmtree('/home/pi/Desktop/result/safe')
shutil.rmtree('/home/pi/Desktop/result/problem')
newpath = r'/home/pi/Desktop/result/safe'
newpath2 = r'/home/pi/Desktop/result/problem'
os.makedirs(newpath)
os.makedirs(newpath2)              
numb_of_images = 16
def_image_location = '/home/pi/Desktop/images/panel'
safe_location = '/home/pi/Desktop/result/safe/panel'
problem_location = '/home/pi/Desktop/result/problem/panel'
for x in range(0,numb_of_images):
    if ftest(def_image_location+str(x)+'.jpg'):
        cv2.imwrite(problem_location+str(x)+'.jpg',cv2.imread(def_image_location+str(x)+'.jpg'))
    else:
        cv2.imwrite(safe_location+str(x)+'.jpg',cv2.imread(def_image_location+str(x)+'.jpg'))
