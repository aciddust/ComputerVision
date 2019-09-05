from PIL import Image, ImageFilter
img = Image.open("../imgs/lenna.png")
blur_img = img.filter(ImageFilter.GaussianBlur(4))
blur_img.show()

'''
from skimage import io, filters
img = io.imread("../imgs/lenna.png")
out = filters.gaussian(img, sigma=4)
io.imshow(out)
io.show()
'''
