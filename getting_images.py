import cv2      # package

img = cv2.imread('lena.jpg', -1)

print(img)      # Returns image's pixel coordinates matrix

cv2.imshow('New Image Window', img)
k = cv2.waitKey(0)       # To make imshow() retain the output for indefinite time period

if k==27 :
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)       # Makes a copy of the image with new File Name
    cv2.destroyAllWindows()