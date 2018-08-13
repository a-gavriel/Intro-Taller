"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 12 Abril

Entradas: Numero Entero
Restricciones: Numeros negativos
Salidas: Si es un palindromo

****************************
"""



def palin(Num):
    if val(Num):
        if palin_aux(str(Num)):
            return True
        else:
            return False
    else:
        return 'Valor de entrada inválido'

def val(A):
    if isinstance (A,int) and A>=0:
        return True
    else:
        return False

def palin_aux(X):
    if X == '':
        return True
    elif X[0]==X[-1]:
        return palin_aux(X[1:-1])
    else:
        return False
