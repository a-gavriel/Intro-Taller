"""
****************************

  Instituto Tecnologico de Costa Rica

    Ingenieria en Computadores

Version de Lenguaje de Python 3.5.1
Autor: Alexis Gavriel
Carné: 2016085662
Version 1.0
Fecha Ultima modificación: 13 Mayo


calculo pi medios
Entradas: Cantidad de sumas a realizar : Numero entero positivo
Restricciones: Ninguna
Salidas: Aproximacion a pi medios

calculo volumen
Entradas: Radio : Numero positivo
Restricciones: Ninguna
Salidas: Valor aproximado del volumen de una esfera

Calculo aproximado de euler
Entradas: Error : Numero fraccionario positivo menor a 1
Restricciones: Ninguna 
Salidas: Aproximacion al numero euler



****************************
"""



def pi_euler(N):
    if isinstance (N,int):
        if 0<N<101:
            return pi_euler_aux(N)
        else:
            return 'N debe estar entre 1 y 100'
    else:
        return 'N debe ser entero'

def fact(A):
    if A==0:
        return 1
    if A == 1:
        return 1
    else:
        return A* fact(A-1)

def pi_euler_aux(K):
    if N<0:
        return 0
    else:
        return ((2**K)*fact(K)**2/fact(2*K+1)) + pi_euler_aux(K-1)

def vol_area(Radio):
    if isinstance (Radio*1.0,float):
        if Radio>0:
            return 4*2*pi_euler(80) * (Radio**3) /3
        else:
            return 'Radio debe ser positivo'
    else:
        return 'Radio debe ser un número Real'






def ctc_e(Error):
    if isinstance(Error,float):
        if Error >=1:
            return 'El error debe ser <1'
        elif Error <= 0:
            return 'El error debe ser >0'
        elif Error < 1*10**(-15):
            return 'El error debe ser > que 1*10Exp-15'
        else:
            return calc_e_aux(0,Error)
    else:
        return 'Parametro debe ser numero' 

def calc_e_aux(B,Error):
    e= 2.718281828459045235360287475352
    new_e = calculo_e (B)
    if B > 100:
        return 'Precision supero el N de la sumatoria'
    elif e - new_e < Error:
        return new_e
    else:
        return calc_e_aux(B + 1,Error)



def calculo_e(N):
  if isinstance (N,int):
    if 0<=N<=100:
      return calc_e(N,0)
    else:
      return "El número debe estar entre 1 y 30"
  else:
    return "Debe ingresar um valor entero"

def calc_e(N,A):
  if N == A:
    return 0
  else:
    return 1/(factorial(A)) + calc_e(N,A+1)




def factorial(X):
    if X==0:
        return 1
    elif X==1:
        return 1
    else:
        return X * factorial(X-1)
