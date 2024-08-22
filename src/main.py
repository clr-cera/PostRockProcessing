import imageio
import numpy as np
from Lib import *

original = imageio.imread("../img/wide_rock.jpg")


final = original.copy()
final = rescale.increase_pixels(final,2**2)
final = dithering.strange_dither(final,2)
final = recolor.grayscale(final)

image_to_save = final
image_to_save = image_to_save.astype(np.uint8)
imageio.imwrite("../img/output.jpg", image_to_save)
    