
def leibniz(n, i=0):
    if i  > n:
        return 0
    return (-1) ** i / (2 * i + 1) + leibniz(n, i+1)


import math

# 0.001 pide 2 decimales de precision
# 0.0001 pide 3 decimales de precision
# 0.00001 pide 4 decimales de precision
def leibniz_approx(error, i=0, approx=0):
    # Caso base
    if abs(math.pi - approx*4) <= error:
        return i
    else:
        approx += (-1) ** i / (2 * i + 1)
        return leibniz_approx(error, i+1, approx)
    

def biseccion(y, error):
    return biseccion_aux(y, error, 0, y)

def biseccion_aux(y, error, li, ls):
    approx = (li + ls)/2
    diff = y - (approx**2)
    if abs(diff) <= error:
        return approx
    else:
        if diff < 0:
            return biseccion_aux(y, error, li, approx)
        else:
            return biseccion_aux(y, error, approx, ls)
    
    
    
