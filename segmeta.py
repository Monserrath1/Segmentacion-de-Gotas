import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy

img = cv2.imread('gotas.jpeg')
img = cv2.resize(img, (550, 350))#cambia tamaño de la imagen
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cambia a escala de grises
#mascara 25x25
ee = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (23,23)  );
#aplica morfologia Top-Hat 
tophat = cv2.morphologyEx( img1,cv2.MORPH_TOPHAT, ee )
#mascara 7x7
e1 = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (7,7)  );
# aplica morfologia de apertura para eliminar las partes pequeñas y recuperar grosor 
apertura = cv2.morphologyEx( tophat, cv2.MORPH_OPEN, e1 )

# obtiene el umbral binario+otsu de la apertura 
ret5, thresh = cv2.threshold(apertura, 0, 255, cv2.THRESH_BINARY +  cv2.THRESH_OTSU)
# copia la imagen original
img2=copy.copy(img)
# obtener los contornos de la imagen umbralizada
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# dibujar los contornos de la copia de imagen original de color rojo ,la linea con 1 de grosor
cv2.drawContours(img2, contours, -1, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("Top-Hat - Apertura - umbralizada",np.hstack((tophat,apertura,thresh)))
cv2.imshow("original - segmentada",np.hstack((img,img2)))
cv2.imwrite("segmentada.jpg",img2)
cv2.waitKey()
cv2.destroyAllWindows()