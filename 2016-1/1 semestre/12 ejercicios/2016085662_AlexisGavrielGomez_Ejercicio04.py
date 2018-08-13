


def listaN(Lista):
  if isinstance (Lista,list):
    if val(Lista):
      return xlista(Lista,[],[])
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

def rev(A,B):
    if B==[]:
        return False
    elif A == B[0]:
        return True
    else:
        return rev(A,B[1:])
    
def xlista (a,b,c):
    if a==[]:
        return c
    elif not rev(a[0],b):
        return xlista (a[1:],[a[0]]+b,c)
    else:
        return xlista (a[1:],b,[a[0]]+c)

