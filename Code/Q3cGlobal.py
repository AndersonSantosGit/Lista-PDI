'''
Created on 4 de out de 2015

@author: Anderson Santos

'''
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
          
import cv2
from matplotlib import pyplot as plt
import math
import numpy as np
import random

img = plt.imread('../Imagens/carta_getulio.jpg')
gray = cv2.imread('../Imagens/carta_getulio.jpg',0)

imGlobalR = cv2.imread('../Imagens/carta_getulio.jpg',0)

#plt.imshow(gray, cmap = 'gray')
#plt.title('Imagem sem Realce'), plt.xticks([]), plt.yticks([])
#plt.show()

y = 3  #Valor da potencia
c = 1
for i in range(imGlobalR.shape[0]):
    for j in range(imGlobalR.shape[1]):
        imGlobalR[i,j] = (c * math.pow(imGlobalR[i,j]/255.0,y))*255.0;

plt.subplot(121),plt.imshow(gray, cmap = 'gray')
plt.title('Imagem sem Realce'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imGlobalR, cmap = 'gray')
plt.title('Imagem com Realce'), plt.xticks([]), plt.yticks([])

plt.show()

plt.show()

'''
    Metodo Global Simples
'''
#Estimativa Inicial para o limiar Global T - IMAGEM COM REALCE
T = random.randint(0,255)
#parametro dt
dt = 1;
T_new = T+ dt+1
while abs(T - T_new) >= dt:
    T = T_new
    res = imGlobalR >= T
    #Calculo das intensidades medias
    if np.isnan(np.mean(imGlobalR[res==False])):
        m1 = 0 + 2
    else:
        m1 = int(round(np.mean(imGlobalR[res==False])))  #Media de 0's
    if np.isnan(np.mean(imGlobalR[res])):
        m2 = 0 + 2
    else:
        m2 =  int(round(np.mean(imGlobalR[res])))  #Media de 0's
    #Calculo do novo limiar
    T_new = int(round(0.5 * (m1+m2)))


imGlobalR = imGlobalR >= T_new
plt.imshow(imGlobalR, cmap = 'gray')
plt.title('Imagem Limiarizada com Realce'), plt.xticks([]), plt.yticks([])

plt.show()