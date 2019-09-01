#!/usr/bin/python3

from PIL import Image, ImageEnhance

img_dict = dict()

img = Image.open("../imgs/lenna.png")
img_dict['original_img'] = img

gray = img.convert("L")
img_dict['grayscale'] = gray

dim = (100, 100, 150, 165)
crop_img = img.crop(dim)
img_dict['crop'] = crop_img

resize = img.resize((200, 200))
img_dict['resize'] = resize

rotate = img.rotate(90)
img_dict['rotate'] = rotate

# using Enhance module
bright = ImageEnhance.Brightness(img).enhance(2)
img_dict['bright'] = bright

contrast = ImageEnhance.Contrast(img).enhance(2)
img_dict['contrast'] = contrast


for k, v in img_dict.items():
  v.show()
  v.save(k+'.png')

