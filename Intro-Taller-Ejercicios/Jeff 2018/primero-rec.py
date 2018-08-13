def suma1(num): # ver 1. Basica
    if num == 0:
        return 0
    else:
        return num % 10 + suma1(num // 10)
    
def suma2(num): # ver 2: poco eficiente
    if isinstance(num, int):
        if num == 0:
            return 0
        else:
            return num % 10 + suma2(num // 10)
    else:
        return "Error"

def suma(num): # ver 3. Eficiente. Funcion principal
    if isinstance(num, int):
        return suma_aux(num)
    else:
        return "Error"

def suma_aux(num): # auxiliar recursiva
    if num == 0:
        return 0
    else:
        return num % 10 + suma_aux(num // 10)












