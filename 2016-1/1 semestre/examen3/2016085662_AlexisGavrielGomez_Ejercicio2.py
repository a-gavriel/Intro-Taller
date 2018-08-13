#
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

Entradas: lista con enteros
Restricciones: ninguna
Salidas: valores de Euler obtenidos con sumatorias con es limite superior

****************************
"""
#
#

def e_vec(VecN):
    if VecN == []:
        return 'vector no deebe ser nulo'
    elif isinstance (VecN,list): #se intercambio el resultado de esta operacion booleana con el siguiente
        return e_aux(VecN,len(VecN),0,[])
    else:
        return 'vector debe ser una lista de numeros enteros'

def e_aux(lista,n,i,R):
    if n==i:
        return R
    else:
        R.append(c_e(0,lista[i],0))
        return e_aux(lista,n,i+1,R)

def fact(N,R):
    if N==0:
        return 1
    elif N==1:
        return R # se cambio 1 por R
    else:
        return fact(N-1,R*N)

def c_e(i,n,R):
    if i>n:
        return R
    else:
        return c_e(i+1,n,R+ (1/fact(i,1)))
