from skimage import measure
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import sobel
import matplotlib.pyplot as plt

# 이미지 읽기
img = imread('../imgs/lenna.png')
# 그레이스케일 변환
img_gray = rgb2gray(img)
# 이미지에서 에지 찾음
img_edges = sobel(img_gray)
# 이미지에서 윤곽선 검출
contours = measure.find_contours(img_edges, 0.2)

# 찾은 이미지에서 윤곽선 표시
fig, ax = plt.subplots()
ax.imshow(img_edges, interpolation='nearest', cmap=plt.cm.gray)
for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

