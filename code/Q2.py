import cv2
import math

gray = cv2.imread('../imagens/knee-mri-white.jpg', 0)
img_pot = cv2.imread('../imagens/knee-mri-white.jpg', 0)

y = 5  # Valor da potecia  BEST VALUES: 1 | 5 | 10 | 15 | 20 | 25 | 30 |
c = 1

for i in range(img_pot.shape[0]):
    for j in range(img_pot.shape[1]):
        img_pot[i, j] = (c*math.pow(img_pot[i, j]/255.0, y))*255.0

cv2.imshow('teste1', gray)
cv2.imshow('teste2', img_pot)
cv2.waitKey(0)
cv2.destroyAllWindows()
