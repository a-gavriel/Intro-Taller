# iguales: funcion que compara si el primer y ultimo digito de un entero son iguales
# E: numero
# S: boolean indicando si primer y ultimo digito son iguales
# R: numero entero

def iguales(num): # Version 1: funcion principal que llama a primero(num) 
    num = abs(num)
    if isinstance(num,int):
        return num % 0 == primero(num)
    else:
        return "Error"

def primero(num): # funcion recursiva que obtiene el digito mas significativo de un entero
    if num < 10: # caso base
        return num
    else:
        return primero(num // 10)
    
def iguales2(num): # version 2: no recursiva que reutiliza codigo de largo(num)
    num = abs(num)
    if isinstance(num,int):
        return num % 10 == num // (10 ** (largo(num) - 1))
    else:
        return "Error"
    
def largo(num):
    if num == 0: # caso base
        return 0
    else:
        return 1 + largo(num // 10)
