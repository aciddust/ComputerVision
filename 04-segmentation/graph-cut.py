import matplotlib.pyplot as plt
import skimage.color as color
import skimage.data as data
import skimage.future.graph as graph
import skimage.io as io
from skimage.io import imread
import skimage.segmentation as segmentation

#img = data.astronaut()
img = imread('../imgs/mushroom.jpg')
segment_img = segmentation.slic(img, compactness = 30, n_segments = 200)
segment_graph = graph.rag_mean_color(img, segment_img, mode = "similarity")
img_cuts = graph.cut_normalized(segment_img, segment_graph)
output = color.label2rgb(img_cuts, img, kind = "avg")
fig, ax = plt.subplots(nrows = 1, ncols = 2)
ax[0].imshow(img)
ax[1].imshow(output)

plt.tight_layout()
plt.show()



