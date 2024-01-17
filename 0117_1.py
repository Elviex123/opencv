import cv2
"""photo
img = cv2.imread('meme.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
cv2.imshow('img',img)

cv2.waitKey(0)
"""
cap = cv2.VideoCapture('video1.mp4')

while True:
    ret, frame =cap.read()
    if ret:
        cv2.imshow('video',frame)
    else:
        break
    cv2.waitKey(1)