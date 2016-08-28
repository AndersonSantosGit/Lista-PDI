import math

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../imagens/img_test.bmp', 0)

fourier = np.fft.fft2(img)
fourier_shifted = np.fft.fftshift(fourier)

magnitude_spectrum = 20*np.log(np.abs(fourier_shifted))

h, w = fourier_shifted.shape[0:2]
filt = np.zeros((h, w))

# wc = math.pi/8
# wc = math.pi/4
wc = 3*math.pi/8

wcpixel = wc*(1/math.pi)*(np.floor(h/2))  # idealmente h = w

n = 2

for i in range(h):
    for j in range(w):
        dist = ((i-(np.floor(h/2)))**2 + (j-(np.floor(w/2)))**2)**.5  # distancia ao centro da imagem
        filt[i, j] = 1-(1/(1+(dist/wcpixel)**(2*n)))  # Filtro Butterworth Passa-Alta

result = np.multiply(fourier_shifted, filt)

result_non_shifted = np.fft.ifftshift(result)
filtered_img = np.fft.ifft2(result_non_shifted)
filtered_img = np.abs(filtered_img)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Imagem orginal'), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(filt, cmap='gray')
plt.title('Filtro'), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(filtered_img, cmap='gray')
plt.title('Imagem filtrada'), plt.xticks([]), plt.yticks([])

plt.show()
