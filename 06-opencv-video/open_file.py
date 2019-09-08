import cv2
cam = cv2.VideoCapture("sample.mp4")
# 비디오를 어느 프레임부터 읽어올지 (시작지점)
cam.set(cv2.CAP_PROP_POS_FRAMES, 300) # 시작지점이 300임.

while(cam.isOpened()):
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()