"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 30 Marzo 2016

Entradas: Numero entero
Restricciones: Numero no entero
Salidas: tupla con cantidad de digitos mayores o iguales  a 7 y menores a 7

****************************
"""


def digitos(X):
    if val(X):
        return xfn7(X,0,0)
    else:
        return 'Debe ingresar un numero entero'

def val(X):
    if isinstance (X,int):
        return True
    else:
        return False


def xfn7(x,a,b):
    if x == 0:
        return (cont(a),cont(b))
    elif x %10 <7:
        return xfn7 (x//10,a,b*10 + x%10)
    else:
        return xfn7 (x//10,a*10 + x%10,b)

def cont(n):
    if n == 0:
        return 0
    else:
        return 1 + cont(n//10)
