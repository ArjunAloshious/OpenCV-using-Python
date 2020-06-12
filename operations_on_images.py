import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)                        # returns tuple of number of rows, columns and channels
print(img.size)                         # returns total number of pixels accessed
print(img.dtype)                        # returns image's datatype
b,g,r = cv2.split(img)                  # splits the image into its bgr channels
img = cv2.merge((b,g,r))                # merges the bgr channels and forms the image again

ball = img[280:340, 330:390]            # region of interest
img[273:333, 100:160] = ball            # forming a copy on a different region within image

img = cv2.resize(img, (512,512))        # to avoid size mismatch error of 2 images
img2 = cv2.resize(img2, (512,512))

dest = cv2.addWeighted(img, .9, img2, .1, 0)         # modifies visibility of 2 images when superimposed

cv2.imshow('image',dest)
cv2.waitKey(0)
cv2.destroyAllWindows()