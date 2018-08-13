"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 30 Marzo 2016

Entradas: numero entero
Restricciones: numero no entero
Salidas: Lista de numeros en hexadecimal
Notas: se debe expandir el tamaño de la pila a 1200

****************************
"""

import random

def rdmhx(N):
    if isinstance (N,int):
        a=rdm(N)
        return rev(a)
    else:
        return 'Debe ingresar un numero entero'

def rdm(N):
    if N<1:
        return []
    else:
        return [int(random.uniform(0,16))] + rdm(N-1)

def hx(a):
    if a<10:
        return str(a)
    elif a==10:
        return 'A'
    elif a==11:
        return 'B'
    elif a==12:
        return 'C'
    elif a==13:
        return 'D'
    elif a==14:
        return 'E'
    elif a==15:
        return 'F'

def rev(a):
    if a==[]:
        return []
    else:
        return [hx(a[0])] + rev(a[1:])
