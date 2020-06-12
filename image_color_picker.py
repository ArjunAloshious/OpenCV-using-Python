import cv2
import numpy as np

def click_event(event, x, y, flags, par):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        myImage = np.zeros((512,512,3), np.uint8)       # initially the new window must be black
        myImage[:] = [blue,green,red]             # this stores the BGR values of clicked pixel to myImage
        cv2.imshow('color', myImage)        # opens a new window with the chosen color

img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()