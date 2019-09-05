from skimage import io, filters, color
img = io.imread('../imgs/lenna.png')
img = color.rgb2gray(img)
edge = filters.sobel(img)
io.imshow(edge)
io.show()
