def cos_tan(AnguloRad,N):
    if isinstance (AnguloRad,float) and 0<=AnguloRad<=2*3.1416:
        if isinstance(N,int) and 0<=N<=75:
            return cos_aux(AnguloRad,N,0,0) , tan_aux(AnguloRad,N)

def factorial(N,R):
    if N==0:
        return 1
    elif N==1:
        return R
    else:
        return factorial(N-1,R*N)

def cos_aux(X,N,Ind,CosXR):
    if Ind>N:
        return CosXR
    else:
        return cos_aux(X,N,Ind+1,CosXR + ((-1)**Ind) * X**(2*Ind) / factorial(2*Ind,1))
                       
def sin_aux(X,N,Ind,SinXR):
    if Ind>N:
        return SinXR
    else:
        return sin_aux(X,N,Ind+1, SinXR + ((-1)**Ind) * X**(2*Ind+1) / factorial(2*Ind+1,1))

def tan_aux(X,N):
    a=cos_aux(X,N,0,0)
    b=sin_aux(X,N,0,0)
    c=round(b,2)
    if b==0 or c==0:
        return 'Indefinido'
    else:
        return b/a
