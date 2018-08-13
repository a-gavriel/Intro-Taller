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

Entradas: ninguna
Restricciones: debe existir el archivo para escribir
Salidas: numeros hexadecimales ordenados por burbuja

****************************
"""
#
#
import time
from timeit import timeit
def burbuja():
    arc = open ('MiNumerito0.txt','r')
    bub = open ('MiNumerito0R.txt','r+')
    a = arc.readlines()
    b = cor(a,[])
    c = burbujax(b)
    camb_burb(c)
    
def cambio(a):
    if a == 10:
        ar = open ('MiNumerito0R.txt','r+')
        ar.write( 'A\n')
        ar.close()
    elif a ==11:
        ar = open ('MiNumerito0R.txt','r+')
        ar.write( 'B\n')
        ar.close()
    elif a==12:
        ar = open ('MiNumerito0R.txt','r+')
        ar.write( 'C\n')
        ar.close()
    elif a==13:
        ar = open ('MiNumerito0R.txt','r+')
        ar.write( 'D\n')
        ar.close()
    elif a== 14:
        ar = open ('MiNumerito0R.txt','r+')
        ar.write( 'E\n')
        ar.close()
    elif a==15:
        ar = open ('MiNumerito0R.txt','r+')
        ar.write( 'F\n')
        ar.close()
    elif 0>= a >=9:
        ar = open ('MiNumerito0R.txt','r+')
        ar.write( str (a) + '\n')
        ar.close()
        
def camb_burb(N):
    if N==[]:
        return True
    else:
        cambio(N[0])
        return camb_burb(N[1:])


def cor(N,R):
    if N == []:
        return R
    else:
        a = N[0]
        b = a[-1]
        if b == 'A':
            R.append(10)
            return cor(N[1:],R)
        elif b == 'B':
            R.append(11)
            return cor(N[1:],R)
        elif b == 'C':
            R.append(12)
            return cor(N[1:],R)
        elif b == 'D':
            R.append(13)
            return cor(N[1:],R)
        elif b == 'E':
            R.append(14)
            return cor(N[1:],R)
        elif b == 'F':
            R.append(15)
            return cor(N[1:],R)
        elif 0>= int(b)>=9:
            R.append(int(b))
            return cor(N[1:],R)
        else:
            None


def burbujax(lista):
    return burbuja_aux(lista, 0, 0, len(lista), False)

def burbuja_aux(lista, i, j, n, swap):
    if i == n:
        return lista
    elif j == n - i - 1:
        if swap:
            return burbuja_aux(lista, i + 1, 0, n, False)
        else:
            return lista
    elif lista[j] > lista[j + 1]:
        tmp = lista[j]
        lista[j] = lista[j + 1]
        lista[j + 1] = tmp
        return burbuja_aux(lista, i, j + 1, n, True)
    else:
        return burbuja_aux(lista, i, j + 1, n, swap)
