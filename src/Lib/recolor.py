import numpy as np

def luminance(pixel):
    return (0.2126*pixel[0] + 0.7152*pixel[1] + 0.0722*pixel[2])

def grayscale(img):
    grayscale_img = np.ndarray(img.shape,dtype='float')

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            grayscale_img[i][j][0] = grayscale_img[i][j][1] = grayscale_img[i][j][2] =0.299 * img[i][j][0] + 0.587 * img[i][j][1] + 0.114 * img[i][j][2] 
    
    return grayscale_img

def b_w_binary(img):
    b_w_img = np.ndarray(img.shape,dtype='float')

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if luminance(img[i][j]) > 128:
                b_w_img[i][j] = (255,255,255)
            else:
                b_w_img[i][j] = (0,0,0)
    return b_w_img


def luminance_matrix(img):
    l_matrix = np.ndarray((img.shape[0],img.shape[1]),dtype ='float')

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            l_matrix[i][j] = luminance(img[i][j])

    return l_matrix