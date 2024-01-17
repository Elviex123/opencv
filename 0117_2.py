import cv2
import numpy as np
import random
img = cv2.imread('meme.jpg')
#print(type(img.shape))

#img = np.empty((300,300,3),np.uint8)
#for row in range(300):
#    for col in range(img.shape[1]):
#        img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
new_Img=img[:150, 200:400]
cv2.imshow('img',img)
cv2.imshow('new_Img',new_Img)
cv2.waitKey(0)