#Funcion factorial
#E: El numero al cual calcularle el factorial
#R: El numero debe ser entero positivo
#S: La funcion factorial del numero
def fact(n):
    print("Inicio fact() de:", n)
    if not isinstance(n, int) or n < 0:
        return None
    if n == 0:
        print("Caso base")
        return 1
    print("Comenzando a calcular fact() de:", n)
    resultado = n * fact(n-1)
    print("El fact() de:",n,"es:", resultado)
    return resultado
