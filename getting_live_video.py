import cv2

cap = cv2.VideoCapture(0)                       # device index of camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')        # 4-byte code specifying the video codec
out = cv2.VideoWriter('output.avi', fourcc, 24.0, (640,480))

while(cap.isOpened()):                             # if the video file mentioned exists and is opened
    ret, frame = cap.read()
    if ret == True :
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))       # Displays each frame's width
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))      # Displays each frame's height

        out.write(frame)                               # Write to file

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # Converts each frame in BGR to a grayscaled image
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):           # This mask is used to return 64 bit values for the system
            break
    else:
        break

cap.release()           # release resources
out.release()
cv2.destroyAllWindows()