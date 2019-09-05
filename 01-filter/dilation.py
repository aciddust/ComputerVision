from skimage import io
from skimage.morphology import disk, binary_dilation
img = io.imread('../imgs/train.jpg')
dilated_img = binary_dilation(img)
io.imshow(dilated_img)
io.show()

