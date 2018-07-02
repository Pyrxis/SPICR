import cv2
import numpy as mp

def ftest( img_url ):
  img = cv2.imread(img_url)
  error_pixel_detected = 0
  h, w, channels = img.shape
  
  threshold = int((h * w) / 10)
  
  blr, bhr = [1, 100]
  glr, ghr = [-1, 100]
  rlr, rhr = [120, 260]
  
  for x in range(1, w):
    for y in range(1, h):
      red, green, blue = img[x, y]
      
      if blr <= blue <= bhr:
        if glr <= green <= ghr:
          if rlr <= red <= rhr:
            error_pixel_detected += 1
            
  if error_pixel_detected > threshold:
    return True
  else:
    return False
