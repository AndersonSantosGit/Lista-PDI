#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy.ndimage.filters as filters

img = cv2.imread('../imagens/old_man.jpg', 0)
# img = cv2.imread('../imagens/plane.jpg', 0)
# img = cv2.imread('../imagens/monkey.jpg', 0)

o = 2
gray = filters.gaussian_filter(img, o)

dy, dx = np.gradient(np.double(gray))

gx = np.power(dx, 2.0)
gy = np.power(dy, 2.0)
M = np.sqrt((gx + gy))  # Magnitude do gradiente

direcao = np.divide(1, np.tan(np.divide(gy, gx)))
direcao = np.arctan(np.divide(gy, gx))

plt.imshow(gray, cmap='gray')
plt.title('Original Image')
plt.show()

plt.imshow(M, cmap='gray')
plt.title('Original Image')
plt.show()

t_baixo = 150
t_alto = 200

edges = cv2.Canny(img, t_baixo, t_alto)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Bordas'), plt.xticks([]), plt.yticks([])

plt.imshow(edges, cmap='gray')
plt.title(''), plt.xticks([]), plt.yticks([])
plt.show()
