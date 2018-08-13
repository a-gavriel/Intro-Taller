"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 27 Marzo 2016

Entradas: Lista con números enteros
Restricciones: No lista, o lista con numeros no enteros
Salidas: Si la lista tiene o no al menos un numero par

****************************
"""
def numpar (Lista):
  if isinstance (Lista,list):
    if val(Lista):
      return xnumpar (Lista)
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
  
def xnumpar (Lista):
  if Lista == []:
    return False
  elif Lista[0] %2 == 0:
    return True
  else:
    return xnumpar(Lista[1:])
