def fact16(N):
    if N==0 or N==1:
        return 1
    else:
        return N * fact16(N-1)

def cose(AnguloRad,N):
    if val1(AnguloRad) and val2(N):
        return calc_cos(AnguloRad,N)
    elif val1(AnguloRad) and not val2(N):
        return 'N no deb superar 75'
    if not val1(AnguloRad) and val2(N):
        return 'El angulo no debbe superar 2*3.1416 radianes'
    else:
        return 'Error en los parametros'

def val1(A):
    if isinstance(A,float) or isinstance(A,int):
        if 0<A<2*3.1416:
            return True
        else:
            return False
    else:
        return False

def val2(X):
    if isinstance (X,float) or isinstance (X,int):
        if 0<X<75:
            return True
        else:
            return False
    else:
        return False

def calc_cos(X,N):
    if N==0:
        return 1
    else:
        return ((-1)**N)*(X**(2*N))/fact16(2*N) + calc_cos(X,N-1)

def grad_rad(X):
    return X*3.1416/180

def par_v0_x(V0,AngGrad,N):
    a= grad_rad(AngGrad)
    b= cose(a,N)
    return V0*b
