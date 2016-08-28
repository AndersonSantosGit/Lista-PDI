#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

import cv2
import numpy as np
from numpy import str_
from matplotlib import pyplot as plt
from scipy.stats.stats import kurtosis, skew

'''
    Parametros (Limiar)

    pyramid: 500 | 100
    flowers: 400 | 200
    animals: 450 | 200
    bear:    500 | 200

'''
name = 'animals'  # pyramid | flowers | animals | bear
img = cv2.imread('../imagens/' + name + '.jpg', 0)

limiar = 200

bit1 = np.mod(img, 2)  # LSB
bit2 = np.mod(np.floor(np.divide(img, 2.)), 2)
bit3 = np.mod(np.floor(np.divide(img, 4.)), 2)
bit4 = np.mod(np.floor(np.divide(img, 8.)), 2)
bit5 = np.mod(np.floor(np.divide(img, 16.)), 2)
bit6 = np.mod(np.floor(np.divide(img, 32.)), 2)
bit7 = np.mod(np.floor(np.divide(img, 64.)), 2)
bit8 = np.mod(np.floor(np.divide(img, 128.)), 2)  # MSB

imReconstrucao8 = 2*(2*(2*(2*(2*(2*(2*bit8+bit7)+bit6)+bit5)+bit4)+bit3)+bit2)+bit1
imReconstrucao7 = 2*(2*(2*(2*(2*(2*bit8+bit7)+bit6)+bit5)+bit4)+bit3)+bit2
imReconstrucao6 = 2*(2*(2*(2*(2*bit8+bit7)+bit6)+bit5)+bit4)+bit3
imReconstrucao5 = 2*(2*(2*(2*bit8+bit7)+bit6)+bit5)+bit4
imReconstrucao4 = 2*(2*(2*bit8+bit7)+bit6)+bit5
imReconstrucao3 = 2*(2*bit8+bit7)+bit6
imReconstrucao2 = 2*bit8+bit7
imReconstrucao1 = bit8

plt.subplot(248), plt.imshow(imReconstrucao1, cmap='gray')
plt.title('1 Mapa'), plt.xticks([]), plt.yticks([])

plt.subplot(247), plt.imshow(imReconstrucao2, cmap='gray')
plt.title('2 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(246), plt.imshow(imReconstrucao3, cmap='gray')
plt.title('3 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(245), plt.imshow(imReconstrucao4, cmap='gray')
plt.title('4 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(244), plt.imshow(imReconstrucao5, cmap='gray')
plt.title('5 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(243), plt.imshow(imReconstrucao6, cmap='gray')
plt.title('6 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(242), plt.imshow(imReconstrucao7, cmap='gray')
plt.title('7 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(241), plt.imshow(imReconstrucao8, cmap='gray')
plt.title('8 Mapas'), plt.xticks([]), plt.yticks([])

plt.show()

plt.subplot(331), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(332), plt.imshow(bit1, cmap='gray')
plt.title('Map Bit 1'), plt.xticks([]), plt.yticks([])

plt.subplot(333), plt.imshow(bit2, cmap='gray')
plt.title('Map Bit 2'), plt.xticks([]), plt.yticks([])

plt.subplot(334), plt.imshow(bit3, cmap='gray')
plt.title('Map Bit 3'), plt.xticks([]), plt.yticks([])

plt.subplot(335), plt.imshow(bit4, cmap='gray')
plt.title('Map Bit 4'), plt.xticks([]), plt.yticks([])

plt.subplot(336), plt.imshow(bit5, cmap='gray')
plt.title('Map Bit 5'), plt.xticks([]), plt.yticks([])

plt.subplot(337), plt.imshow(bit6, cmap='gray')
plt.title('Map Bit 6'), plt.xticks([]), plt.yticks([])

plt.subplot(338), plt.imshow(bit7, cmap='gray')
plt.title('Map Bit 7'), plt.xticks([]), plt.yticks([])

plt.subplot(339), plt.imshow(bit8, cmap='gray')
plt.title('Map Bit 8'), plt.xticks([]), plt.yticks([])

plt.show()

medias = []
variancias = []
curtoses = []
assimetrias = []

for i in range(int(imReconstrucao3.max()+1)):
    indices = np.equal(imReconstrucao3, i)
    plt.imshow(indices, cmap='gray')
    imAux = np.multiply(img, indices)
    if(imAux.max()):
        # plt.imshow(imAux, cmap='gray')
        # plt.title('Intensidade: ' + str_(i)), plt.xticks([]), plt.yticks([])
        # plt.show()
        medias.append(np.mean(imAux))
        variancias.append(np.var(imAux))
        curtoses.append(np.mean(kurtosis(imAux)))
        assimetrias.append(np.mean(skew(imAux)))
    else:
        medias.append(0)
        variancias.append(0)
        curtoses.append(0)
        assimetrias.append(0)
        print 'A imagem não possui nenhuma intensidade ' + str_(i)

niveis = []
# plt.imshow(imReconstrucao3, cmap='gray')
# plt.show()
for i in range(len(medias)):
    for j in range(len(medias)):
        if(i != j):
            distancia = math.sqrt(np.power((medias[i]-medias[j]), 2)+np.power((variancias[i]-variancias[j]), 2) +
                                  np.power((curtoses[i]-curtoses[j]), 2)+np.power((assimetrias[i]-assimetrias[j]), 2))
            if distancia < limiar:
                if not(i in niveis):
                    niveis.append(i)

# Segmentacao Final :D
output = np.multiply(imReconstrucao3, 0)
output2 = np.multiply(imReconstrucao3, 0)
for i in range(1, len(niveis)):
    indices = np.equal(imReconstrucao3, niveis[i])
    output[indices] = np.add(output[indices], imReconstrucao3[indices])
    output2[indices] = np.add(output2[indices], np.divide(imReconstrucao3[indices], niveis[i]))

output = np.multiply(imReconstrucao3, output2)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Tons de Cinza'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(imReconstrucao3, cmap='gray')
plt.title('Reconstrucao'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(output2, cmap='gray')
plt.title('Segmentacao'), plt.xticks([]), plt.yticks([])
plt.show()
