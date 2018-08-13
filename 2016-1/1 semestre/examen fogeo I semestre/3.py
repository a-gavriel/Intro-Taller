def factorial(A):
    if A == 0 or A == 1:
        return 1
    else:
        return A * factorial(A-1)

def num_e(A):
    if A==0:
        return 1
    else:
        return 1 / (factorial(A)) + num_e(A-1)

def num_e_aux(A):
    if isinstance (A,int):
        if 0 <= A >= 24:
            return num_e(A)
        else:
            return 'El numero debe estar entre 0 y 24'
    else:
        return 'A debe ser entero'

def num_e_C9_aux(N,CantiDigitos):
    return 




def complemento1(A):
    a = A
    m = cantdig_int(a)
    n = cantdig_frac(a)
    o = 10**(m)
    p = 10**(-1*n)
    return o -a -p

def cantdig_frac(A):
    a = A
    return cantdig_int(conv(a)) - cantdig_int(a)

def cantdig_int(A):
    if A == 0:
        return 0
    else:
        return 1 + cantdig_int(A//10)

def conv(A):
    if A == int(A):
        return int(A)
    else:
        return conv(A*10)
