#31/08/2022
#Valdovinos Ochoa Montserrat
#
#
# #crear tuplas
# tupla1=tuple()
# tupla2=()
# tupla3=(2,'Jose Luis',True,4.5)
#
# #accesar a elementos de la tupla igual que a listas
#
# print(tupla3[1])
#
# for e in tupla3:
#     print(e)
# #Son inmutables
# #tupla3[1]='José Luis'
# grupo_a=('Jose Luis', 'Carmen', 'Estela')
# grupo_b=('Luis', 'Karina')
# grupo_c=(grupo_a, grupo_b)
# print(grupo_c)
#
# numeros=((3,4),(4,7),(7,98))
# # print(numeros)
#
#
# lista=['A','B','C','F']
# tupla_letras=tuple(lista)
# print(tupla_letras)
#
#
# alumno=(18420100,'Montserrat Valdovinos')
# control, nombre = alumno
# print("Control:", control, "Nombre: ", nombre)
#
# #Count(), cuenta el numero de elementos existentes en la tupla
# print(grupo_a.count('Luis'))
#Index() Regresa el kindice donde se ha encontrado tambien puede apsar el segundo
#es apartir de que posición quieres buscar
# lista=['A','B','C','F','G']
# tupla_letras=tuple(lista)
# print("Posición: ",tupla_letras.index('G',1))
'''
# Tema: Tuplas
# Fecha: 31 de agosto del 2022
# Autor: Leonardo Martínez González
'''
# 1. Definición. Es una colección de elementos inmutables.
#             Las tuplas son immutables y normalmente contienen una secuencia heterogénea
#             de elementos que son accedidos al desempaquetar o indizar.

# 2. Crear tuplas


# 3. Accesar a elementos de la tupla, igual que en las listas


# 4. Operaciones.
# 4.A. Son inmutables


# 4.B. Las tuplas pueden ser anidadas


# 4.C. Las listas se pueden convertir en tuplas  haciendo uso de la función tuple()


# 4.D. Se puede asignar el valor de una tupla con n elementos a n variables


# 5. Métodos de tuplas


# index() Regresa el índice donde se ha encontrado, tambien puede pasarle un segundo


'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
con la siguiente forma:
(nombre, clave, destino)
Ejemplo:
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el estado al que pertencen.
Ejemplo:
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de pasajeros
- Agregar ciudades a la lista de ciudades
- Dada la CLAVE de un pasajero, ver a que ciudad viaja
- Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
- Dada la CLAVE de un pasajero, ver a que ESTADO viaja
- Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
- Salir del programa

NOTA: Haga uso de funciones
'''
#MENU INTERACTIVO
from Funciones_Practica4 import*

pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

def menu_principal():
    while True:
        print("----------Menu principal-----------")
        print("1. Agregar pasajero")
        print("2. Agregar ciudad")
        print("3. Ciudad a la que viaja un pasajero")
        print("4. Cantidad de pasajeros que viajan a la ciudad:")
        print("5. A que estado viaja el pasajero")
        print("6. Cantidad de pasajeros que viajan a un estado ")
        print("7. Salir")

        opc=int(input("Elige una opción: "))
        #Evaluar la variable opción1

        if opc ==1:
            print("Agregar pasajero: ")
            agregar_pasajeros(pasajeros)
            print(pasajeros)
        elif opc==2:
            print("Agregar ciudad: ")
            agregar_ciudades(ciudades)
            print(ciudades)
        elif opc==3:
            print("Ciudad a la que viaja el pasajero: ")
            clave=int(input("Dame la clave del pasajero: "))
            ciudad=buscar_ciudad(clave,pasajeros)
            print("El pasajero: ", clave, "viaja a la ciudad de: ", ciudad)
        elif opc==4:
            print("Cantidad de pasajeros que viajan a una ciudad")
            ciudad=input("Dame la ciudad: ")
            print("La cantidad de pasajeros que viajan  a la ciudad: ", ciudad, "son: ", contar_pasajeros(ciudad, pasajeros))
        elif opc==5:
            print("Estado al que viaja un pasajero")
            clave=input("Dame la clave el usuario: ")
            print("El pasajero: ", clave, "viaja al estado: ", regresa_estado(clave, pasajeros, ciudades))
        elif opc==6:
            pass
        elif opc==7:
            break
        else:
            print("Opción no valida")
#Mandar llamar el menú principal
menu_principal()
