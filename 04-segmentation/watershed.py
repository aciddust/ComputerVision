from scipy import ndimage as ndi
from skimage.morphology import watershed, disk
from skimage import data
from skimage.io import imread
from skimage.filters import rank
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte
import matplotlib.pyplot as plt

img = data.astronaut()
img_gray = rgb2gray(img)
image = img_as_ubyte(img_gray)

# 이미지에서 지역 그래디언트 계산 후 20보다 작은 점들만 선택
markers = rank.gradient(image, disk(5)) < 20
markers = ndi.label(markers)[0]
gradient = rank.gradient(image, disk(2))

# Watershed
labels = watershed(gradient, markers)

fig, ax = plt.subplots()
ax.imshow(labels, interpolation='nearest')
plt.show()