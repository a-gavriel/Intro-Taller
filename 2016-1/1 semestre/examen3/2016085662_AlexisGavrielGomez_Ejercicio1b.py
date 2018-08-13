#
#
"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.1
Fecha Ultima modificación: 5 Junio

Entradas:
Para a_mas_bc15(A,B,C): 2 Matrices con numeros en base8 y [] 
Para a_masbc15(A,B): 2 Matrices (la funcion agrega el C )
Restricciones: listas de listas que no son matrices , numeros no en base8, C no []
Salidas: suma de las matrices en base8
****************************
"""
#
#
def a_masbc15(A,B):
    return a_mas_bc15(A,B,[])


def a_mas_bc15(A,B,C):
    return suma(A,B,len(A),len(A[0]),0,0,[],C)



def suma(A,B,n,m,i,j,Vect,C):
    if i==n:
        return C
    elif j==m:
        C.append(Vect)
        return suma(A,B,n,m,i+1,0,[],C)
    else:
        Num10 = N8_10(A[i][j] ) + N8_10(B[i][j])
        Num8 = N10_8(Num10)
        Vect.append(Num8)
        return suma(A,B,n,m,i,j+1,Vect,C)


def N8_10(A):
    N = abs(A)
    if A < 0:
        return -1*((8* (N//10)) + N%10)
    else:
        return (8* (N//10)) + N%10

def N10_8(A):
    N = abs(A)
    if A < 0:
        return -1*((N//8)*10 + (N%8) )
    else:
        return ((N//8)*10 + (N%8) )




       
