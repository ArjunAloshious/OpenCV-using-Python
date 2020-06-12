import cv2
import numpy as np

img = cv2.imread('lena.jpg', 1)

img = cv2.line(img, (0,0), (255,255), (0, 255, 255), 3)
img = cv2.arrowedLine(img, (0,255), (255,255), (255, 255, 0), 3)
img = cv2.rectangle(img, (384,0), (510,128), (255,100,100), -1)
img = cv2.circle(img, (447,63), 63, (100, 0, 255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (30,480), font, 4, (255,255,255),5,cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()