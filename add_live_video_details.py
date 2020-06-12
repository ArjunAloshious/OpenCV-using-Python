import cv2
import datetime

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text1 = 'Width : ' + str(cap.get(3))
        text2 = 'Height : ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (780, 700), font, 1, (255,255,255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, text1, (20, 650), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, text2, (20, 700), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()           # release resources
cv2.destroyAllWindows()