import cv2
import math

gray = cv2.imread('../imagens/knee-mri-white.jpg', 0)
imgPot = cv2.imread('../imagens/knee-mri-white.jpg', 0)

y = 5  # Valor da potecia  BEST VALUES: 1 | 5 | 10 | 15 | 20 | 25 | 30 |
c = 1

for i in range(imgPot.shape[0]):
    for j in range(imgPot.shape[1]):
        imgPot[i, j] = (c*math.pow(imgPot[i, j]/255.0, y))*255.0

cv2.imshow('teste1', gray)
cv2.imshow('teste2', imgPot)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
plt.subplot(131),plt.imshow(gray, cmap = 'gray')
plt.title('Imagem orginal'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(imgPot, cmap = 'gray')
plt.title('Transformacao de Potencia'), plt.xticks([]), plt.yticks([])

plt.show()

'''
