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
