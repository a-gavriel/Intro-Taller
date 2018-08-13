# iguales: funcion que compara si el primer y ultimo digito de un entero son iguales
# E: numero
# S: boolean indicando si primer y ultimo digito son iguales
# R: numero entero

a = 0

def iguales(num): # Version 1: funcion principal que llama a primero(num) 
    global a
    num = abs(num)
    if isinstance(num,int):
        digmas = primero(num)
        print(a)
        return num % 10 == digmas
    else:
        return "Error"

def primero(num): # funcion recursiva que obtiene el digito mas significativo de un entero
    global a
    a = a + 1
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

def par(n):
    return n % 2 == 0 # funcion que retorna si un numero es par
def impar(n):
    return n % 2 != 0 # funcion que retorna si un numero es impar

def suma_parimpar(num):
    if isinstance(num,int):
        num = abs(num)
        return par_impar_aux(num, par), par_impar_aux(num, impar)
    else:
        return "Error"

def par_impar_aux(num, funcion):
    if num == 0: # caso base
        return 0
    elif funcion(num): # selecciona digito segun funcion de entrada
        return num % 10 + par_impar_aux(num // 10, funcion)
    else:
        return par_impar_aux(num // 10, funcion)
    
def dig_ab(n1, n2): # version con divide y venceras
    if isinstance(n1, int) and isinstance(n2, int):
        return dig_ab_aux(abs(n1), abs(n2))
    else:
        return "error"

def dig_ab_aux(n1, n2):
    if n1 == 0: # caso base 1
        return True
    elif not contenido(n1 % 10, n2): # caso base 2
        return False
    else:
        return dig_ab_aux(n1 // 10, n2)

def contenido(dig, num):
    if num == 0: # caso base 1
        return False
    elif dig == num % 10: # caso base 2
        return True
    else:
        return contenido(dig, num // 10)
    
def dig_ab1(n1, n2): # version con divide y venceras
    if isinstance(n1, int) and isinstance(n2, int):
        n2 = abs(n2)
        return dig_ab1_aux(abs(n1), n2, n2)
    else:
        return "error"
        
def dig_ab1_aux(n1, n2, n3):
    if n1 == 0 and n2 == 0: # caso base 1
        return True
    if n1 == 0: # caso base 2
        return False
    elif n2 == 0:
        return dig_ab1_aux(n1 // 10, n3, n3)
    elif n1 % 10 == n2 % 10:
        return dig_ab1_aux(n1 // 10, n3, n3)
    else:
        return dig_ab1_aux(n1, n2 // 10, n3)
        
    

























        
        







        

