"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 27 Marzo 2016

Entradas: Números enteros
Restricciones: Números no enteros
Salidas: Cantidad de primos entre los numeros enteros

****************************
"""

def num_primos(a,b):
  if val(a) and val(b):
    return orden(a,b)
  else:
    return "Los valores deben ser enteros"

def orden(a,b):
  if a == b:
    return "Los numeros no pueden ser iguales"
  elif a<b:
    return primos (a,b+1)
  else:
    return primos (b,a+1)

def primos(a,b):
  if a == b:
    return 0
  elif primo1(a):
    return 1 + primos(a+1,b)
  else:
    return 0 + primos(a+1,b)
    
def val(A):
  if isinstance (A,int):
    return True
  else:
    return False

def primo1(A):
  if A == 1:
    return True
  if A == 2:
    return True
  elif A%2==0:
    return False
  else:
    return xprimo(A,3)

def xprimo(A,B):
  if A==B:
    return True
  elif A%B == 0:
    return False
  else:
    return xprimo(A,B+2)
