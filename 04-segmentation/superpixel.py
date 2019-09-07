from skimage import segmentation, color
from skimage.io import imread
from skimage.future import graph
from matplotlib import pyplot as plt
img = imread('../imgs/lenna.png')
img_segments = segmentation.slic(img, compactness=10, n_segments=1000)
superpixels = color.label2rgb(img_segments, img, kind='avg')
fig, ax = plt.subplots()
ax.imshow(superpixels)
plt.show()
