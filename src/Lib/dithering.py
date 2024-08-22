import numpy as np
from math import floor

def strange_dither(img, color_number, spread=0):
    bayer8 = np.ndarray((8,8))

    bayer8[0] = [0, 32, 8, 40, 2, 34, 10, 42]
    bayer8[1] = [48, 16, 56, 24, 50, 18, 58, 26]
    bayer8[2] = [12, 44, 4, 36, 14, 46, 6, 38]
    bayer8[3] = [60, 28, 52, 20, 62, 30, 54, 22]
    bayer8[4] = [3, 35, 11, 43, 1, 33, 9, 41]
    bayer8[5] = [51, 19, 59, 27, 49, 17, 57, 25]
    bayer8[6] = [15, 47, 7, 39, 13, 45, 5, 37]
    bayer8[7] = [63,31, 55, 23, 61, 29, 53, 21]

    dithered_img = np.ndarray(img.shape,dtype='float')

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x = i % 8
            y = j % 8
            
            M = bayer8[x][y]
            M = (M / (8**2)) - 0.5
            
            pattern_px = img[i][j]/255 + spread* M

            color = (
                floor(pattern_px[0] * (color_number - 1) + 0.5) / (color_number-1),
                floor(pattern_px[1] * (color_number - 1) + 0.5) / (color_number-1),
                floor(pattern_px[2] * (color_number - 1) + 0.5) / (color_number-1),
            )

            dithered_img[i][j] = color

    return 255*dithered_img.astype(np.uint)
