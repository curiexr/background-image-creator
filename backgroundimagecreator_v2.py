# importing the modules
import numpy as np
import cv2
from PIL import Image

# image size variable in px
imagesize = [900, 1440, 3]
# rgb value
RGB = [90, 124, 255]
  
# creating array using np.zeroes()
array = np.zeros(imagesize,
                 dtype = np.uint8)
  
# setting RGB color values as 255,255,255
array[:, :] = RGB 
  
# displaying the image
cv2.imshow("image", array)
im = Image.fromarray(array)
im.save('output.jpg')