#Funcion Fibonacci
# E: un numero
# R: el numero debe ser entero positivo
# S: la funcion fibonacci del numero o None en caso de error
def fib(n,espacio):
    if not isinstance(n, int) or n < 0:
        return None
    print(espacio + "Calculando fib(",n,")")
    if n == 0:
        print(espacio + "Resultado", 0)
        return 0
    if n == 1:
        print(espacio + "Resultado", 1)
        return 1
    fib_n1 = fib(n-1, espacio + "*")
    fib_n2 = fib(n-2, espacio + "*")
    print(espacio + "Resultado", fib_n1 + fib_n2)
    return fib_n1 + fib_n2
    
