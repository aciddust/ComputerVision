import cv2
img = cv2.imread('../imgs/lenna.png')
img_temp = cv2.imread('../imgs/lenna_face.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_temp = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)

w, h = gray_temp.shape[::-1]
output = cv2.matchTemplate(gray, gray_temp, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(output)
top = max_loc
bottom = (top[0] + w, top[1] + h)
cv2.rectangle(img, top, bottom, 255, 2)
cv2.imshow('image', img)
cv2.imwrite('img.jpg', img)