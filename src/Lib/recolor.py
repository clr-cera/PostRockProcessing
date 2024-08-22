import numpy as np

def grayscale(img):
    grayscale_img = np.ndarray(img.shape,dtype='float')

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            grayscale_img[i][j][0] = grayscale_img[i][j][1] = grayscale_img[i][j][2] =0.299 * img[i][j][0] + 0.587 * img[i][j][1] + 0.114 * img[i][j][2] 
    
    return grayscale_img