
def leibniz(n):
    if n >1:
        return leibniz_aux(n,0 , 0) * 4
    else:
        return None

def leibniz_aux(n, i, aprox):
    if i > n:
        return aprox
    else:
        aprox += ((-1)**i / (2*i + 1))
        return leibniz_aux(n, i+1, aprox)

import math

def leibniz2(error):
    if error > 0:
        return leibniz_aux2(error, 0 , 0)
    else:
        return None

def leibniz_aux2(error, i, aprox):
    if abs(math.pi - (aprox*4)) <= error:
        print("n:", i)
        return aprox * 4
    else:
        aprox += ((-1)**i / (2*i + 1))
        return leibniz_aux2(error, i+1, aprox)


def biseccion(y, error):
    if y > 0:
        return biseccion(y, error, 0, y, 0)
    return None

def biseccion_aux(y, error, approx)
