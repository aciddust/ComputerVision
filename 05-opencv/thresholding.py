import cv2
image = cv2.imread("../imgs/lenna.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
new_image = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
cv2.imwrite("thresholding.jpg", new_image[1])
cv2.imshow("thresholding", new_image[1])