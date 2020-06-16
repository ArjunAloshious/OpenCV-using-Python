import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')
cv.imshow("img", img)
plt.hist(img.ravel(), 256, [0,256])         # displays a plot of an image's pixel intensity
plt.show()

b, g, r = cv.split(img)                         # splits the image into 3 different channels
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)
plt.hist(b.ravel(), 256, [0,256])               # creates a histogram for blue pixels intensity
plt.hist(g.ravel(), 256, [0,256])               # creates a histogram for green pixels intensity
plt.hist(r.ravel(), 256, [0,256])               # creates a histogram for red pixels intensity
plt.show()

img = cv.imread('lena.jpg', 0)                  # load image in grayscale
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()