import cv2
import numpy as np

img = cv2.imread('lena.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
lr3 = cv2.pyrDown(lr2)

hr1 = cv2.pyrUp(img)
hr2 = cv2.pyrUp(hr1)
hr3 = cv2.pyrUp(hr2)

cv2.imshow('image', img)
cv2.imshow('LR1', lr1)
cv2.imshow('LR2', lr2)
cv2.imshow('LR3', lr3)

cv2.imshow('UR1', hr1)
cv2.imshow('UR2', hr2)
cv2.imshow('UR3', hr3)

cv2.waitKey(0)
cv2.destroyAllWindows()