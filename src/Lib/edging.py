import numpy as np
from Lib import recolor
from scipy.signal import convolve

def paint_edge(img):
    l_matrix = recolor.luminance_matrix(img)

    gx = np.array((
        (-1,-1,-1),
        (0,0,0),
        (1,1,1),
        ))

    gy = np.array((
        (-1,0,1),
        (-1,0,1),
        (-1,0,1),
        ))

    dx_img = convolve(2*gx, l_matrix)
    dy_img = convolve(2*gy, l_matrix) 

    grad_img  = np.ndarray((img.shape[0],img.shape[1]), dtype='float')
    for i in range(grad_img.shape[0]):
        for j in range(grad_img.shape[1]):
            grad_img[i][j] = (abs(dx_img[i][j]) + abs(dy_img[i][j])) / 2

    edge_final = np.ndarray(img.shape, dtype='float')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            edge_final[i][j] = np.array([1,1,1]) * grad_img[i][j]
    

    return edge_final