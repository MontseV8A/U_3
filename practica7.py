'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 06 de septiembre del 2022
Autor: Montserrat Valdovinos Ochoa
Continuación de la práctica 6 //Use sus metodos para que saliera bien :c
'''
import bcrypt

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes. (5) 10 min.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . . 
        ],
        "Promedio general": 98.4
   }

4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"}, 
    {"Nombre": "Base de datos distribuidas"}, 
    {"Nombre": "Finanzas internacionales IV"}, 
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"}, 
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]


5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Cifrar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4

   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada

6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }

   ó

   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }

   ó

    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }


'''
import json
import random


# 1.
def regresa_conjunto_estudiantes():
    estudiantes = set()
    tupla_estudiante = ()
    with open("estudiantes.prn") as arch_estudiantes:
        for linea in arch_estudiantes:
            control = linea[0:8]
            nombre = linea[8:-1]
            estudiantes.add((control,nombre))
    # Cerrar el archivo
    arch_estudiantes.close()
    return estudiantes

# 2.
def regresa_conjunto_promedios():
    promedios_materias = set()
    with open("kardex.txt") as kardex:
        for linea in kardex:
            control = linea.split("|")[0]
            materia = linea.split("|")[1]
            promedio = linea.split("|")[2][:-1]  # el -1 para no incluir el último caracter
            promedios_materias.add((control,materia,promedio))
    # Cerrar el archivo
    kardex.close()
    return promedios_materias

# 3.
def regresa_datos(ctrl):
    estudiantes = regresa_conjunto_estudiantes()
    promedios = regresa_conjunto_promedios()
    datos = dict() # Creamos el diccionario
    lista_materias = []
    nombre = ""
    promedio = 0.0
    for alu in estudiantes:
        if ctrl == alu[0]:
            nombre = alu[1]
            promedio_acumulado = 0 # Para acumular los promedios
            numero_materias = 0 # Para contar el número de materias.
            for mat in promedios:
                if ctrl == mat[0]:
                    materia = {}
                    materia["Nombre"] = mat[1]
                    materia["Promedio"] = int(mat[2])
                    lista_materias.append(materia)
                    promedio_acumulado += int(mat[2])
                    numero_materias += 1
            promedio = promedio_acumulado / numero_materias

    # Ya se puede formar el JSON
    datos["Nombre"] = nombre
    datos["Materias"] = lista_materias
    datos["Promedio General"] = promedio
    return json.dumps(datos) # regresar el JSON

# print(regresa_datos('18420430'))

#4. Lista de materias
def regresa_materias_por_estudiante(ctrl):
    promedios = regresa_conjunto_promedios()
    lista_materias = []
    for mat in promedios:
        c,m,p = mat # Desestructurar la variable mat
        if ctrl == c:
            lista_materias.append({"Nombre":m})
    return json.dumps(lista_materias)

# print(regresa_materias_por_estudiante('18420428'))

# 5. A. Al menos una letra mayúscula
#    B. Al menos una letra minúscula
#    C. Numeros
#    D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

def generar_letra_mayuscula():  # Regresa una Letra desde la A .. Z
    return chr(random.randint(65,90))

def generar_letra_minuscula():  # Regresa una letra minuscula desde la a ...  z
    return chr(random.randint(97,122))

def generar_numeros():  # Regresa un numero aleatorio entre 0 .... 9
    return chr(random.randint(48,57))

def generar_caracter_especial():  # Regresa un caracter especial
    lista_caracteres = ['@', '#', '$','%','&','_','?','!']
    return lista_caracteres[random.randint(0,7)]

def generar_contrasena():
    clave = ""
    for i in range(0,10):
        numero = random.randint(1,5)
        if numero == 1:
            clave = clave + generar_letra_mayuscula()
        elif numero == 2:
            clave = clave + generar_letra_minuscula()
        elif numero == 3:
            clave = clave + generar_caracter_especial()
        elif numero >= 4 and numero <= 5:
            clave = clave + generar_numeros()
    # Regresar la contraseña
    return clave

# print(generar_contrasena())

# Cifrar las contraseñas con bcrypt
def cifrar_contrasena(contrasena):
    sal = bcrypt.gensalt() # Default tiene de 12
    contrasena_cifrada = bcrypt.hashpw(contrasena.encode('utf-8'), sal)
    return contrasena_cifrada

# clave = generar_contrasena()
# print(clave,cifrar_contrasena(clave))

#print(bcrypt.checkpw("_@3S8&@3TK".encode('utf-8'),"$2b$12$2CJJaULDzRi51zw2K8e3yeT5zLWz0tOrNE0e5f2nk3q5RzX6Rl6YG".encode('utf-8')))

# Generar el archivo de usuarios:
def generar_archivo_usuarios():
    #Obtener la lista de estudiantes
    estudiantes = regresa_conjunto_estudiantes()
    usuarios = open("usuarios.txt", "w")
    contador = 1
    for est in estudiantes:
        c,n = est
        clave = generar_contrasena()
        clave_cifrada = cifrar_contrasena(clave)
        registro = c +"|" + n + "|" + clave + "|" + str(clave_cifrada, 'utf-8') + "\n"
        usuarios.write(registro)
        contador += 1
        print(contador)
    print("Archivo generado")


#generar_archivo_usuarios()

def verificar_contraseña(us, psw):
    res={}
    if us!=" ":
        archivo=open("usuarios.txt", 'r')
        usu=archivo.read().split("\n")

        for al in usu:
            info=al.split("|")
            if len(info)>0:
                if info[0] == us:
                    pswn=psw.encode('utf-8')
                    pswe=info[3].encode('utf-8')
                    iguales=bcrypt.checkpw(pswn,pswe)
                    if iguales == True:
                        res={"Bandera" : True, "Usuario" :  info[1],"Mensaje" : "Datos correctos bienvenido"}
                    else:
                        res={"Bandera" : False, "Mensaje": "Datos incorrectos para el usuario", "Usuario": info[1]}

                    break
    if len(res)==0:
        res={"Bandera": False, "Usuario: ": "", "Mensaje" : "Usuario inexistente"}
    print(res)

verificar_contraseña("18420485","V6!722v5U1")