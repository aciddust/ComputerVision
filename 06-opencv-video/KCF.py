import cv2

tracker = cv2.TrackerKCF_create()
cam = cv2.VideoCapture(0)
for i in range(5):
    ret, frame = cam.read()
obj = cv2.selectROI("Tracking", frame)
ok = tracker.init(frame, obj)

while True:
    ret, frame = cam.read()
    upd, obj = tracker.update(frame)
    if upd:
        x1 = (int(obj[0]), int(obj[1]))
        x2 = (int(obj[0] + obj[2]), int(obj[1] + obj[3]))
        cv2.rectangle(frame, x1, x2, (255, 0, 0))
    cv2.imshow("Track object", frame)
    if (cv2.waitKey(1) & 0xFF) == 27:
        break

cam.release()
cv2.destroyAllWindows()


    