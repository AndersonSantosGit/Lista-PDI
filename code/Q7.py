#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from numpy import str_
from matplotlib import pyplot as plt


def limiar(centro, pixels):
    output = []
    for a in pixels:
        if a >= centro:
            output.append(1)
        else:
            output.append(0)
    return output


def get_pixel(image, x, y):
    try:
        return image[x, y]
    except IndexError:
        return 0


def get_lbp(img, img_lbp):
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            centro = img[x, y]
            acima_esquerda = get_pixel(img, x-1, y-1)
            acima = get_pixel(img, x, y-1)
            acima_direita = get_pixel(img, x+1, y-1)
            direta = get_pixel(img, x+1, y)
            esquerda = get_pixel(img, x-1, y)
            abaixo_esquerda = get_pixel(img, x-1, y+1)
            abaixo_direita = get_pixel(img, x+1, y+1)
            abaixo = get_pixel(img, x, y+1)
            values = limiar(centro, [acima_esquerda, acima, acima_direita, direta, abaixo_direita, abaixo,
                                     abaixo_esquerda, esquerda])
            weights = [1, 2, 4, 8, 16, 32, 64, 128]
            res = 0
            for a in range(0, values.__len__()):
                res += weights[a] * values[a]
            img_lbp[x, y] = res
    return img_lbp

# Selecionando as imagens

n_query = 2  # 1 - 2
n_image = 8  # 1 - 8

img_aux_1 = cv2.imread('../imagens/query_' + str_(n_query) + '.jpg', 0)
img_aux_2 = cv2.imread('../imagens/query_' + str_(n_query) + '.jpg', 0)
img_aux_2 = cv2.imread('../imagens/texture_sample_' + str_(n_image) + '.jpg', 0)
img_lbp = cv2.imread('../imagens/query_' + str_(n_query) + '.jpg', 0)
amostra_lbp = cv2.imread('../imagens/texture_sample_' + str_(n_image) + '.jpg', 0)
img_lbp = get_lbp(img_aux_1, img_lbp)
amostra_lbp = get_lbp(img_aux_2, amostra_lbp)

plt.subplot(121), plt.imshow(img_lbp, cmap='gray')
plt.title('LBP Query ' + str_(n_query)), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(amostra_lbp, cmap='gray')
plt.title('LBP Sample ' + str_(n_image)), plt.xticks([]), plt.yticks([])

plt.show()

hist_image, bins = np.histogram(img_lbp.flatten(), 256, [0, 256])
hist_amostra, bins = np.histogram(amostra_lbp.flatten(), 256, [0, 256])

dist = 0
for i in range(hist_image.shape[0]):
    dist = dist + np.sqrt(np.power(hist_image[i]-hist_amostra[i], 2))

if dist != 0:
    print 1.0/float(dist)
else:
    print 1
