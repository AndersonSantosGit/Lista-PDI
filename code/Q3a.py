'''
Created on 3 de out de 2015

@author: Anderson Santos


'''
#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
          
import cv2
import numpy as np 
import random
from matplotlib import pyplot as plt

img = plt.imread('../Imagens/carta_getulio.jpg')
gray = cv2.imread('../Imagens/carta_getulio.jpg',0)


'''
    Metodo Global Simples
'''


#Estimativa Inicial para o limiar Global T
T = random.randint(0,255)
#parametro dt
dt = 1;
T_new = T+ dt+1

#Calculando Histograma
#histograma = plt.hist(gray)
#plt.show()

plt.subplot(121),plt.imshow(gray, cmap = 'gray')
plt.title('Imagem em Niveis de Cinza'), plt.xticks([]), plt.yticks([])    
plt.subplot(122),plt.hist(gray)
plt.title('Histograma'), plt.xticks([]), plt.yticks([])
plt.show()

while abs(T - T_new) >= dt:
    T = T_new
    res = gray >= T
    #Calculo das intensidades medias
    if np.isnan(np.mean(gray[res==False])):
        m1 = 0 + 2
    else:
        m1 = int(round(np.mean(gray[res==False])))  #Media de 0's
    if np.isnan(np.mean(gray[res])):
        m2 = 0 + 2
    else:
        m2 =  int(round(np.mean(gray[res])))  #Media de 0's
    #Calculo do novo limiar
    T_new = int(round(0.5 * (m1+m2)))
    
res = gray >= T_new

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Imagem orginal'), plt.xticks([]), plt.yticks([])    
plt.subplot(132),plt.imshow(gray, cmap = 'gray')
plt.title('Imagem Gray'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(res, cmap = 'gray')
plt.title('Imagem Limiarizada'), plt.xticks([]), plt.yticks([])

plt.show()

plt.imshow(res, cmap = 'gray')
plt.title('Imagem Limiarizada'), plt.xticks([]), plt.yticks([])

plt.show()