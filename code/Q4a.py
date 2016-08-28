#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import cv2
import numpy as np
from numpy import str_
from matplotlib import pyplot as plt

gray = cv2.imread('../imagens/coins.bmp', 0)

d_y, d_x = np.gradient(np.double(gray))

m_gx = np.power(d_x, 2.0)
m_gy = np.power(d_y, 2.0)

m = np.sqrt((m_gx + m_gy))  # Magnitude do gradiente
'''
    Metodo Global Simples
'''
# Estimativa Inicial para o limiar Global t
t = random.randint(0, 255)
# parametro dt
dt = 1
t_new = t + dt + 1
while abs(t - t_new) >= dt:
    t = t_new
    res = m >= t
    # Calculo das intensidades medias
    if np.isnan(np.mean(m[res==False])):
        m1 = 0 + 2
    else:
        m1 = int(round(np.mean(m[res==False])))  # Media de 0's
    if np.isnan(np.mean(m[res])):
        m2 = 0 + 2
    else:
        m2 = int(round(np.mean(m[res])))  # Media de 0's
    # Calculo do novo limiar
    t_new = int(round(0.5 * (m1+m2)))

output = m >= t_new

plt.subplot(321), plt.imshow(m_gx, cmap='gray')
plt.title('Gx'), plt.xticks([]), plt.yticks([])

plt.subplot(322), plt.imshow(m_gy, cmap='gray')
plt.title('Gy'), plt.xticks([]), plt.yticks([])

plt.subplot(323), plt.imshow(m, cmap='gray')
plt.title('Gradiente'), plt.xticks([]), plt.yticks([])

plt.subplot(324), plt.hist(m)
plt.title('Histograma'), plt.xticks([]), plt.yticks([])

plt.subplot(325), plt.imshow(gray, cmap='gray')
plt.title('Imagem Gray Scale'), plt.xticks([]), plt.yticks([])

plt.subplot(326), plt.imshow(output, cmap='gray')
plt.title('Limiar: ' + str_(t_new)), plt.xticks([]), plt.yticks([])

plt.show()

plt.imshow(output, cmap='gray')
plt.title('Limiar: ' + str_(t_new)), plt.xticks([]), plt.yticks([])

plt.show()

# PLOTANDO IMAGENS INDIVIDUAIS

plt.imshow(gray, cmap='gray')
plt.title('Imagem Gray Scale'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(m_gx, cmap='gray')
plt.title('Gx'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(m_gy, cmap='gray')
plt.title('Gy'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(m, cmap='gray')
plt.title('Gradiente'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(output, cmap='gray')
plt.title('Limiar: ' + str_(t_new)), plt.xticks([]), plt.yticks([])
plt.show()
