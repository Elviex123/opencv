import cv2
img = cv2.imread('meme.jpg')
img = cv2.resize(img,(300,300))
cv2.imshow('img',img)

cv2.waitKey(0)