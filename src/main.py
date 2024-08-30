import imageio.v3 as imageio
import numpy as np
from Lib import *

original = imageio.imread("../img/hand_small.jpg")


final = original.copy()
final = rescale.increase_pixels(final, 2**4)
edge = edging.paint_edge(final)
edge = recolor.b_w_binary(2*edge)
final = (0.7*final + 0.3*edge)

image_to_save = final
image_to_save = image_to_save.astype(np.uint8)
imageio.imwrite("../img/output.jpg", image_to_save)