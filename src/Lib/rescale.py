import numpy as np

def downscale(img, scale):
    shape = img.shape
    downscale_shape = shape[0]//scale, shape[1]//scale, shape[2]

    downscale_img = np.ndarray(downscale_shape,dtype='uint')
    for i in range(downscale_shape[0]):
        for j in range(downscale_shape[1]):
            downscale_img[i][j] = img[i*scale][j*scale]

    return downscale_img

def upscale(img, scale):
    shape = img.shape
    upscale_shape = shape[0]*scale, shape[1]*scale, shape[2]
    
    upscale_img = np.ndarray(upscale_shape,dtype='uint')
    for i in range(upscale_shape[0]):
        for j in range(upscale_shape[1]):
            x = min(i//scale, shape[0]-1)
            y = min(j//scale, shape[1]-1)
            upscale_img[i][j] = img[x][y]
    
    return upscale_img

def increase_pixels(img, scale):
    downscale_image = downscale(img, scale)
    final_image = upscale(downscale_image, scale)

    return final_image