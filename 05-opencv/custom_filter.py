import cv2
import numpy as np
image = cv2.imread("../imgs/lenna.png")
kernel = np.array([[1,1,1],
                    [1,1,1],
                    [1,1,1]])

new_image = cv2.filter2D(image, -1, kernel)
cv2.imwrite("filter.jpg", new_image)
cv2.imshow("filter", new_image)