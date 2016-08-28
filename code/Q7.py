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


def getPixel(image, x, y):
    try:
        return image[x, y]
    except IndexError:
        return 0


def getLBP(img, imgLbp):
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            centro = img[x, y]
            acimaEsquerda = getPixel(img, x-1, y-1)
            acima = getPixel(img, x, y-1)
            acimaDireita = getPixel(img, x+1, y-1)
            direta = getPixel(img, x+1, y)
            esquerda = getPixel(img, x-1, y)
            abaixoEsquerda = getPixel(img, x-1, y+1)
            abaixoDireita = getPixel(img, x+1, y+1)
            abaixo = getPixel(img, x, y+1)
            values = limiar(centro, [acimaEsquerda, acima, acimaDireita, direta, abaixoDireita, abaixo, abaixoEsquerda, esquerda])
            weights = [1, 2, 4, 8, 16, 32, 64, 128]
            res = 0
            for a in range(0, values.__len__()):
                res += weights[a] * values[a]
            imgLbp[x, y] = res
    return imgLbp

# Selecionando as imagens

nQuery = 2  # 1 - 2
nImage = 8  # 1 - 8

imgAux1 = cv2.imread('../imagens/query_' + str_(nQuery) + '.jpg', 0)
imgAux2 = cv2.imread('../imagens/query_' + str_(nQuery) + '.jpg', 0)
imgAux2 = cv2.imread('../imagens/texture_sample_' + str_(nImage) + '.jpg', 0)
imgLBP = cv2.imread('../imagens/query_' + str_(nQuery) + '.jpg', 0)
amostraLBP = cv2.imread('../imagens/texture_sample_' + str_(nImage) + '.jpg', 0)
imgLBP = getLBP(imgAux1, imgLBP)
amostraLBP = getLBP(imgAux2, amostraLBP)

plt.subplot(121), plt.imshow(imgLBP, cmap='gray')
plt.title('LBP Query ' + str_(nQuery)), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(amostraLBP, cmap='gray')
plt.title('LBP Sample ' + str_(nImage)), plt.xticks([]), plt.yticks([])

plt.show()

histImage, bins = np.histogram(imgLBP.flatten(), 256, [0, 256])
histAmostra, bins = np.histogram(amostraLBP.flatten(), 256, [0, 256])

dist = 0
for i in range(histImage.shape[0]):
    dist = dist + np.sqrt(np.power(histImage[i]-histAmostra[i], 2))

if dist != 0:
    print 1.0/float(dist)
else:
    print 1
