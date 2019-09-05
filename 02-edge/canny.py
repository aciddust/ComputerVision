from skimage import io, feature, color
img = io.imread("../imgs/lenna.png")
img = color.rgb2gray(img)
edge = feature.canny(img, 3)
io.imshow(edge)
io.show()
