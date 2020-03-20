
# Esta tarefa consiste em:
# 
# 1) Assistir ao vídeo https://www.youtube.com/watch?v=waNQ-7ckw0I
# 
# 2) Desenvolver as máscaras de derivada discutidas no vídeo
# 
# 3) Implementar o detector de bordas discutido no vídeo
# 
# 3.1) Ler uma imagem em escala de cinzas (ou ler imagem colorida e transformar para escala de cinzas)
# 
# 3.2) Ampliar a imagem para que ela tenha dois pixels a mais na direção horizontal (uma coluna de pixels à esquerda da imagem e uma coluna de pixels à direita da imagem) e dois pixels a mais na direção vertical (uma linha de pixels no topo da imagem e uma linha na base da imagem). Esses pixels adicionais terão valor de intensidade iguais a zero.
# 
# 3.3) usar uma máscara de derivada (abordagem central) e aplicá-la a cada pixel da imagem ampliada que não seja um pixel de borda. O resultado da aplicação da máscara sobre um pixel é copiado no pixel correspondente de uma imagem nova.
# 
# 3.4) Exibir a imagem original e a imagem nova.

# Inicia em 19/03/2020 às 00h00 e finaliza em 02/04/2020 às 23h59


# # Lendo uma imagem colorida e transformando para escala de cinzas

import numpy as np
import matplotlib.pyplot as plt
from skimage import io

def rgb_to_gray(rgb):
    #Y' = 0.2989 R + 0.5870 G + 0.1140 B 
    return np.dot(rgb[...], [0.2989, 0.5870, 0.1140])

def convolution2d(image, kernel):
    #Kernel tem que ser quadrado.
    
    m, n = kernel.shape
    x, y = image.shape
    
    y = y - m + 1
    x = x - m + 1
    new_image = image.copy()
    for i in range(x):
        for j in range(y):
            new_image[i][j] = np.sum(np.multiply(image[i:i+m, j:j+n],kernel))
            
    return new_image


img = io.imread('/home/titowoche30/Área de Trabalho/Métodos Numéricos II/blocks.jpg')
img = img[...,:3]

img = rgb_to_gray(img)
plt.figure(figsize=(12,12))
plt.imshow(img, cmap='gray')


# # Ampliando a imagem para que ela tenha dois pixels a mais na direção horizontal (uma coluna de pixels à esquerda da imagem e uma coluna de pixels à direita da imagem) e dois pixels a mais na direção vertical (uma linha de pixels no topo da imagem e uma linha na base da imagem).


new_img = np.zeros((img.shape[0]+2,img.shape[1]+2))
new_img[1:img.shape[0]+1, 1:img.shape[1]+1] = img 

plt.figure(figsize=(12,12))
plt.imshow(new_img, cmap='gray')


# #  Desenvolvendo as máscaras de derivada

box_blur = np.array([[0,1,0],[1,0,1],[0,1,0]])
gaussian_blur = np.array([[1,2,1],[2,4,2],[1,2,1]])
sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
embossing = np.array([[1,1,0],[1,0,-1],[0,-1,-1]])

vertical_kernel = np.array([[0,0,0],[-1,0,1],[0,0,0]])
horizontal_kernel = np.array([[0,1,0],[0,0,0],[0,-1,0]])
hv_kernel = np.array([[0,1,0],[-1,0,1],[0,-1,0]])


# # Usando uma máscara(kernel) de derivada (abordagem central) e aplicando a cada pixel da imagem ampliada que não seja um pixel de borda. O resultado da aplicação da máscara sobre um pixel é copiado no pixel correspondente de uma imagem nova.

conv=convolution2d(new_img,sharpen)
plt.figure(figsize=(12,12))
plt.imshow(conv, cmap='gray')

conv=convolution2d(new_img,embossing)
plt.figure(figsize=(12,12))
plt.imshow(conv, cmap='gray')

conv=convolution2d(new_img,hv_kernel)
plt.figure(figsize=(12,12))
plt.imshow(conv, cmap='gray')

conv=convolution2d(new_img,vertical_kernel)
plt.figure(figsize=(12,12))
plt.imshow(conv, cmap='gray')

conv=convolution2d(new_img,horizontal_kernel)
plt.figure(figsize=(12,12))
plt.imshow(conv, cmap='gray')
