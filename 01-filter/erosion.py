from skimage import morphology, io
img = io.imread('../imgs/train.jpg')
eroded_img = morphology.binary_erosion(img)
io.imshow(eroded_img)
io.show()
