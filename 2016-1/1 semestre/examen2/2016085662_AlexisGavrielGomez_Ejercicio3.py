def ctc_e(Error):
    if Error >=1:
        return 'El error debe ser <1'
    elif Error <= 0:
        return 'El error debe ser >0'
    elif Error < 1*10**(-15):
        return 'El error debe ser > que 1*10Exp-15'
    else:
        return calc_ex(0,150,Error,0)

def calc_ex(N,M,Error,R):
    e= 2.718281828459045235360287475352
    if e-R<Error:
        return R
    elif N>M:
        return 'Precision supero el N de la sumatoria'
    else:
        return calc_ex(N+1,M,Error,R+1/factorial(N,1)) #Se agregó al final R+

def factorial(X,R):
    if X==0:
        return 1
    elif X==1:
        return R
    else:
        return factorial(X-1,R*X)
