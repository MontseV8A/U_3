#Insertar pasajero

def agregar_pasajeros(pasajeros):
    clave = int(input("Dame la clave del pasajero: "))
    nombre=input("Dame el nombre del pasajero:")
    ciudad=input("Dame el nombre de la ciudad:")
    pasajeros.appened((nombre,clave,ciudad))
#insertar ciudades

def agregar_ciudades(ciudades):
    ciudad=input("Dame la ciudad: ")
    estado=input("Dame el estado: ")
    ciudades.appened((ciudad,estado))

def buscar_ciudad(clave,pasajeros):
    for pasajero in pasajeros:
        if pasajero in pasajeros:
            return pasajero[2]
    return "No existe"

def contar_pasajeros(ciudad, pasajeros):
    contador=0
    for pasajero in pasajeros:
        if pasajero[2]== ciudad:
            contador +=1
    return contador
#regresa el estado al que viaja un pasajero
def regresa_estado(clave, pasajeros, ciudades):
    for p in pasajeros:
        if p[1]==clave:
            for c in ciudades:
                if c[0]== p[2]:
                    return c[1]
    return "No existe"