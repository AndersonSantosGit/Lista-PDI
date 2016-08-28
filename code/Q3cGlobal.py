#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import random

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = plt.imread('../imagens/carta_getulio.jpg')
gray = cv2.imread('../imagens/carta_getulio.jpg', 0)
im_global_r = cv2.imread('../imagens/carta_getulio.jpg', 0)

plt.imshow(gray, cmap='gray')
plt.title('Imagem sem Realce'), plt.xticks([]), plt.yticks([])
plt.show()

y = 3  # Valor da potencia
c = 1
for i in range(im_global_r.shape[0]):
    for j in range(im_global_r.shape[1]):
        im_global_r[i, j] = (c*math.pow(im_global_r[i, j]/255.0, y))*255.0

plt.subplot(121), plt.imshow(gray, cmap='gray')
plt.title('Imagem sem Realce'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(im_global_r, cmap='gray')
plt.title('Imagem com Realce'), plt.xticks([]), plt.yticks([])

plt.show()

'''
    Metodo Global Simples
'''
# Estimativa Inicial para o limiar Global T - IMAGEM COM REALCE
T = random.randint(0, 255)
# parametro dt
dt = 1
t_new = T + dt + 1
while abs(T - t_new) >= dt:
    T = t_new
    res = im_global_r >= T
    # Calculo das intensidades medias
    if np.isnan(np.mean(im_global_r[res==False])):
        m_1 = 0 + 2
    else:
        m_1 = int(round(np.mean(im_global_r[res==False])))  # Media de 0's
    if np.isnan(np.mean(im_global_r[res])):
        m_2 = 0 + 2
    else:
        m_2 = int(round(np.mean(im_global_r[res])))  # Media de 0's
    # Calculo do novo limiar
    t_new = int(round(0.5 * (m_1+m_2)))

im_global_r = im_global_r >= t_new
plt.imshow(im_global_r, cmap='gray')
plt.title('Imagem Limiarizada com Realce'), plt.xticks([]), plt.yticks([])

plt.show()
