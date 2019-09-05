from skimage.transform import rotate
from skimage.feature import local_binary_pattern
from skimage import data
from skimage.color import label2rgb
import numpy as np

# 비교를 위한 각각 다른 이미지 로드 
image = list()
tmp = list()
tmp.append(data.load('rough-wall.png'))
tmp.append(data.load('grass.png'))
tmp.append(data.load('brick.png'))

def next_step():
    global tmp 
    global image
    image.append(tmp)
    tmp = list()

next_step()
# image 0 >> frog, lenna, brick

for img in image[0]:
    tmp.append(local_binary_pattern(img, 16, 2, 'uniform'))
next_step()
# image 1 >> lbp_frog, lbp_lenna, lbp_brick

for img in image[0]:
    tmp.append(rotate(img, angle=22, resize=False))
next_step()
# image 2 >> rot_frog, rot_lenna, rot_brick

for img in image[2]:
    tmp.append(local_binary_pattern(img, 16, 2, 'uniform'))
next_step()
# image 3 >> rot_lbp_frog, rot_lbp_lenna, rot_lbp_brick


bins_num = int(image[1][2].max() + 1)
brick_hist, _ = np.histogram(image[1][2],
                                normed=True,
                                bins=bins_num,
                                range=(0, bins_num))
lbp_features = image[3]
min_score = 1000
winner = 0
idx = 0
for feature in lbp_features:
    historgram, _ = np.histogram(feature,
                                    normed=True,
                                    bins=bins_num,
                                    range=(0, bins_num))

    p = np.asarray(brick_hist)
    q = np.asarray(historgram)
    filter_idx = np.logical_and(p != 0, q != 0)
    score = np.sum(p[filter_idx] * np.log2(p[filter_idx] / q[filter_idx]))
    if score < min_score:
        min_score = score
        winner = idx
    idx += 1

if winner == 0:
    print ('Brick matched with rotated Rough-wall')
elif winner == 1:
    print ('Brick matched with rotated Grass')
elif winner == 2:
    print ('Brick matched with rotated Brick')
else:
    print ('Something goes wrong.')
    

    

