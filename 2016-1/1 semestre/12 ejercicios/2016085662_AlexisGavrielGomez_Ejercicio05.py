def calculo_e(N):
  if isinstance (N,int):
    if 0<=N<=30:
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

def factorial (A):
  if A==0:
    return 1
  elif A==1:
    return 1
  else:
    return A * factorial(A-1)
    
