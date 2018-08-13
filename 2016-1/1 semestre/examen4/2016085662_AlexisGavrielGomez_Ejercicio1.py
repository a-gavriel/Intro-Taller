"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 16 Junio

Entradas: un vector de 5 numeros reales, una matriz con con un string y 5 numeros por fila, lista vacia para el resultado
Restricciones: matriz contiene distintos valores de los mencionados, o contiene numeros complejos
Salidas: matiz que contiene los datos de la matriz más la suma de la multiplicacion de las filas por el vector

****************************
"""

def fact_cel(VecCost,MatCon,MatFact):
    if val(VecCost):
        if val2(VecCost,MatCon):
            return fact_aux(['']+VecCost,MatCon,MatFact) #se agrego la palabra return
        else:
            return 'Error, matriz debe tener 6 columnas y el vector 5 elementos'
    else:
        return 'Error, Vector debe contener numeros reales'

def val(vec):
    for a in vec:
        if isinstance(a,int) or isinstance (a,float):
            pass
        else:
            return False
    return True

def val2(VecCost,MatCon):
    if len(VecCost) == 5 :
        if len (MatCon[0]) == 6:
            return True
        else:
            return False
    else:
        return False

def fact_aux(Vec,mat,R):
    v= []
    for a in range(len(mat)):
        for b in range(len(mat[0])):
            if isinstance(mat[a][b],str):
                v.append(mat[a][b])
            else:
                res = (mat[a][b] * Vec[b])
                v.append (round(res,5))
        suma = v[1] + v[2] + v[3] + v[4] + v[5]
        R.append (mat[a]+[suma])
        v=[]
    return R


