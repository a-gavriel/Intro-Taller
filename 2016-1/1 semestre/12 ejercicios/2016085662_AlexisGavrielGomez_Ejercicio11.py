"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 2.0
Fecha Ultima modificación: 28 Marzo 2016

Entradas: Dos numeros romanos entre 1 y 15
Restricciones: numeros no romanos
Salidas: Suma en decimal de los numeros

****************************
"""
def sum_rom(A,B):
    if val(A)==True:
        if val(B)==True:
            return suma(A,B)
        else:
            return 'Segundo valor invalido'
    else:
        return'Primer valor invalido'

def val(A):
    if valrom(A) ==True and val2rom(A,0)==True:
        return True
    else:
        return 'los valores deben ser romanos'

    
def valrom(A):
    if isinstance(A,str):
      return True
    else:
        return "Debe ingresar un String" 

def val2rom(A,B):
    if len(A) == B:
        return True
    elif A[B] != 'I' and A[B] != 'V' and A[B] != 'X' :
        return 'El string debe contener unicamente "X" "V" "I" '
    else:
        return val2rom(A,B+1)
    

def suma(A,B):
    suma10 = (crom_10(A)) + (crom_10(B))
    return suma10

def crom_10(A):
    if A == '':
        return 0
    elif A == 'IX':
        return 9
    elif A == 'IV':
        return 4
    elif A[0] == 'X':
        return 10 + crom_10(A[1:])
    elif A[0] == 'V':
        return 5 + crom_10(A[1:])
    else:
        return 1 + crom_10(A[1:])
    
