from PIL import Image
from PIL import ImageFilter
img = Image.open("../imgs/lenna.png").convert("L")
my_kernel = ImageFilter.Kernel((3,3), [1,2,3,4,5,6,7,8,9])
new_img = img.filter(my_kernel)
new_img.show()

