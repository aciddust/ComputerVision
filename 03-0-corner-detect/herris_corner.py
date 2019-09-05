from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.feature import corner_harris, corner_subpix, corner_peaks

image = imread('../imgs/lenna.png')
image = rgb2gray(image)

# 이미지에서 헤리스코너 계산, 이미지의 각 픽셀의 코너 측정 응답값 반환
corners = corner_harris(image)
# 코너 응답 값을 이용해 이미지에 있는 실제 코너 계산
coords = corner_peaks(corners, min_distance=5)
# 코너가 에지 점인지 고립된 점인지 결정
coords_subpix = corner_subpix(image, coords, window_size=13)

fig, ax = plt.subplots()
ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
ax.plot(coords[:, 1], coords[:, 0], '.b', markersize=3)
ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
ax.axis((0, 220, 220, 0))
plt.show()