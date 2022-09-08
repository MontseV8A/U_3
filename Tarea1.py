#Leer un archivo de texto que contenga numero de control y nombre

ruta='/Users/best buy/Desktop/Estudiantes.txt'
archivo = open(ruta, 'r')
#print(archivo.read())
#print(archivo.readline())
print(archivo.readlines())
archivo.close()

contenido="18420076,Alejandro"
nueva_ruta='/Users/best buy/Desktop/Archivo1.txt'
archivo=open(nueva_ruta,'r+')
archivo.write(contenido)
archivo.seek(0)
print(archivo.read())
archivo.close()
#for linea in archivo.readlines():
     #print(linea)