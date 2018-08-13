def paridad_par_1d3_0d5(A):
    if valtipo(A):
        if valnum(A):
            return paridad_par_aux(A)
        else:
            return 'En la lista deben haber solo 1 o 0'
    else:
        return 'Debe ingresar una lista'

def div(A):
    if contar1(A) % 3 == 0 and contar0(A) % 5 ==0:
        return A +['Unos SI divisible por 3'] + ['Ceros SI divisible por 5']
    elif contar1(A) % 3 == 0 and contar0(A) % 5 !=0:
        return A +['Unos SI divisible por 3'] + ['Ceros NO divisible por 5']
    elif contar1(A) % 3 != 0 and contar0(A) % 5 ==0:
        return A +['Unos NO divisible por 3'] + ['Ceros SI divisible por 5']
    elif contar1(A) % 3 != 0 and contar0(A) % 5 !=0:
        return A +['Unos NO divisible por 3'] + ['Ceros NO divisible por 5']

def valtipo(A):
    if isinstance (A,list):
        return True
    else:
        return False

def valnum(A):
    if A == []:
        return True
    elif A[0] != 0 and A[0] != 1:
        return False
    else:
        return valnum(A[1:])

def paridad_par_aux(A):
    if contar1(A) %2 == 0:
        return div(A)
    else:
        return div(A + [1])

def contar1(A):
    if A == []:
        return 0
    elif A[0] == 0:
        return paridad_par_aux(A[1:])
    else:
        return 1+ paridad_par_aux(A[1:])

def contar0(A):
    if A == []:
        return 0
    elif A[0] == 1:
        return paridad_par_aux(A[1:])
    else:
        return 1+ paridad_par_aux(A[1:])

