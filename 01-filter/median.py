from PIL import Image, ImageFilter
img = Image.open("../imgs/lenna.png")
median_img = img.filter(ImageFilter.MedianFilter(7))
median_img.show()

'''
from skimage import io, color, filters
from skimage.morphology import disk
img = io.imread("../imgs/lenna.png")
img = color.rbg2gray(img)
out = filters.median(img, disk(7))
io.imshow(out)
io.show()
'''
