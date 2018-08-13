"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 16 Junio

Entradas: dos matrice de igual tamaño que contienen numeros enteros
Restricciones: matrices con valores distintos de los especificados
Salidas: suma de las matrices

****************************
"""


def suma(mat1,mat2):
    return sumax(mat1,mat2,[])

def sumax(mat1,mat2, R):
    if len(mat1)==(len(mat2)):
        if len(mat1[0]) == len(mat2[0]):
            return suma_aux(mat1,mat2,[])
        else:
            return 'tamaños  de matrices distintos'
    else:
            return 'tamaños  de matrices distintos'

def suma_aux(mat1,mat2,R):
    v = []
    for a in range(len(mat1)):
        for b in range(len(mat1[0])):
            if isinstance(mat1[a][b],int): #se agrego [a][b] al final de mat1
                if isinstance(mat2[a][b],int):   #se agrego [a][b] al final de mat2
                    v.append(mat1[a][b] + mat2[a][b])
                else:
                    return 'Error, numero no entero en matriz 2'
            else:
                    return 'Error, numero no entero en matriz 1'
        R.append(v)
        v=[]
    return R
