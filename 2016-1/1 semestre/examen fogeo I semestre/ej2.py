from math import sqrt
def gravitación_universal(F,m1,m2,r):
    G = 6.67338*10**(-11)
    if F == '':
        if m1 != '' and m2 != '' and r!=''
            return str(G*int(m1)*int(m2)/int(r)**2) + 'N'
        else:
            return 'Parametros invalidos'
    elif m1 == '':
        if F != '' and m2 != '' and r!=''
            return str(int(F)*int(r)**2/G*int(m2)) + 'Kg'
        else:
            return 'Parametros invalidos'
    elif m2 == '':
        if F != '' and m1 != '' and r!=''
            return str(int(F)*int(r)**2/G*int(m1)) + 'Kg'
        else:
            return 'Parametros invalidos'
    elif r == '':
        if F != '' and m1 != '' and m2 !=''
            return str(sqrt (G*int(m1)*int(m2)/F) ) + 'm'
        else:
            return 'Parametros invalidos'
    else:
        return 'Incorrecto dbe existir una incognita'
