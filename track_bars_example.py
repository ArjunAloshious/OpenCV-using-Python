import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

cv.namedWindow('image')
cv.createTrackbar('CurrPos', 'image', 10, 400, nothing)
switch = 'Color/Gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(True):
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('CurrPos', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 4, (255,255,255))
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.imshow('image', img)


cv.destroyAllWindows()