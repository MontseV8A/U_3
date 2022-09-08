# #Tema Listas
# #Fecha 29/08/2022
# #Montserrat Valdovinos Ochoa
#
#
# #Lista anidada de 5 elementos cada elemento debe tener numero de control, nombre y promedio
#
# lista=[
#     [18420100,"Montse",70],
#     [18420093,"Jorge",70],
#     [18420098,"Raul",80],
#     [18420087,"Armando",85],
#     [18420076,"Alejandro", 100]
#
# ]
# for li in lista:
#     print(li[-1])
# #crear una lista con los promedios con la lista anidada anterior
# prom=[]
# for li in lista:
#     prom.append((li[-1]))
# print(prom)
# #Crear lista por comprension de promedios:
# prom2=[li[-1] for li in lista]
# print(prom2)

#lista de estudiantes
#1. Menú principal: Insertar, Eliminar, Actualizar y Salir
#Si le das opcion no valida que diga que no es valida y no deje salirse del menú
lista=['Mon','José']
def buscar(nom):
    for li in lista:
        if(nom==li[1]):
            return True
    return False
print(buscar('Alejandra'))

def insertar():
    nom = input("Dame un nombre: ")
    print(nom)
    lista.append(nom)
print(insertar(),lista)

def eliminar():
    nom = input("Dame un nombre: ")
    print(nom)
    lista.remove(nom)
print(eliminar(), lista)

def actualizar():
    nom = input("Dame un nombre: ")
    print(nom)
    lista.update(nom)
print(eliminar(), lista)