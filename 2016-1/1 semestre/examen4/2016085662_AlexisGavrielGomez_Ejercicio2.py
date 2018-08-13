"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 16 Junio

Entradas: dos matrices de igual tamaño y cuadradas con valores binarios.
La matriz 1 debe contener un unico 1, y la matriz 2 un unico 0 
Restricciones: matrices que contengan datos distintos a los especificados
Salidas: True si la posicion del 1 en la matriz 1 coincide con la posicion del 0 de la matriz 2
Nota: en caso de haber mas de un 1 en la matriz 1 o mas de un cero en la matriz 2 retornara:
'Aparce estela del objeto en matriz' sin especificar cual matriz contiene el error

****************************
"""

def val_neg(mat1,mat2):
    if len(mat1)==len(mat1[0]):
        if len(mat2)==len(mat2[0]):
            if len(mat1)==len(mat2):
                if val(mat1):
                    if val(mat2):
                        if val2(mat1,1) and val2(mat2,0):
                            if LF(mat1,1)==LF(mat2,0):
                                return True
                            else:
                                return False
                        else:
                            return 'Aparce estela del objeto en matriz'
                    else:
                        return 'Valores invalidos en matriz 2'
                else:
                    return 'Valores invalidos en matriz 1'
            else:
                return 'Matrices deben tener mismo tamaño'
        else:
            return "matriz 2 no cuadrada"
    else:
            return "matriz 1 no cuadrada"

def val(m):
    for a in range(len(m)):
        for b in range(len(m[0])):
            if m[a][b] == 1 or m[a][b] == 0:
                pass
            else:
                return False
    return True


def val2(mat,x):
    c = 0
    for a in range(len(mat)):
        for b in range(len(mat[0])):
            if mat[a][b] == x:
                c+=1
            else:
                pass
    if c==1:
        return True
    else:
        return False

def LF(mat,x):
    for a in range(len(mat)):
        for b in range(len(mat[0])):
            if mat[a][b] == x:
                return a,b
            else:
                pass
    return False
    






    
