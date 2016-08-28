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

bit_1 = np.mod(img, 2)  # LSB
bit_2 = np.mod(np.floor(np.divide(img, 2.)), 2)
bit_3 = np.mod(np.floor(np.divide(img, 4.)), 2)
bit_4 = np.mod(np.floor(np.divide(img, 8.)), 2)
bit_5 = np.mod(np.floor(np.divide(img, 16.)), 2)
bit_6 = np.mod(np.floor(np.divide(img, 32.)), 2)
bit_7 = np.mod(np.floor(np.divide(img, 64.)), 2)
bit_8 = np.mod(np.floor(np.divide(img, 128.)), 2)  # MSB

im_reconstrucao_8 = 2*(2*(2*(2*(2*(2*(2*bit_8+bit_7)+bit_6)+bit_5)+bit_4)+bit_3)+bit_2)+bit_1
im_reconstrucao_7 = 2*(2*(2*(2*(2*(2*bit_8+bit_7)+bit_6)+bit_5)+bit_4)+bit_3)+bit_2
im_reconstrucao_6 = 2*(2*(2*(2*(2*bit_8+bit_7)+bit_6)+bit_5)+bit_4)+bit_3
im_reconstrucao_5 = 2*(2*(2*(2*bit_8+bit_7)+bit_6)+bit_5)+bit_4
im_reconstrucao_4 = 2*(2*(2*bit_8+bit_7)+bit_6)+bit_5
im_reconstrucao_3 = 2*(2*bit_8+bit_7)+bit_6
im_reconstrucao_2 = 2*bit_8+bit_7
im_reconstrucao_1 = bit_8

plt.subplot(248), plt.imshow(im_reconstrucao_1, cmap='gray')
plt.title('1 Mapa'), plt.xticks([]), plt.yticks([])

plt.subplot(247), plt.imshow(im_reconstrucao_2, cmap='gray')
plt.title('2 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(246), plt.imshow(im_reconstrucao_3, cmap='gray')
plt.title('3 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(245), plt.imshow(im_reconstrucao_4, cmap='gray')
plt.title('4 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(244), plt.imshow(im_reconstrucao_5, cmap='gray')
plt.title('5 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(243), plt.imshow(im_reconstrucao_6, cmap='gray')
plt.title('6 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(242), plt.imshow(im_reconstrucao_7, cmap='gray')
plt.title('7 Mapas'), plt.xticks([]), plt.yticks([])

plt.subplot(241), plt.imshow(im_reconstrucao_8, cmap='gray')
plt.title('8 Mapas'), plt.xticks([]), plt.yticks([])

plt.show()

plt.subplot(331), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(332), plt.imshow(bit_1, cmap='gray')
plt.title('Map Bit 1'), plt.xticks([]), plt.yticks([])

plt.subplot(333), plt.imshow(bit_2, cmap='gray')
plt.title('Map Bit 2'), plt.xticks([]), plt.yticks([])

plt.subplot(334), plt.imshow(bit_3, cmap='gray')
plt.title('Map Bit 3'), plt.xticks([]), plt.yticks([])

plt.subplot(335), plt.imshow(bit_4, cmap='gray')
plt.title('Map Bit 4'), plt.xticks([]), plt.yticks([])

plt.subplot(336), plt.imshow(bit_5, cmap='gray')
plt.title('Map Bit 5'), plt.xticks([]), plt.yticks([])

plt.subplot(337), plt.imshow(bit_6, cmap='gray')
plt.title('Map Bit 6'), plt.xticks([]), plt.yticks([])

plt.subplot(338), plt.imshow(bit_7, cmap='gray')
plt.title('Map Bit 7'), plt.xticks([]), plt.yticks([])

plt.subplot(339), plt.imshow(bit_8, cmap='gray')
plt.title('Map Bit 8'), plt.xticks([]), plt.yticks([])

plt.show()

medias = []
variancias = []
curtoses = []
assimetrias = []

for i in range(int(im_reconstrucao_3.max()+1)):
    indices = np.equal(im_reconstrucao_3, i)
    plt.imshow(indices, cmap='gray')
    im_aux = np.multiply(img, indices)
    if(im_aux.max()):
        # plt.imshow(im_aux, cmap='gray')
        # plt.title('Intensidade: ' + str_(i)), plt.xticks([]), plt.yticks([])
        # plt.show()
        medias.append(np.mean(im_aux))
        variancias.append(np.var(im_aux))
        curtoses.append(np.mean(kurtosis(im_aux)))
        assimetrias.append(np.mean(skew(im_aux)))
    else:
        medias.append(0)
        variancias.append(0)
        curtoses.append(0)
        assimetrias.append(0)
        print 'A imagem não possui nenhuma intensidade ' + str_(i)

niveis = []
# plt.imshow(im_reconstrucao_3, cmap='gray')
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
output = np.multiply(im_reconstrucao_3, 0)
output_2 = np.multiply(im_reconstrucao_3, 0)
for i in range(1, len(niveis)):
    indices = np.equal(im_reconstrucao_3, niveis[i])
    output[indices] = np.add(output[indices], im_reconstrucao_3[indices])
    output_2[indices] = np.add(output_2[indices], np.divide(im_reconstrucao_3[indices], niveis[i]))

output = np.multiply(im_reconstrucao_3, output_2)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Tons de Cinza'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(im_reconstrucao_3, cmap='gray')
plt.title('Reconstrucao'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(output_2, cmap='gray')
plt.title('Segmentacao'), plt.xticks([]), plt.yticks([])
plt.show()
