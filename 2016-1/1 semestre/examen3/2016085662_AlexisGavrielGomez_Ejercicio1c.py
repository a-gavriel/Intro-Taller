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

Entradas: 1 Matriz con numeros en base 8
Restricciones: numeros no en base8
Salidas: De los numeros de la matriz saca el complemento C7 a los
numeros negativos (y los deja negativos), y los positivos no los afecta
****************************
"""
#
#
def C7(c7):
    return c7_aux(c7,len(c7),len(c7[0]),0,0,[],[])

def c7_aux(Mat,n,m,i,j,V,R):
    if i==n:
        return R
    elif j==m:
        R.append(V)
        return c7_aux(Mat,n,m,i+1,0,[],R)
    elif Mat[i][j] >= 0:
        V.append(Mat[i][j])
        return c7_aux(Mat,n,m,i,j+1,V,R)
    elif Mat[i][j] < 0:
        V.append(-1 * (77 - abs(Mat[i][j])))
        return c7_aux(Mat,n,m,i,j+1,V,R)
    else:
        return 'Error'

