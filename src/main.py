import imageio
import numpy as np
from Lib import *

original = imageio.imread("../img/wide_rock.jpg")


final = original.copy()

final = sorting.sort_image_rows(final)

image_to_save = final
image_to_save = image_to_save.astype(np.uint8)
imageio.imwrite("../img/output.jpg", image_to_save)
    