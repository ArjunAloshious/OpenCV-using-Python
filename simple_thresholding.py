import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)
_, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, thr2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, thr3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, thr4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, thr5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow('Image', img)
cv.imshow('Binary', thr1)
cv.imshow('Binary_Inv', thr2)
cv.imshow('Trunc', thr3)
cv.imshow('To_Zero', thr4)
cv.imshow('To_Zero_Inv', thr5)

cv.waitKey()
cv.destroyAllWindows()