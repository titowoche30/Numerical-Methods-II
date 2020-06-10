import sys
import platform
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def derivate(a, b):
    return (b-a)/2

def rgb_to_gray(rgb):
    #Y' = 0.2989 R + 0.5870 G + 0.1140 B 
    return np.dot(rgb[...], [0.2989, 0.5870, 0.1140])

def edges_X(image):
    x, y = image.shape
    new_image = image.copy()
    
    for i in range(x-1):
        for j in range(y-1):
            new_image[i][j] = abs(derivate(image[i][j-1], image[i][j+1]))
            
    return new_image

def edges_Y(image):
    x, y = image.shape
    new_image = image.copy()
    
    for i in range(x-1):
        for j in range(y-1):
            new_image[i][j] = abs(derivate(image[i-1][j], image[i+1][j]))
            
    return new_image

def edges_XY(image):
    x, y = image.shape
    new_image = image.copy()
    
    for i in range(x-1):
        for j in range(y-1):
            new_image[i][j] = abs(derivate(image[i-1][j], image[i+1][j]) + derivate(image[i][j-1], image[i][j+1]))
            
    return new_image

def read_image(img_name):
    img = io.imread(img_name)
    
    plt.figure(figsize=(12,12))
    plt.title('Original Image',size='xx-large')
    plt.imshow(img)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    img = img[...,:3]
    img = rgb_to_gray(img)
    
    return img
    
def expand_image(img):
    new_img = np.zeros((img.shape[0]+2,img.shape[1]+2))
    new_img[1:img.shape[0]+1, 1:img.shape[1]+1] = img 
    
    return new_img

def plot(f,img,img_name):
    conv=f(img)
    
    plt.figure(figsize=(12,12))
    plt.title(f.__name__,size='xx-large')
    plt.imshow(conv, cmap='gray')
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.savefig(img_name.split('.')[0] + '_edges.png',cmap='gray')
    plt.show()


if __name__ == '__main__':
    if platform.system() == 'Linux':
        img_name=sys.argv[1]
    else:
        img_name=str(input('Enter the name of a image with its format'))
        
    f = edges_XY
    #f=edges_Y
    #f=edges_X

    img = read_image(img_name)
    new_img = expand_image(img)
    plot(f,new_img,img_name)
