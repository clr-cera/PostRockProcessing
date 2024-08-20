import numpy as np

def luminance(pixel):
    return (0.2126*pixel[0] + 0.7152*pixel[1] + 0.0722*pixel[2])

def sort_image_rows(img):
    sorted_img = np.ndarray(img.shape,dtype='uint')
    for i in range(img.shape[0]):
        sorted_img[i] = sorted(img[i], key=luminance)
            
    
    return sorted_img

