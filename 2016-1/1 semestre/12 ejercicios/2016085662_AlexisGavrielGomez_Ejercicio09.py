"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 28 Marzo 2016

Entradas: String con numero romanos
Restricciones: numeros no romanos
Salidas: Si la hilera contiene unicamente numeros romanos

****************************
"""
def valrom(A):
    if isinstance(A,str):
        return val2rom(A,0)
    else:
        return "Debe ingresar un String"

def val2rom(A,B):
    if len(A) == B:
        return True
    elif A[B] != 'I' and A[B] != 'V' and A[B] != 'X' :
        return 'El string debe contener unicamente "X" "V" "I" '
    else:
        return val2rom(A,B+1)
    
