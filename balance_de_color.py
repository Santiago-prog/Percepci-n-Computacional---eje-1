import cv2
import numpy as np
from matplotlib import pyplot as plt
original = cv2.imread(‘original.jpg') 
resultado = cv2.imread(‘original.jpg')
pixeles = resultado.shape[0] * resultado.shape[1]
canal_rojo = cv2.calcHist([resultado], [0], None, [256], [0, 256])
canal_verde = cv2.calcHist([resultado], [1], None, [256], [0, 256])
canal_azul = cv2.calcHist([resultado], [2], None, [256], [0, 256])
total_canal_rojo = 0
total_canal_verde = 0
total_canal_azul = 0
percentil_inferior = 0.01
percentil_superior = 1 - percentil_inferior
percentil_rojo_inferior = 0
percentil_rojo_superior = 0
percentil_verde_inferior = 0
percentil_verde_superior = 0
percentil_azul_inferior = 0
percentil_azul_superior = 0
percentil_rojo_inferior_localizado = 0
percentil_rojo_superior_localizado = 0
percentil_verde_inferior_localizado = 0
percentil_verde_superior_localizado = 0
percentil_azul_inferior_localizado = 0
percentil_azul_superior_localizado = 0
coef = 200

for i in range (256):
 total_canal_rojo = int(total_canal_rojo + canal_rojo[i])
 total_canal_verde = int(total_canal_verde + canal_verde[i])
 total_canal_azul = int(total_canal_azul + canal_azul[i])
 if total_canal_rojo >= percentil_inferior * pixeles and percentil_rojo_inferior_localizado == 0:
 percentil_rojo_inferior = i;
 percentil_rojo_inferior_localizado = 1;
 if total_canal_rojo >= percentil_superior * pixeles and percentil_rojo_superior_localizado == 0:
 percentil_rojo_superior = i
 percentil_rojo_superior_localizado = 1;
 if total_canal_verde >= percentil_inferior * pixeles and percentil_verde_inferior_localizado == 0:
 percentil_verde_inferior = i
 percentil_verde_inferior_localizado = 1;
 if total_canal_verde >= percentil_superior * pixeles and percentil_verde_superior_localizado == 0:
 percentil_verde_superior = i
 percentil_verde_superior_localizado = 1;
 if total_canal_azul >= percentil_inferior * pixeles and percentil_azul_inferior_localizado == 0:
 percentil_azul_inferior = i
 percentil_azul_inferior_localizado = 1;
 if total_canal_azul >= percentil_superior * pixeles and percentil_azul_superior_localizado == 0:
 percentil_azul_superior = i
 percentil_azul_superior_localizado = 1;
for x in range(resultado.shape[0]):
 for y in range(resultado.shape[1]):
 if resultado[x,y][0] >= percentil_rojo_inferior: resultado[x,y][0] = resultado[x,y][0] - percentil_rojo_inferior
 if resultado[x,y][1] >= percentil_verde_inferior: resultado[x,y][1] = resultado[x,y][1] - percentil_verde_inferior
 if resultado[x,y][2] >= percentil_azul_inferior: resultado[x,y][2] = resultado[x,y][2] - percentil_azul_inferior
 if resultado[x,y][0] < 0:
 print (x,',',y, ' es ',resultado[x,y][0])
 resultado[x,y][0] = 0
 if resultado[x,y][1] < 0: 
 print (x,',',y, ' es ',resultado[x,y][1])
 resultado[x,y][1] = 0
 if resultado[x,y][2] < 0:
 print (x,',',y, ' es ',resultado[x,y][2])
 resultado[x,y][2] = 0
 resultado[x,y][0] = int(coef * resultado[x,y][0] / (percentil_rojo_superior-percentil_rojo_inferior))
 resultado[x,y][1] = int(coef * resultado[x,y][1] / (percentil_verde_superior-percentil_verde_inferior))
 resultado[x,y][2] = int(coef * resultado[x,y][2] / (percentil_azul_superior-percentil_azul_inferior))
 if resultado[x,y][0] > 255:
 print (x,',',y, ' es ',resultado[x,y][0])
 resultado[x,y][0] = 255
 if resultado[x,y][1] > 255:
 print (x,',',y, ' es ',resultado[x,y][1])
 resultado[x,y][1] = 255
 if resultado[x,y][2] > 255:
 print (x,',',y, ' es ',resultado[x,y][2])
 resultado[x,y][2] = 255
canal_rojo2 = cv2.calcHist([resultado], [0], None, [256], [0, 256])
canal_verde2 = cv2.calcHist([resultado], [1], None, [256], [0, 256])
canal_azul2 = cv2.calcHist([resultado], [2], None, [256], [0, 256])
plt.plot(canal_rojo, color='R' )
plt.plot(canal_verde, color='G' )
plt.plot(canal_azul, color='B' )
plt.xlabel('intensidad de iluminación')
plt.ylabel('cantidad de pixeles')
plt.show()
plt.plot(canal_rojo2, color='R' )
plt.plot(canal_verde2, color='G' )
plt.plot(canal_azul2, color='B' )
plt.xlabel('intensidad de iluminación')
plt.ylabel('cantidad de pixeles')
plt.show()
union = np.concatenate((original, resultado), axis=1) # axis = 0 vertical 1 horizontal
cv2.imshow('imagenes',union)
cv2.imwrite('resultado.jpg', union)
cv2.waitKey(0)
cv2.destroyAllWindows() 
