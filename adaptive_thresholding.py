import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png', 0)
_, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
thr2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
thr3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('Image', img)
cv.imshow('Binary', thr1)
cv.imshow('Adaptive_Mean_C', thr2)
cv.imshow('Adaptive_Gaussian_C', thr3)

cv.waitKey()
cv.destroyAllWindows()