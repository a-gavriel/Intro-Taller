#################################################
#  Recursividad de Pila
#################################################


def suma_par_impar_pila(num):
    num=abs(num)
    if not isinstance(num,int):
        return "Ingrese un número entero"
    return suma_par_aux(abs(num)) , suma_impar_aux(abs(num))

def suma_par_aux(num):
    if num==0:
        return 0
    else:
        if num%2==0:
            return num%10 + suma_par_aux(num//10)
        else:
            return suma_par_aux(num//10)

def suma_impar_aux(num):
    if num==0:
        return 0
    else:
        if num%2!=0:
            return num%10 + suma_impar_aux(num//10)
        else:
            return suma_impar_aux(num//10)

#################################################
#  Recursividad de Cola
#################################################

def suma_par_impar_cola(num):
    num=abs(num)
    if not isinstance(num,int):
        return "Ingrese un número entero"
    return suma_par_impar_aux(abs(num),0,0)

def suma_par_impar_aux(num, par, impar):
    if num==0:
        return (par,impar)
    else:
        if num%2==0:
            par= par + num%10
            return suma_par_impar_aux(num//10 , par, impar)
        else:
            impar= impar + num%10
            return suma_par_impar_aux(num//10 , par, impar)
