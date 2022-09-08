'''
Tema: conjuntos
Fecha: 05 de septiembre del 2022
Autor: Montserrat Valdovinos Ochoa
'''

# 1. Definición. en Python es utilizado para trabajar con conjuntos de elementos.
#    La principal característica de este tipo de datos es que es una colección cuyos elementos
#    no guardan ningún orden y que además son únicos.
#    los principales usos de esta clase se usan para conocer si un elemento pertenece o no
#    a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).


# 2. Creación. Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {},
#    o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable
#    (como una lista, una tupla, una cadena …).

# conjunto1 = {1,2,3,4,5}
# conjunto2 = set([i for i in range(0,11,2)])
# conjunto3=set()
# print(conjunto1,conjunto2, conjunto3)
#no guarda valores duplicados




#    Usando la función frozenset. es inmutable y su contenido no puede ser modificado
#    una vez que ha sido inicializado
# c4=frozenset({letra for letra in range(65,90)})
# print(c4)
#    Los elementos repetidos se eliminan


# 3. Para acceder a los elementos de un conjunto. Dado que los conjuntos son colecciones
#    desordenadas, en ellos no se guarda la posición en la que son insertados los elementos
#    como ocurre en los tipos list o tuple. Es por ello que no se puede acceder a los elementos
#    a través de un índice.



# 4. Añadir elementos: con el método add() ó con el método update()
#    Agregar el numero 8 al conjunto c
# conjunto1.add(10)
# print(conjunto1)
# conjunto1.update({20,80,50})
# conjunto1.update([35,69,87])
# print(conjunto1)
#    Agregar varios elementos al conjunto


# 5. Eliminar elementos del conjunto: discard(elemento), remove(elemento), pop() y clear()
#    discard(elemento) y remove(elemento) son muy parecidos, solo que remove lanza una excepcion KeyError
#    en caso de no existir el elemento

# print(conjunto1)
# conjunto1.discard(10)
# conjunto1.discard(100) #no lanza la excepción pero funciona de la misma manera
# #conjunto1.remove(100) lanza la excepción
# print(conjunto1)

#     pop() devuelve un elemento aleatorio y lo elimina, si el conjunto esta vacio lanza una
#     excepcion KeyError.

# conjunto1.pop() #elimina aleatorio
# print(conjunto1)

#    El método clear() elimina todos los elementos del conjunto

#conjunto1.clear()

#print(conjunto1)
#    Número de elementos en un conlunto con la función len()
# print("Número de elementos del conjunto: ", len(conjunto1))
#
# #    Verificar si un elemento esta dentro de un conjunto
# print(80 in conjunto1)


# ************************ Operaciones con conjuntos
# 1. Union  ( | )

# c1={i for i in range(1,21,2)}
# c2={ i for i in range(2,22,2)}
# print(c1)
# print(c2)
# print(c1 | c2)
# # 2. Intersección ( & )
# print(c1 & c2)
# c1.update([2,4,6,8,10])
# print(c1)
# print(c1 & c2)
# 3. Diferencia ( - )

#print(c1)
#print(c2)
#print(c1 - c2) #todo lo que esta en c1 pero no en c2
# 4. Diferencia simétrica ( ^ ). es el conjunto que contiene los elementos de A y B
#    que no son comunes.
#print(c1 ^ c2 )

# 5. Inclusión de conjuntos.  Se utiliza el operador <= para comprobar si un conjunto A
#    es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.
#c3={1,2,3,4,5,6,7}
#c4={1,2,3}
#print(c3 >= c4)
# 5. Conjuntos disjuntos. Dos conjuntos A y B son disjuntos si no tienen elementos en común,
#    es decir, la intersección de A y B es el conjunto vacío.


# 6. Igualdad de conjuntos. En Python dos conjuntos son iguales si y solo si todos los elementos
#    de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto
#    del otro.
#a1={1,3}
#a2={1,3}
#print(a1==a2)

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes. 
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"",
                "Promedio":
            },
            {
                "Nombre":"",
                "Promedio":
            },
            . . . 
        ],
        "Promedio general": 
   }


'''
#TAREA
#
# import json
# ruta='/Users/best buy/Desktop/Estudiantes.txt'
# archivo=open(ruta, 'r')
# # print(archivo.read())
# estudiantes= archivo.read().split("\n")
# estudiante2 = []
# for est in estudiantes:
#     estudiante2.append((est[0:8],est[8: ]))
#
# print(set(estudiante2))
# archivo.close()
#
# ruta = '/Users/best buy/Desktop/Kardex.txt'
# archivo = open(ruta, 'r')
#
#
# mater = archivo.read().split("\n")
# materias = []
# for mat in mater:
#     if len(mat) > 0:
#         info = mat.split("|")
#         materias.append((info[0], info[1], info[2]))
# print(set(materias))
#
#
#
# ruta = '/Users/best buy/Desktop/Kardex.txt'
# ruta2='/Users/best buy/Desktop/Kardex.json'
# archivo = open(ruta,'r')
# mJson = open(ruta2, 'r+')
# nc=input("Dame un numero de control: ")
# estudiantes=[]
# informacion = {}
# materias1 = []
# promedio = 0
# for i in range(0, len(estudiantes)):
#     if estudiantes[i][0] == nc:
#         for j in range(0, len(materias)):
#             if materias[j][0] == nc:
#                 materias1.append({"Nombre": materias[j][1], "Promedio": materias[j][2]})
#                 promedio += int(materias[j][2])
#                 informacion = {"Nombre": estudiantes[i][1], "Materias": materias1, "Promedio General": (promedio / len(materias1))}
#
# json.dump(informacion, mJson)










