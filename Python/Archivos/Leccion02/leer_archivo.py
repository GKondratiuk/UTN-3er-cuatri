#recordar especificar la ruta dependiendo en que directorio se encuentra el archivo
archivo = open('prueba.txt','r',encoding='utf8') # 'r' read modo para leer
#archivo = open('prueba.txt','a',encoding='utf8')  'a' append modo para anexar
#archivo = open('prueba.txt','r',encoding='utf8')  'r' read modo para leer
#archivo = open('prueba.txt','x',encoding='utf8')  'x' crea un archivo
#archivo = open('prueba.txt','t',encoding='utf8')  't' crea un archivo texto
#archivo = open('prueba.txt','b',encoding='utf8')  'x' crea un archivos binarios
#archivo = open('prueba.txt','w+',encoding='utf8')  'w+' escribir y leer info.
#archivo = open('prueba.txt','r+',encoding='utf8')  'r+' leer y escribir info.

#print(archivo.read(8)) #nos muestra las 8 primeras letras de la palabra
#print(archivo.read(7)) #continua despues de las 8 que ya leó

print(archivo.readline()) #lee la primera linea
