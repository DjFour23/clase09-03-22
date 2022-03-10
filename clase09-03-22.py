# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 18:50:21 2022

@author: dbenavid5
"""

#tabla del and
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False
print("--------------------------")

#tabla del or
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False
print("--------------------------")

#Negación
print(not True) #False
print(not False) #True
print("--------------------------")

#Jerarquía de Operaciones 
# 1. Parentesis y llaves
# 2. Potencias y Raices
# 3. Multiplicación y División
# 4. Sumas y Restas

print(True and False and True or False or True or True)
print(True and(False and True)or False or (True or True))
print("--------------------------")
#Estructura if 
x= 6
if(x > 0):
    print('1')
else:
    print('2')    
print('3')

if x > 0 :
    print('Mayor que cero')
elif x == 0:
    print('Es igual a cero')
else:
    print('despedido')
    

#HAU que dada la edad de una persona indique si es mayor o menor de edad

edad = int(input('ingrese la edad: \n'))

if edad >= 18:
    print('La persona es mayor de edad')
elif edad < 0: 
        print('Edad invalida')
else: 
    print('La persona es menor de edad')
    

#HAU que identifique si un estudiante aprobo o reprobo la asignatura teniendo 
#en cuenta que se aprueba min con 3.0
nota = float(input('ingrese la nota: \n'))
if(nota >= 3):
    print(f'Aprobó la asignatura con una nota {nota}.')
else:
    print(f'Reprobó la asignatura con una nota {nota}.')


#HAU que identifique si un estudiante aprobo o reprobo la asignatura teniendo 
#en cuenta que se aprueba min con 3.0, validado que sea nota valida
nota = float(input('ingrese la nota: \n'))
if nota < 0 or nota >5: 
        print('nota invalida')
elif(nota >= 3):
    print(f'Aprobó la asignatura con una nota {nota}.')
else:
    print(f'Reprobó la asignatura con una nota {nota}.')


#HUA que dado un número n diga si es negativo, positivo o cero
n = float(input('ingrese el num: \n'))
if n> 0: 
    print('Es positivo')
elif n == 0: 
    print('Es cero')
else:
    print('Es negativo')
    
# Ciclos en python

# For

# Range 

# Iterador Flojo

for valor in range(4):
    print(valor)

for valor in range(1, 6):
    print(valor)
    
for valor in range(1, 100, 2):
    print(valor)

for i in range(1, 11):
    for j in range(1, 6):
        print(i,j)

# While

while True:
    print('Hola Mundo')

# HUA que de las n notas de un estudiante calcule el promedio
# académico final
notas = 0
numero_notas = int(input('Digite el número de notas del estudiante: '))
for i in range(1, numero_notas + 1):
    while True:
        nota = float(input(f'Digite la nota número {i}: '))
        if nota <5 and nota > 0:
            break
    notas = notas + nota
prom = notas /numero_notas
prom = round(prom, 2)
print(f'El promedio académico final de las {numero_notas} notas es: {prom} ')

#Pos quedo incompleto porque ya vpy a apagar xd
