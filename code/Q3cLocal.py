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
t = [[random.randint(0, 255) for x in range(int(im_local_r.shape[1]/w))] for x in range(int((im_local_r.shape[0]/w)))]

# parametro dt
dt = 1
t_new = np.array(t)+dt+1
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
        while abs(t[i][j] - t_new[i, j]) >= dt:
            t[i][j] = t_new[i, j]
            res = window >= t[i][j]
            # plt.hist(window)
            # plt.show()
            # Calculo das intensidades medias
            if np.isnan(np.mean(window[res==False])):
                m_1 = 0 + 2
            else:
                m_1 = int(round(np.mean(window[res==False])))  # Media de 0's
            if np.isnan(np.mean(window[res])):
                m_2 = 0 + 2
            else:
                m_2 = int(round(np.mean(window[res])))  # Media de 0's
            # Calculo do novo limiar
            t_new[i, j] = int(round(0.5 * (m_1+m_2)))
        im_local_r[r:r+windowsize_r, c:c+windowsize_c] = im_local_r[r:r+windowsize_r, c:c+windowsize_c] >= t_new[i, j]
        j = j+1

    # Ajustando na horizontal
    if np.mod(im_local_r.shape[1], w) != 0:
        # Redimensionando a janela
        windowsize_r_aux = w
        windowsize_c_aux = int(np.mod(im_local_r.shape[1], w))
        # Obtendo a janela
        window = im_local_r[r:r+windowsize_r_aux, c:c+windowsize_c_aux]
        t_aux = random.randint(0, 255)
        t_new_aux = t_aux+dt+1
        while abs(t_aux - t_new_aux) >= dt:
            t_aux = t_new_aux
            res = window >= t_aux
            # Calculo das intensidades medias
            if np.isnan(np.mean(window[res==False])):
                m_1 = 0 + 2
            else:
                m_1 = int(round(np.mean(window[res==False])))  # Media de 0's
            if np.isnan(np.mean(window[res])):
                m_2 = 0 + 2
            else:
                m_2 = int(round(np.mean(window[res])))  # Media de 0's
            # Calculo do novo limiar
            t_new_aux = int(round(0.5 * (m_1+m_2)))
        im_local_r[r:r+windowsize_r_aux, c+windowsize_c:c+windowsize_c+windowsize_c_aux] = im_local_r[r:r+windowsize_r_aux, c+windowsize_c:c+windowsize_c+windowsize_c_aux] >= t_new_aux
    i = i+1

# Ajustando na Vertical
if np.mod(im_local_r.shape[0], w) != 0:
    # Redimensionando a janela
    windowsize_r_aux = int(np.mod(im_local_r.shape[0], w))
    windowsize_c_aux = w
    # Percorrendo a ultima linha da imagem
    for c in range(0, im_local_r.shape[1] - windowsize_c_aux, windowsize_c_aux):  # Colunas
        window = im_local_r[r+windowsize_r:r+windowsize_r_aux, c:c+windowsize_c_aux]
        t_aux = random.randint(0, 255)
        t_new_aux = t_aux+dt+1
        while abs(t_aux - t_new_aux) >= dt:
            t_aux = t_new_aux
            res = window >= t_aux
            # Calculo das intensidades medias
            if np.isnan(np.mean(window[res==False])):
                m_1 = 0 + 2
            else:
                m_1 = int(round(np.mean(window[res==False])))  # Media de 0's
            if np.isnan(np.mean(window[res])):
                m_2 = 0 + 2
            else:
                m_2 = int(round(np.mean(window[res])))  # Media de 0's
            # Calculo do novo limiar
            t_new_aux = int(round(0.5 * (m_1+m_2)))
        im_local_r[r+windowsize_r:(r+windowsize_r+windowsize_r_aux), c:c+windowsize_c] = im_local_r[r+windowsize_r:(r+windowsize_r+windowsize_r_aux), c:c+windowsize_c] >= t_new_aux

# Ajustando na horizontal - Ultimo frame :p
if np.mod(im_local_r.shape[1], w) != 0:
    # Redimensionando a janela
    windowsize_r_aux = int(np.mod(im_local_r.shape[0], w))
    windowsize_c_aux = int(np.mod(im_local_r.shape[1], w))
    # Obtendo a janela
    window = im_local_r[r+windowsize_r:r+windowsize_r_aux, c+windowsize_c:c+windowsize_c_aux]
    t_aux = random.randint(0, 255)
    t_new_aux = t_aux+dt+1
    while abs(t_aux - t_new_aux) >= dt:
        t_aux = t_new_aux
        res = window >= t_aux
        # Calculo das intensidades medias
        if np.isnan(np.mean(window[res==False])):
            m_1 = 0 + 2
        else:
            m_1 = int(round(np.mean(window[res==False])))  # Media de 0's
        if np.isnan(np.mean(window[res])):
            m_2 = 0 + 2
        else:
            m_2 = int(round(np.mean(window[res])))  # Media de 0's
        # Calculo do novo limiar
        t_new_aux = int(round(0.5 * (m_1+m_2)))
    im_local_r[r+windowsize_r:(r+windowsize_r+windowsize_r_aux), c+windowsize_c:(c+windowsize_c+windowsize_c_aux)] = im_local_r[r+windowsize_r:(r+windowsize_r+windowsize_r_aux),c+windowsize_c:(c+windowsize_c+windowsize_c_aux)]>=t_new_aux


plt.imshow(im_local_r, cmap='gray')
plt.title('Imagem Limiarizada sem Realce'), plt.xticks([]), plt.yticks([])
plt.show()
