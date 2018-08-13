#
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

Entradas: 2 Matrices
Restricciones: listas de listas que no son matrices
Salidas: verificacion si las matrices son iguales y sus digitos estan en base8

****************************
"""
#
#
def ver(A,B):
    if len(A)==len(B) and len(A[0]) == len(B[0]):
        if val(A,len(A),len(A[0]),0,0):
            if val(B,len(B),len(B[0]),0,0):
                return 'Las matrices son del mismo tamaño y estan en base 8'
            else:
                return 'La matriz B debe estar en base 8'
        else:
            return 'La matriz A debe estar en base 8'
    else:
        return 'Las matrics no son del mismo tamaño'


def val(Matriz,n,m,i,j):
    if i==n:
        return 'Las matrices son iguales y sus numeros estan en base8'
    elif j==m:
        return val(Matriz,n,m,i+1,0)
    elif base8(abs(Matriz[i][j])): #se cambio la forma de verificar si el numero esta en base8
        return val(Matriz,n,m,i,j+1)
    else:
        return False

#se agrego una funcion para la determinacion de si un numero esta en base8
def base8(N):
    N = str(N)
    if N == '':
        return True
    elif N[0] == '1':
        return base8(N[1:])
    elif N[0] == '2':
        return base8(N[1:])
    elif N[0] == '3':
        return base8(N[1:])
    elif N[0] == '4':
        return base8(N[1:])
    elif N[0] == '5':
        return base8(N[1:])
    elif N[0] == '6':
        return base8(N[1:])
    elif N[0] == '7':
        return base8(N[1:])
    elif N[0] == '0':
        return base8(N[1:])
    else:
        return False
    
    
