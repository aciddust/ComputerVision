import cv2
image = cv2.imread('../imgs/lenna.png')
new_image = cv2.medianBlur(image, 7)
cv2.imwrite('median_blur.jpg', new_image)
cv2.imshow('median_blur', new_image)