# Segmentacion de Gotas

Dada la siguiente imagen: 

![gotas](https://github.com/Monserrath1/Segmentacion-de-Gotas/assets/130505601/e7a9a1e2-8b15-468c-8507-1e93494dde39)

segmentar las gotas, basada en Morfológica Matemática
Las operaciones morfológicas simplifican imágenes y conservan las principales características de forma de los objetos.
1. Aplicamos morfologia Top-Hat, dando como resultado:

![image](https://github.com/Monserrath1/Segmentacion-de-Gotas/assets/130505601/ac8fcf14-38e8-45c1-80bb-9f6fda054075)

2. Después aplicamos apertura, para eliminar las partes pequeñas y recuperar grosor  a continuación se muestra :

![image](https://github.com/Monserrath1/Segmentacion-de-Gotas/assets/130505601/f4221044-a823-46de-bc22-8b06559721c1)

3. Finalmente amplicamos un umbral binario+otsu a la imagen anterior de apertura 

![image](https://github.com/Monserrath1/Segmentacion-de-Gotas/assets/130505601/b4d9e6ed-d3b9-42c1-a0f1-c16987629755)

4.  Dibujamos los contornos de imagen de color rojo

![segmentada](https://github.com/Monserrath1/Segmentacion-de-Gotas/assets/130505601/0e089995-64ff-4eb4-b33c-c3fb40ca9978)
