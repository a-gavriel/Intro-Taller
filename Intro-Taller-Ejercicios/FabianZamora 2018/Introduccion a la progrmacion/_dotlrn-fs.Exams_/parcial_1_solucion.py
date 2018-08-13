# Escriba una función elim_min_max(num, min, max)
# que reciba un número entero natural (num) y
# dos dígitos válidos positivos (min, max).
# La función debe retornar un nuevo número entero natural,
# formado por los dígitos de num mayores o iguales a min
# y menores a max. En caso de error o argumento invalido,
# debe retornar None.
def elim_min_max(num, men, may):
    if not isinstance(num, int):
        return None
    if not isinstance(men, int):
        return None
    if not isinstance(may, int):
        return None
    if num > 0 and 0 <= men < 10 and 0 <= may < 10:
        return elim_min_max_aux(num, men, may, 0)
    else:
        return None

def elim_min_max_aux(num, men, may, cant_dig_res):
    if num == 0:
        return 0
    ultimo_dig = num % 10
    if men <= ultimo_dig < may:
        return 10**cant_dig_res*ultimo_dig + elim_min_max_aux(num//10, men, may, cant_dig_res+1)
    else:
        return elim_min_max_aux(num//10, men, may, cant_dig_res)

# Escriba una función split(num, dig) que reciba un número entero natural
# (num) y un dígito positivo (dig). La función debe retornar una lista de
# números donde cada número se forma juntando los dígitos de num hasta
# encontrar una aparición de dig. La función debe retornar None en caso
# de error o argumento inválido.
def split(num, dig):
    if not isinstance(num, int):
        return None
    if not isinstance(dig, int):
        return None
    if num > 0 and 0 < dig < 10:
        return split_aux(num, dig, 0, 0)
    else:
        return None

def split_aux(num, dig, tmp, digs_tmp):
    if num == 0:
        if tmp != 0:
            return [tmp]
        else:
            return []
        
    # Si el digito no es igual se debe ir formando el
    # resultado temporal
    ult_dig = num % 10
    if ult_dig != dig:
        tmp = tmp + (10**digs_tmp*ult_dig)
        return split_aux(num//10, dig, tmp, digs_tmp + 1)

    # Si el digito es igual, se guarda el resultado tmp
    # Si no es cero. Cero significa que a tmp no se le ha
    # Agregado ningun digito.
    if ult_dig == dig and tmp != 0:
        return split_aux(num//10, dig, 0, 0) + [tmp]
    else:
        return split_aux(num//10, dig, 0, 0)        

# Escriba una función separa(lista, num) que reciba una
# lista de números naturales y un número natural.
# La función debe devolver una lista con dos sub-listas:
# en la primer sub-lista debe incluir los elementos de
# lista que son divisibles por num, mientras que en la
# segunda lista debe incluir los que no. En caso de que
# la entrada no sea una lista o num no sea entero natural
# debe retornar None. Puede asumir que dentro de la lista
# todos los elementos son enteros naturales.
def separa(lista, num):
    if not isinstance(lista, list):
        return None
    if not isinstance(num, int) or num <= 0:
        return None
    return separa_aux(lista, num, [], [])

def separa_aux(lista, num, div, no_div):
    if lista == []:
        return [div, no_div]
    elem = lista[0]
    if elem % num == 0:
        return separa_aux(lista[1:], num, div+[elem], no_div)
    else:
        return separa_aux(lista[1:], num, div, no_div+[elem])
    
# Escriba una función sumatoria_listas(lista) que
# reciba una lista que puede contener cualquier
# tipo de elementos (int, float, str, list…) y
# obtenga la sumatoria de todos los elementos de
# tipo int y float de la lista y todas sus sub-listas.
# En caso de que la entrada no sea una lista debe retornar None.
def sumatoria_listas(lista):
    if not isinstance(lista, list):
        return None
    if lista == []:
        return 0
    primer_elem = lista[0]
    if isinstance(primer_elem, int) or isinstance(primer_elem, float):
        return primer_elem + sumatoria_listas(lista[1:])
    elif isinstance(primer_elem, list):
        return sumatoria_listas(primer_elem) + sumatoria_listas(lista[1:])
    else:
        return sumatoria_listas(lista[1:])


    
