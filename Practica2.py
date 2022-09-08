#Tema Listas
#Fecha 29/08/2022
#Montserrat Valdovinos Ochoa
#
# lista = ['Raul', 'Juan', 'Jose', 'Pedro', 'Laura']
# print(lista[1])
#
# for x in range(5):
#     print(lista[x])
#
# print("Longitud de la lista: " + str(len(lista)))
#
# #Partes de la lista
# print(lista[0:2])
#
# print(lista[ : 2])
# print(lista[2:4])
# print(lista[-1])
#
# #listas [inicio_fin]
#
# print(lista[-5 : -3])
#
# lista.insert(1,'Montse')
# print(lista)
#
# lista.remove('Montse')
# print(lista)
# #Ecepciones
# print(lista.index('Pedro'))
#
# lista.insert(4, 'Juan')
# print(lista)
#
# print(lista.count('Juan'))
#
# #Invertir lista
# lista.reverse()
# print(lista)




#Generar una lista con los primeros 5 numeros

lista=[i for i in range(5)]
print(lista)
#Generar una lista con elementos aleatorios del 1-100

import random
lista=[random.randint(1,100) for i in range(10)]
print(lista)

