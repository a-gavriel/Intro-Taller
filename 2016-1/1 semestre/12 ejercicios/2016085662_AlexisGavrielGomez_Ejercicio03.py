"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.2
Fecha Ultima modificación: 30 Marzo 2016

Entradas: Lista con numeros enteros
Restricciones: numeros no enteros
Salidas: Lista de numeros pares y lista de numeros impares

****************************
"""

def par_impar (Lista):
  if isinstance (Lista,list):
    if val(Lista):
      return xpar_impar(Lista,[],[])
    else:
      return "Un valor en la lista no es entero"
  else:
    return "Debe ingresar una lista"

def val(Lista):
  if Lista == []:
    return True
  elif not valE(Lista[0]):
    return False
  else:
    return val(Lista[1:])

def valE(X):
    if isinstance (X,int):
      return True
    else:
      return False


def xpar_impar(Lista,l1,l2):
  if Lista == []:
    return l1,l2
  elif Lista[0] %2 == 0:
    return xpar_impar(Lista[1:],[Lista[0]]+l1,l2)
  else:
    return xpar_impar(Lista[1:],l1,[Lista[0]]+l2)

