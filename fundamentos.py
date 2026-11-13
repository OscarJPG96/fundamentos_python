print("hola mundo")

# tipo de escritura de las variables --------------

#camelCase
aprendizSena = "sena"

#pascalCase
AprendizSena ="sena"

#snake_case es que utilizaremos
aprendiz_sena ="sena"

#REGLAS DE LAS VARIABLES:
# 2026anio = "ANIO ACTUAL"

nombre_completo = "oscar perez"

#--------------TIPOS DE DATOS PRIMITIVOS------------
nombre = "oscar"
print(type(nombre)) #str

edad =29
print(type(edad)) #int

altura =1.69
print(type(altura)) #float

activo =True
print(type(activo)) #bool

complejo = 2 +3j
print(type(complejo)) #complex

byte = b"hola"
print(type(byte)) #byte

nulo     = None
print(type(nulo)) #nonetype

#------TIPOS DE DATOS ESTRUCTURAS---------

lista =["python, javascript"]
print(type(lista)) #list

conjunto ={"html","css"}
print(type(conjunto)) #set

tupla =("java", "c#")
print(type(tupla)) #tuple

diccionario ={"nombre": "javier", "edad": 32}
print(type(diccionario)) #dict

rango = range(5)
print(type(rango)) #range

#-----CONVERCION DE TIPOS DE DATOS O CASTEO--------

# -- casteo de entero -> texto

telefono = 3203885572
print(type(telefono), telefono) #int
telefono_str = str(telefono)
print(type(telefono_str), telefono_str) #str


#casteo de texto -> entero
cedula = "1053513158"
print(type(cedula), cedula) #str


cedula_int = int(cedula)
print(type(cedula_int), cedula_int) #int

#casto de bool -> int
matriculado = False
print(type(matriculado), matriculado) #bool

matriculado_int = int(matriculado)
print(type(matriculado_int), matriculado_int) #int

#casteo float -> int
promedio = 4.13
print(type(promedio), promedio) #float

promedio_int =int(promedio)
print(type(promedio_int),promedio_int) #int


#casteo de int -> float
edadd =32
print(type(edadd), edad)

edadd_float = float(edadd)
print(type(edadd_float), edadd_float)

#casteo de entero ->booleano
activo = 0
print(type(activo), activo) #int

activo_bool = bool(activo) 
print(type(activo_bool),activo_bool) #bool


#casteo de booleano -> decimal

beneficio =True
print(type(beneficio), beneficio) #bool

beneficio_float = float(beneficio)
print(type(beneficio_float), beneficio_float) #float


# casteo decimal -> bool
descuento = 10.5
print(type(descuento), descuento) #float

descuento_bool = bool(descuento)
print(type(descuento_bool), descuento_bool) #bool

# este es un comentario de una sola linea

"""este es un comentario
de varias lineas que se utiliza para explicar
el codigo de manera mas detallada"""


#identacion en python

#con un condicional if

if 5 > 2:
    print("5 es mayor que 2")  
else:
    print("5 no es mayor que 2")


#----INPUT : ENTRADAS DE DATOS

nombre_completo =input("ingresa tu nombre completo: ")
programa =input("cual es tu programa de formacion? ")

#OUTPUT : SALIDA DE DATOS

print("hola " + nombre_completo + " bienbenido al curso de python")
print("hola", nombre_completo, "bienvenido al curso de python")

print("hola mi nombre es: ", nombre_completo, " estoy en el programa de:", programa)

#impresion con formato f-string
print(f"hola mi nombre es: {nombre_completo}, y estoy en el programa de: {programa}")













