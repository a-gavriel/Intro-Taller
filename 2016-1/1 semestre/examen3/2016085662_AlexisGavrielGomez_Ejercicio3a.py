#
"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 27 mayo

Entradas: numero entre 1 y 2000
Restricciones: numeros no enteros
Salidas: lista de numeros hexadecimales en el archivo

****************************
"""
import random
def num(N):
    if 1<N<2001 and isinstance(N,int):
        return minum(N)
    else:
        return 'Debe ingresar un numero entero entre 1 y 2000'

def random():
    a = int(random.uniform(0,16))
    if a == 10:
        return 'A\n'
    elif a ==11:
        return 'B\n'
    elif a==12:
        return 'C\n'
    elif a==13:
        return 'D\n'
    elif a== 14:
        return 'E\n'
    elif a==15:
        return 'F\n'
    elif 0>= a >=9:
        return str (a) + '\n'

def minum(N):
    if 1<N:
        return
    else:
        arc = open ('MiNumerito0.txt','r+')
        a.readlines()
        arc.write(random())
        arc.close()

