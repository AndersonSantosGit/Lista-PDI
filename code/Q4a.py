#!/usr/bin/python
# -*- coding: utf-8 -*-


import random

import cv2
import numpy as np
from numpy import str_
from matplotlib import pyplot as plt

gray = cv2.imread('../imagens/coins.bmp', 0)

dy, dx = np.gradient(np.double(gray))

mgx = np.power(dx, 2.0)
mgy = np.power(dy, 2.0)

M = np.sqrt((mgx + mgy))  # Magnitude do gradiente

'''
    Metodo Global Simples
'''

# Estimativa Inicial para o limiar Global T
T = random.randint(0, 255)
# parametro dt
dt = 1
T_new = T + dt + 1
while abs(T - T_new) >= dt:
    T = T_new
    res = M >= T
    # Calculo das intensidades medias
    if np.isnan(np.mean(M[res==False])):
        m1 = 0 + 2
    else:
        m1 = int(round(np.mean(M[res==False])))  # Media de 0's
    if np.isnan(np.mean(M[res])):
        m2 = 0 + 2
    else:
        m2 = int(round(np.mean(M[res])))  # Media de 0's
    # Calculo do novo limiar
    T_new = int(round(0.5 * (m1+m2)))

output = M >= T_new

plt.subplot(321), plt.imshow(mgx, cmap='gray')
plt.title('Gx'), plt.xticks([]), plt.yticks([])

plt.subplot(322), plt.imshow(mgy, cmap='gray')
plt.title('Gy'), plt.xticks([]), plt.yticks([])

plt.subplot(323), plt.imshow(M, cmap='gray')
plt.title('Gradiente'), plt.xticks([]), plt.yticks([])

plt.subplot(324), plt.hist(M)
plt.title('Histograma'), plt.xticks([]), plt.yticks([])

plt.subplot(325), plt.imshow(gray, cmap='gray')
plt.title('Imagem Gray Scale'), plt.xticks([]), plt.yticks([])

plt.subplot(326), plt.imshow(output, cmap='gray')
plt.title('Limiar: ' + str_(T_new)), plt.xticks([]), plt.yticks([])

plt.show()

plt.imshow(output, cmap='gray')
plt.title('Limiar: ' + str_(T_new)), plt.xticks([]), plt.yticks([])

plt.show()

# PLOTANDO IMAGENS INDIVIDUAIS

plt.imshow(gray, cmap='gray')
plt.title('Imagem Gray Scale'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(mgx, cmap='gray')
plt.title('Gx'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(mgy, cmap='gray')
plt.title('Gy'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(M, cmap='gray')
plt.title('Gradiente'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(output, cmap='gray')
plt.title('Limiar: ' + str_(T_new)), plt.xticks([]), plt.yticks([])
plt.show()
