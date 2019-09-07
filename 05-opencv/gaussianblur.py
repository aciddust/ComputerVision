import cv2
image = cv2.imread('../imgs/lenna.png')
new_image = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imwrite('gaussian_blur.jpg', new_image)
cv2.imshow('gaussian_blur', new_image)