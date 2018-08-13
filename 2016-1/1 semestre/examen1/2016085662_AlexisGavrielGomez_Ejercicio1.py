def par_hex(X):
    if isinstance(X,str):
        if valhex(X) and X != '':
            return par_hex_aux(X)
        else:
            return 'Debe ingresar un numero hexadecimal entero positivo con digitos mayores'
    else:
        return 'La entrada debe ser un String no vacío'

def valhex(N):
    if N=='':
        return True
    elif N[0]=='A':
        return valhex(N[1:])
    elif N[0]=='B':
        return valhex(N[1:])
    elif N[0]=='C':
        return valhex(N[1:])
    elif N[0]=='D':
        return valhex(N[1:])
    elif N[0]=='E':
        return valhex(N[1:])
    elif N[0]=='F':
        return valhex(N[1:])
    else:
        return False

def conv_hex2binstr(A):
    if A=='':
        return ''
    elif A[-1]=='F':
        return conv_hex2binstr(A[:-1])+'1111'
    elif A[-1]=='E':
        return conv_hex2binstr(A[:-1])+'1110'
    elif A[-1]=='D':
        return conv_hex2binstr(A[:-1])+'1101'
    elif A[-1]=='C':
        return conv_hex2binstr(A[:-1])+'1100'
    elif A[-1]=='B':
        return conv_hex2binstr(A[:-1])+'1011'
    elif A[-1]=='A':
        return conv_hex2binstr(A[:-1])+'1010'
    else:
        return 'Debe ingresar un valor entero positivo con digitos altos en hexadecimal'

def conv_hex2bin(Hex):
    if isinstance(Hex,str) and Hex != '':
        if valhex(Hex):
            return int(conv_hex2binstr(Hex))
        else:
            return 'Debe ingresar un valor entero positivo con digitos altos en hexadecimal'
    else:
        return 'Debe ingresar un string no vacío'

def paridad_bin1(N):
    if N==0:
        return 0
''' elif N%10 ==0:
        return  paridad_bin1(N//10)'''    
    else:
        return 1+paridad_bin1(N//10)

def paridad_bin(N):
    if paridad_bin1(N)%2 == 1:
        return N*10
    else:
        return N*10+1








        
    
