"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 16 Junio

Entradas: matriz que contiene valores binarios de los cuales hay un UNICO 0 y una lista vacia
Restricciones: matriz no contiene los valores especificados
Salidas: matriz donde los valores que esten en la misma columna o fila del valor 0, son cambiados por 0

****************************
"""


def proy_obj(mat2,mat3):
    v = []
    pos = LF(mat2,0)
    for a in range(len(mat2)):
        for b in range(len(mat2[0])):
            if a == pos[0]:
                v.append(0)
            elif b ==pos[1]:
                v.append(0)
            else:
                v.append(1) #se cambio por pass
        mat3.append(v)
        v = []
    return mat3


def LF(mat,x):
    for a in range(len(mat)):
        for b in range(len(mat[0])):
            if mat[a][b] == x:
                return a,b
            else:
                pass
    return False
    
