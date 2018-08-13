def hexto2C5(ListaBase16):
    if isinstance(ListaBase16,list):
        if ListaBase16==[]:
            return []
        elif val(ListaBase16):
            return hextobin(ListaBase16,[])
        else:
            return ListaBase16,'Error base16'
    else:
        return 'El argumento debe ser una lista'

def val(Lista16):
    if Lista16==[]:
        return True
    elif Lista16[0]=='A':
        return val(Lista16[1:])
    elif Lista16[0]=='B':
        return val(Lista16[1:])
    elif Lista16[0]=='C':
        return val(Lista16[1:])
    elif Lista16[0]=='D':
        return val(Lista16[1:])
    elif Lista16[0]=='E':
        return val(Lista16[1:])
    elif Lista16[0]=='F':
        return val(Lista16[1:])
    else:
        return False


def hextobin(Lista16,Lista2):
    if Lista16 == []:
        return comp(Lista2,[])
    elif Lista16[0]== 'A':
        return hextobin(Lista16[1:],Lista2+['1','0','1','0'])
    elif Lista16[0]== 'B':
        return hextobin(Lista16[1:],Lista2+['1','0','1','1'])
    elif Lista16[0]== 'C':
        return hextobin(Lista16[1:],Lista2+['1','1','0','0'])
    elif Lista16[0]== 'D':
        return hextobin(Lista16[1:],Lista2+['1','1','0','1'])
    elif Lista16[0]== 'E':
        return hextobin(Lista16[1:],Lista2+['1','1','1','0'])
    elif Lista16[0]== 'F':
        return hextobin(Lista16[1:],Lista2+['1','1','1','1'])
    else:
        print ('No se pudo convertir a binario')

def comp(Lista2,comp2):
    if Lista2 == []:
        return comp2
    elif Lista2[0]== '1':
        return comp(Lista2[1:],comp2 + ['0'])
    elif Lista2[0]== '0':
        return comp(Lista2[1:],comp2 + ['1'])

def string2num(ListaBin):
    if isinstance(ListaBin,list):
        if ListaBin==[]:
            return 0
        elif val2(ListaBin):
            return string2num_aux(ListaBin,0)
        else:
            return ListaBin,'Error base 2'
    else:
        return 'Debe ingresar una lista'

def val2(Lista):
    if Lista == []:
        return True
    elif Lista[0]=='0':
        return val2(Lista[1:])
    elif Lista[0]=='1':
        return val2(Lista[1:])
    else:
        return False

def string2num_aux(Lista,R):
    if Lista == []:
        return R
    else:
        return string2num_aux(Lista[1:],R*10+int(Lista[0]))




