import cv2
img = cv2.imread('meme.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
import numpy as np
kernel = np.ones((10,10),np.uint8)
kernel1 = np.ones((10,10),np.uint8)
#彩色->灰階
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#高斯模糊
blur = cv2.GaussianBlur(img,(7,7),5)
#圖片邊緣
canny = cv2.Canny(img,150,200)
#圖片邊緣->加粗
dilate = cv2.dilate(canny,kernel,iterations=2)
#圖片邊緣加粗->輕實
erode = cv2.erode(dilate,kernel1,iterations=2)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dileate',dilate)
cv2.imshow('erode',erode)
cv2.waitKey(0)