import sys
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

# 코너 검출기 파라미터
feature_params = dict(maxCorners = 1000,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize = 5,
                      useHarrisDetector=1,
                      k=0.04)

# LK optical flow의 params
lk_params = dict(winSize=(15,15), maxLevel=2)

# 임의 색 생성
color = np.random.randint(0,255,(1000,3))

# 첫 프레임 읽고 코너 찾기
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# 화면 표시를 위한mask 생성
mask = np.zeros_like(old_frame)
# 프레임 카운트
count = 0 

while(cap.isOpened()):
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Optical flow 계산
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # 좋은 특징점 선택
    good_new = p1[st==1]
    good_old = p0[st==1]

    
    # 추적 내용 표시
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b), (c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame, (a,b), 5, color[i].tolist(), -1)

    img = cv2.add(frame, mask)
    cv2.imshow('frame', img)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

    old_gray = frame_gray.copy()
    count += 1
    if count % 100 == 0:
        p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
    else:
        p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()

