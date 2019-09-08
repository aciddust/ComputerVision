import cv2
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
h, w = frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video_write = cv2.VideoWriter('saved.avi', fourcc, 25.0, (w,h))
while(cam.isOpened()):
    ret, frame = cam.read()
    # grayscale 영상을 원한다면
    # cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    video_write.write(frame)
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
video_write.release()
cv2.destroyAllWindows()