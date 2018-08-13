

def sumatoria(n,resultado):
    if type(n)==int:
        if n==0:
            return resultado
        else:
            return sumatoria(n-1,resultado+n)
    else:
        return "Ingrese un numero entero"


def suma_ultimo_digito(a,b):
    return ((a%10) + (b%10))

def invertir_3digitos(num):
    if (type(num)== int ) and 99 < num < 1000 :
        ultimo_digito =  num%10
        num2 = num //10
        penultimo_digito = num2 %10
        num3 = num2 //10
        primer_digito = num3 %10
        numero = ultimo_digito*100 + penultimo_digito*10 + primer_digito
        return numero


def numero_de_digitos( n ):
    if n == 0:
        return 0
    else:
        return 1 + numero_de_digitos( n//10 )
