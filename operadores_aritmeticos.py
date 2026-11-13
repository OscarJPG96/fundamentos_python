#----OPERADORES ARITMETICOS------

a = 10
b = 3

#--suma--
suma = a + b
print(f"la suma entre {a} y {b} es: {suma}")

#-- resta---
resta = a - b
print(f"la resta entre {a} y {b} es: {resta}")

#--- multiplicacion
multiplicacion = a * b
print(f"la multiplicacion entre {a} y {b} es: {multiplicacion}")

#--divicion- flotante o decimal--
divicion = a / b
print(f"la divicion entre {a} y {b} es: {divicion}")

#--divicon entera sin decimal---
divicion_entera = a // b
print(f"la dicicion entera entre {a} y {b} es: {divicion_entera}")


#modulo o residuo
modulo = a % b
print(f"el resultado del modulo entre {a} y {b} es: {modulo}")

#exponenciacion o potencia

exponente = a ** b
print(f"la exponencia entre {a} elevado a {b} es: {exponente}")


# ---PRECEDENCIA DE OPERADORES----

resultado = a + b * 2
print(f"el resultado de la operacion es : {resultado}") #16

resultado_2 = (10 + 3) *2
print(f"el resultado de la operacion es: {resultado_2} ") #26

resultado_3 = 10 * 3 // 3
print(f"el resultado es {resultado_3}") #10

ejercicio = ((a + b) * (a -b) / (a * b)) - ((a ** b) %3)
print (f"el resultado es {ejercicio}") #2.033333333

#---LIBRERIAS EN PY----
import math

print(math.pi)

print(math.e)

print(math.sqrt(16))

import random

print(random.random())



