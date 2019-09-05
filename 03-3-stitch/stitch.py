from skimage.feature import ORB, match_descriptors
from skimage.io import imread
from skimage.measure import ransac
from skimage.transform import ProjectiveTransform
from skimage.color import rgb2gray
from skimage.io import imsave, show
from skimage.color import gray2rgb
from skimage.exposure import rescale_intensity
from skimage.transform import warp
from skimage.transform import SimilarityTransform
import numpy as np

img0 = rgb2gray(imread('../imgs/mushroom-left.jpg'))
img1 = rgb2gray(imread('../imgs/mushroom-right.jpg'))

orb = ORB(n_keypoints=1000, fast_threshold=0.05)
orb.detect_and_extract(img0)
key1 = orb.keypoints
dsc1 = orb.descriptors
orb.detect_and_extract(img1)
key2 = orb.keypoints
dsc2 = orb.descriptors

matches = match_descriptors(dsc1, dsc2, cross_check=True)
src = key2[matches[:, 1]][:, ::-1]
dst = key1[matches[:, 0]][:, ::-1]
transform_model, inliers = ransac((src, dst), ProjectiveTransform, min_samples=4, residual_threshold=2)
r, c = img1.shape[:2]
corners = np.array([[0,0], [0,r], [c,0], [c,r]])
warped_corners = transform_model(corners)
all_corners = np.vstack((warped_corners, corners))
corner_min = np.min(all_corners, axis=0)
corner_max = np.max(all_corners, axis=0)

output_shape = (corner_max-corner_min)
output_shape = np.ceil(output_shape[::1])
offset = SimilarityTransform(translation = -corner_min)
img0_warp = warp(img0, offset.inverse, output_shape=output_shape, cval=-1)
img1_warp = warp(img1, (transform_model + offset).inverse, output_shape=output_shape, cval=-1)

img0_mask = (img0_warp != -1)
img0_warp[~img0_mask] = 0
img0_alpha = np.dstack((gray2rgb(img0_warp), img0_mask))
img1_mask = (img1_warp != -1)
img1_warp[~img1_mask] = 0
img1_alpha = np.dstack((gray2rgb(img1_warp), img1_mask))

merged = (img0_alpha + img1_alpha)
alpha = merged[..., 3]
merged /= np.maximum(alpha, 1)[..., np.newaxis]
imsave('output.png', merged)
