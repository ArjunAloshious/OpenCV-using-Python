import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', 0)
_, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, thr2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, thr3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, thr4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, thr5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Image', 'Binary', 'Binary_Inv', 'Trunc', 'To_Zero', 'To_Zero_Inv']
images = [img, thr1, thr2, thr3, thr4, thr5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()                      # Displays multiple images in the same window
cv.waitKey()
cv.destroyAllWindows()