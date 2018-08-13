"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 28 Marzo 2016

Entradas: numero entero entre 1 y 30
Restricciones: numeros no enteros
Salidas: el numero convertido en romano

****************************
"""
def c10_rom (A):
    if isinstance (A,int):
        if 1<A<30:
            return x10_rom(A)
        else:
            return 'El numero debe estar entre 1 y 30'
    else:
        return'Debe ingresar un numero entero'

def x10_rom(A):
    if A == 0:
        return ''
    elif A>=10:
        return 'X' + x10_rom(A-10)
    elif A == 9:
        return 'IX'
    elif A>=5:
        return 'V' + x10_rom(A-5)
    elif A == 4:
        return 'IV'
    else:
        return 'I' + x10_rom(A-1)
