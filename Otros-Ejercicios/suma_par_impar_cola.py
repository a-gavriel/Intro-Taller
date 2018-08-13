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
