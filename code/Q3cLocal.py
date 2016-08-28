#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = plt.imread('../imagens/carta_getulio.jpg')
gray = cv2.imread('../imagens/carta_getulio.jpg', 0)

im_local_r = cv2.imread('../imagens/carta_getulio.jpg', 0)

y = 3  # Valor da potencia
c = 1
for i in range(im_local_r.shape[0]):
    for j in range(im_local_r.shape[1]):
        im_local_r[i, j] = (c * math.pow(im_local_r[i, j]/255.0, y))*255.0

plt.imshow(im_local_r, cmap='gray')
plt.title('Imagem com Realce'), plt.xticks([]), plt.yticks([])
plt.show()

'''
    Limiarizacao Local
'''
w = 50
# Iniciando os Limiares
T = [[random.randint(0, 255) for x in range(int(im_local_r.shape[1]/w))] for x in range(int((im_local_r.shape[0]/w)))]

# parametro dt
dt = 1
T_new = np.array(T)+dt+1
# Define the window size
windowsize_r = w
windowsize_c = w
i = 0
for r in range(0, im_local_r.shape[0]-windowsize_r, windowsize_r):  # linhas
    j = 0
    for c in range(0, im_local_r.shape[1]-windowsize_c, windowsize_c):  # Colunas
        window = im_local_r[r:r+windowsize_r, c:c+windowsize_c]
        # plt.imshow(window, cmap = 'gray')
        # plt.show()
        # hist = np.histogram(window,bins=256)
        while abs(T[i][j] - T_new[i, j]) >= dt:
            T[i][j] = T_new[i, j]
            res = window >= T[i][j]
            # plt.hist(window)
            # plt.show()
            # Calculo das intensidades medias
            if np.isnan(np.mean(window[res==False])):
                m1 = 0 + 2
            else:
                m1 = int(round(np.mean(window[res==False])))  # Media de 0's
            if np.isnan(np.mean(window[res])):
                m2 = 0 + 2
            else:
                m2 = int(round(np.mean(window[res])))  # Media de 0's
            # Calculo do novo limiar
            T_new[i, j] = int(round(0.5 * (m1+m2)))
        im_local_r[r:r+windowsize_r, c:c+windowsize_c] = im_local_r[r:r+windowsize_r, c:c+windowsize_c] >= T_new[i, j]
        j = j+1

    # Ajustando na horizontal
    if np.mod(im_local_r.shape[1], w) != 0:
        # Redimensionando a janela
        windowsize_r_AUX = w
        windowsize_c_AUX = int(np.mod(im_local_r.shape[1], w))
        # Obtendo a janela
        window = im_local_r[r:r+windowsize_r_AUX, c:c+windowsize_c_AUX]
        T_AUX = random.randint(0, 255)
        T_new_AUX = T_AUX+dt+1
        while abs(T_AUX - T_new_AUX) >= dt:
            T_AUX = T_new_AUX
            res = window >= T_AUX
            # Calculo das intensidades medias
            if np.isnan(np.mean(window[res==False])):
                m1 = 0 + 2
            else:
                m1 = int(round(np.mean(window[res==False])))  # Media de 0's
            if np.isnan(np.mean(window[res])):
                m2 = 0 + 2
            else:
                m2 = int(round(np.mean(window[res])))  # Media de 0's
            # Calculo do novo limiar
            T_new_AUX = int(round(0.5 * (m1+m2)))
        im_local_r[r:r+windowsize_r_AUX, c+windowsize_c:c+windowsize_c+windowsize_c_AUX] = im_local_r[r:r+windowsize_r_AUX, c+windowsize_c:c+windowsize_c+windowsize_c_AUX] >= T_new_AUX
    i = i+1

# Ajustando na Vertical
if np.mod(im_local_r.shape[0], w) != 0:
    # Redimensionando a janela
    windowsize_r_AUX = int(np.mod(im_local_r.shape[0], w))
    windowsize_c_AUX = w
    # Percorrendo a ultima linha da imagem
    for c in range(0, im_local_r.shape[1] - windowsize_c_AUX, windowsize_c_AUX):  # Colunas
        window = im_local_r[r+windowsize_r:r+windowsize_r_AUX, c:c+windowsize_c_AUX]
        T_AUX = random.randint(0, 255)
        T_new_AUX = T_AUX+dt+1
        while abs(T_AUX - T_new_AUX) >= dt:
            T_AUX = T_new_AUX
            res = window >= T_AUX
            # Calculo das intensidades medias
            if np.isnan(np.mean(window[res==False])):
                m1 = 0 + 2
            else:
                m1 = int(round(np.mean(window[res==False])))  # Media de 0's
            if np.isnan(np.mean(window[res])):
                m2 = 0 + 2
            else:
                m2 = int(round(np.mean(window[res])))  # Media de 0's
            # Calculo do novo limiar
            T_new_AUX = int(round(0.5 * (m1+m2)))
        im_local_r[r+windowsize_r:(r+windowsize_r+windowsize_r_AUX), c:c+windowsize_c] = im_local_r[r+windowsize_r:(r+windowsize_r+windowsize_r_AUX), c:c+windowsize_c] >= T_new_AUX

# Ajustando na horizontal - Ultimo frame :p
if np.mod(im_local_r.shape[1], w) != 0:
    # Redimensionando a janela
    windowsize_r_AUX = int(np.mod(im_local_r.shape[0], w))
    windowsize_c_AUX = int(np.mod(im_local_r.shape[1], w))
    # Obtendo a janela
    window = im_local_r[r+windowsize_r:r+windowsize_r_AUX, c+windowsize_c:c+windowsize_c_AUX]
    T_AUX = random.randint(0, 255)
    T_new_AUX = T_AUX+dt+1
    while abs(T_AUX - T_new_AUX) >= dt:
        T_AUX = T_new_AUX
        res = window >= T_AUX
        # Calculo das intensidades medias
        if np.isnan(np.mean(window[res==False])):
            m1 = 0 + 2
        else:
            m1 = int(round(np.mean(window[res==False])))  # Media de 0's
        if np.isnan(np.mean(window[res])):
            m2 = 0 + 2
        else:
            m2 = int(round(np.mean(window[res])))  # Media de 0's
        # Calculo do novo limiar
        T_new_AUX = int(round(0.5 * (m1+m2)))
    im_local_r[r+windowsize_r:(r+windowsize_r+windowsize_r_AUX), c+windowsize_c:(c+windowsize_c+windowsize_c_AUX)] = im_local_r[r+windowsize_r:(r+windowsize_r+windowsize_r_AUX),c+windowsize_c:(c+windowsize_c+windowsize_c_AUX)]>=T_new_AUX


plt.imshow(im_local_r, cmap='gray')
plt.title('Imagem Limiarizada sem Realce'), plt.xticks([]), plt.yticks([])
plt.show()
