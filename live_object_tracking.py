import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Tracking")
cv2.createTrackbar("LowerHue", "Tracking",0 ,255 , nothing)
cv2.createTrackbar("LowerSat", "Tracking",0 ,255 , nothing)
cv2.createTrackbar("LowerVal", "Tracking",0 ,255 , nothing)
cv2.createTrackbar("UpperHue", "Tracking",255 ,255 , nothing)
cv2.createTrackbar("UpperSat", "Tracking",255 ,255 , nothing)
cv2.createTrackbar("UpperVal", "Tracking",255 ,255 , nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LowerHue", "Tracking")
    l_s = cv2.getTrackbarPos("LowerSat", "Tracking")
    l_v = cv2.getTrackbarPos("LowerVal", "Tracking")
    u_h = cv2.getTrackbarPos("UpperHue", "Tracking")
    u_s = cv2.getTrackbarPos("UpperSat", "Tracking")
    u_v = cv2.getTrackbarPos("UpperVal", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27 :
        break

cap.release()
cv2.destroyAllWindows()