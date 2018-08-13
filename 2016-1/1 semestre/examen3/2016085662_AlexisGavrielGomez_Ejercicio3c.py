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
Salidas: numeros hexadecimales ordenados por quick sort

****************************
"""
#
import time
from timeit import timeit
def burbuja():
    arc = open ('MiNumerito0.txt','r')
    qs = open ('MiNumerito0QS.txt','r+')
    a = arc.readlines()
    b = cor(a,[])
    c = quick_sort(b)
    camb(c)
    
def cambio(a):
    if a == 10:
        ar = open ('MiNumerito0QS.txt','r+')
        ar.write( 'A\n')
        ar.close()
    elif a ==11:
        ar = open ('MiNumerito0QS.txt','r+')
        ar.write( 'B\n')
        ar.close()
    elif a==12:
        ar = open ('MiNumerito0QS.txt','r+')
        ar.write( 'C\n')
        ar.close()
    elif a==13:
        ar = open ('MiNumerito0QS.txt','r+')
        ar.write( 'D\n')
        ar.close()
    elif a== 14:
        ar = open ('MiNumerito0QS.txt','r+')
        ar.write( 'E\n')
        ar.close()
    elif a==15:
        ar = open ('MiNumerito0QS.txt','r+')
        ar.write( 'F\n')
        ar.close()
    elif 0>= a >=9:
        ar = open ('MiNumerito0QS.txt','r+')
        ar.write( str (a) + '\n')
        ar.close()

        
def camb(N):
    if N==[]:
        return True
    else:
        cambio(N[0])
        return camb(N[1:])


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


def quick_sort(Lista):
    Menores = []
    Iguales = []
    Mayores = []
    if len(Lista) <= 1:
        return Lista
    Pivote = Lista[-1]
    partir(Lista, 0, len(Lista), Pivote, Menores, Iguales,Mayores)
    ret = quick_sort(Menores)
    ret.extend(Iguales)
    ret.extend(quick_sort(Mayores))
    return ret

def partir(Lista, i, n, Pivote, Menores, Iguales, Mayores):
    if i == n:
        return Menores, Iguales, Mayores
    if Lista[i] < Pivote:
        Menores.append(Lista[i])
    elif Lista[i] > Pivote:
        Mayores.append(Lista[i])
    elif Lista[i] == Pivote:
        Iguales.append(Lista[i])
    return partir(Lista, i + 1, n, Pivote, Menores, Iguales, Mayores)

