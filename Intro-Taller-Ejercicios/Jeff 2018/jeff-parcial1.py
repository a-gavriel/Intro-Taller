# Introducción a la Programación
# I examen parcial - i semestre 2018
# Realizado por: Jeff Schmidt Peralta
########################################
# 1.
# función que recibe 2 listas y forma una nuevo con los números de la primera lista que
# no están contenidos en la segunda lista y los numeros de la segunda lista que no estan
# contenidos en la primera
# E: 2 listas
# S: lista con la diferencia de conjuntos
# R: listas válidas

def diferencia(lista1, lista2):
    if isinstance(lista1, list) and isinstance(lista2, list):
        return diferencia_aux(lista1, lista2) + diferencia_aux(lista2, lista1)
    else:
        return "Error"

def diferencia_aux(lista1, lista2):
    if lista1 == []:
        return []
    elif not pertenece(lista1[0], lista2):
        return [lista1[0]] + diferencia_aux(lista1[1:], lista2)
    else:
        return diferencia_aux(lista1[1:], lista2)

def pertenece(num, lista):
    if lista == []:
        return False
    elif num == lista[0]:
        return True
    else:
        return pertenece(num, lista[1:])

##################################
# 2.
# función que suma los elementos de una lista elevandolos a una potencia,
# incluyendo las sublistas
# E: lista
# S: cantidad de elementos incluyendo las sublistas
# R: lista valida

def suma(lista):
    if isinstance(lista, list):
        return suma_aux(aplanar(lista), 1)
    else:
        return "Error"

def aplanar(lista):
    if lista == []:
        return []
    elif isinstance(lista[0], list):
        return aplanar(lista[0]) + aplanar(lista[1:])
    else:
        return [lista[0]] + aplanar(lista[1:])

def suma_aux(lista, i):
    if lista == []:
        return 0
    else:
        return lista[0] ** i + suma_aux(lista[1:], i + 1)

##################################
# 3.
# función que obtiene el digito menor de un numero
# E: numero
# S: digito menor
# R: numero entero

def menor(num):
    if isinstance(num, int):
        return menor_aux(abs(num))
    else:
        return 'Error'

def menor_aux(num):
    if num < 10:
        return num
    else:
        return compara(num % 10, menor(num // 10))

def compara(dig1, dig2):
    if dig1 < dig2:
        return dig1
    else:
        return dig2

##################################
# 4.
# función que recibe un numero y forma una tupla con los digitos en posicion par e impar
# E: número
# S: (numero con digitos en posicion par, numero con digitos en posicion impar)
# R: Numero entero

def separa(num):
    if isinstance(num,int) and num // 10 != 0:
        num = abs(num)
        return separa_aux(num, 0), separa_aux(num//10, 0)
    else:
        return "Error"

def separa_aux(num, exp):
    if num == 0:
        return 0
    else:
        return (num%10) * 10 ** exp + separa_aux(num//100, exp + 1)
