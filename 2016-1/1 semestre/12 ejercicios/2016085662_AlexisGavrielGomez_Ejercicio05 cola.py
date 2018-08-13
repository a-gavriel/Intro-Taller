#calculo E
def factorial(A,R):
    if A == 0:
        return 1
    elif A==1:
        return R
    else:
        return factorial(A-1,R*A)
