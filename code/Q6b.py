#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

name = 'animals'  # pyramid | flowers | bear | animals
img = cv2.imread('../imagens/' + name + '.jpg', 0)

# Gaussian filtering
blur = cv2.GaussianBlur(img, (5, 5), 0)  # Otsu's thresholding after Gaussian filtering
ret_3, th_3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret_2, th_2 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
plt.imshow(th_2, cmap='gray')
plt.title('Otsu'), plt.xticks([]), plt.yticks([])
plt.show()

bit_1 = np.mod(img, 2)  # LSB
bit_2 = np.mod(np.floor(np.divide(img, 2.)), 2)
bit_3 = np.mod(np.floor(np.divide(img, 4.)), 2)
bit_4 = np.mod(np.floor(np.divide(img, 8.)), 2)
bit_5 = np.mod(np.floor(np.divide(img, 16.)), 2)
bit_6 = np.mod(np.floor(np.divide(img, 32.)), 2)
bit_7 = np.mod(np.floor(np.divide(img, 64.)), 2)
bit_8 = np.mod(np.floor(np.divide(img, 128.)), 2)  # MSB

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
