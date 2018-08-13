#Maximo Comun Divisor de 2 Numeros
#Entrada: 2 numeros
#Salida: MCD de los dos numeros

#Funcion para saber si un numero es primo
def primos(n, cont):
    if (n==0 or n==1):
        return False
    elif (n==cont):
        return True
    elif (n%cont == 0):
        return False
    else:
        return primos(n,cont+1)

#Funcion auxiliar para obtener MCD
def mcd_aux(a,b,div):
    if(div > a or div > b):
        return 1
    elif(primos(div,2)):
        if(a%div == 0 and b%div == 0):
            return div * mcd_aux(a/div, b/div, div)
        else:
            return mcd_aux(a, b, div+1)
    else:
        return mcd_aux(a,b,div+1)


#Llamada principal a MCD
def mcd_main(a,b):
    cont = 2
    return   mcd_aux(a,b,cont)


#Funcion para calcular el area de un rectangulo
def area_rect(l, a):
    print("El area del rectangulo es: ", l * a)

#Funcion para convertir colones a dolares
def col_dol(colones):
    print("El valor en dolares del monto ingresado es de: ", colones//564)

#Funcion para obtener el area de un circulo
import math
def area_circulo(radio):
    print("El area del circulo es igual a: ", math.pi*(radio**2))

#Funcion para armar rectangulo con *
def tipoA(n):
    print("*" * n) 

def tipoB(n):
    print("*" + (n-2) * " " + "*")

def ast_aux(l,h,cont):
    if(cont == 1):
        tipoA(l)
        return ast_aux(l, h, cont+1)
    elif(cont < h):
        tipoB(l)
        return ast_aux(l, h, cont+1)
    elif(cont == h):
        tipoA(l)
    else:
        print("Error en el programa")

def ast(l, h):
    cont = 1
    return   ast_aux(l,h,cont)
    
#Funcion para calcular un capital a N años

def capital(c,x,n):
    if(x > 0):
        print("El valor del capital es de: ", c*(1+x/100)*n, "euros") 
    else:
        print("El valor del interes debe ser positivo")


#Funcion para distribuir billetes

def euros(n):
    if(n == 0):
        print("Fin")

    elif(n>=500):
        print("Billetes de 500 euros: ", n//500)
        return euros(n%500)
    elif(n>=200):
        print("Billetes de 200 euros: ", n//200)
        return euros(n%200)
    elif(n>=100):
        print("Billetes de 100 euros: ", n//100)
        return euros(n%100)
    elif(n>=50):
        print("Billetes de 50 euros: ", n//50)
        return euros(n%50)
    elif(n>=20):
        print("Billetes de 20 euros: ", n//20)
        return euros(n%20)
    elif(n>=10):
        print("Billetes de 10 euros: ", n//10)
        return euros(n%10)
    elif(n>=5):
        print("Billetes de 5 euros: ", n//5)
        return euros(n%5)
    elif(n>=2):
        print("Monedas de 2 euros: ", n//2)
        return euros(n%2)
    elif(n>=1):
        print("Monedas de 1 euro: ", n//1)
        return euros(n%1)
    else:
        print("Error, revise su programa")


#Funcion para obtener la distancia segun formula de Pitagoras

def distancia(x1,y1,x2,y2):
    print("El valor de la distancia segun las coordenadas es de: ", ((x2-x1)**2 + (y2-y1)**2)**(1/2) )


def porcentaje(n, t):
    return (n * 100)/t
    
def nounProject(a,b,c,d):
    total = a + b + c + d
    print("El porcentaje de Josue es igual a: ", porcentaje(a, total), "y posee: ", a//(total/2000))
    porcentajeA = porcentaje(a, total)
    print("El porcentaje de Agustin es igual a: ", porcentaje(b, total), "y posee: ", b//(total/2000))
    porcentajeB = porcentaje(b, total)
    print("El porcentaje de Isaac es igual a: ", porcentaje(c, total), "y posee: ", c//(total/2000))
    porcentajeC = porcentaje(c, total)
    print("El porcentaje de Sergio es igual a: ", porcentaje(d, total), "y posee: ", d//(total/2000))
    porcentajeD = porcentaje(d, total)
    print("El valor de la accion es de: ", total/2000)
    
    inversion = int(input("El valor de inversion de Felipe es de: "))
    total = total + (inversion*564)
    nuevaAccion = total/2000
    print("El valor del nuevo capital es: ", total)
    print("El valor de la nueva accion post inversion es de: ", nuevaAccion)
    
    restriccion = int(input("Ingrese el % de acciones que recibira Felipe: "))

    print("La cantidad de dinero que posee Josue es igual a: ", (porcentajeA*(total*0.9)/100))
    print("La cantidad de dinero que posee Agustin es igual a: ", (porcentajeB*(total*0.9)/100))
    print("La cantidad de dinero que posee Isaac es igual a: ", (porcentajeC*(total*0.9)/100))
    print("La cantidad de dinero que posee Sergio es igual a: ", (porcentajeD*(total*0.9)/100))
    print("La cantidad de dinero que posee Felipe es igual a: ", (total*0.1))


#Funcion para calcular monto a pagar de un prestamo a 5, 8 o 12 años

def solicitudPrestamo(monto):
    plazo = int(input("Ingrese el plazo deseado entre 5, 8 o 12 años"))
    totalPagar = (((monto * 0.2625)*plazo) + monto)/(plazo * 12)
    penalizacion = (totalPagar * 0.022)
    print ("El monto total a pagar es de", totalPagar, "y se le penalizara un monto de: ", penalizacion, "en caso de atraso")
        

#Funcion para convertir un decimal a un binario

def decimalesBinarios(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return int(str(decimalesBinarios(num//2))+str(num%2))

# Funcion para convertir un decimal a hexadecimal
# Estructura de diccionario usada para obtener resultados de una coleccion
# finita de datos.
def obtenerLetra(x):
    return {
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F',
        }.get(x,x)

def decimalesHexa(num):
    if(0 <= num <= 9):
        return num
    elif(10 <= num <= 15):
        return obtenerLetra(num)
    else:
        return str(decimalesHexa(num//16))+str(decimalesHexa(num%16))
              

#Laboratorio 1 de Taller de Programacion

#Funcion que calcula el resultado de operar numeros en duplas a partir de un
# numero ingresado


def contNum(n):
    if(0 <= n <= 99):
        return 1
    else:
        return 1 + contNum(n//100)

def calculadora(n, op):
    cal_aux(n, contNum(n), op)
    
def cal_aux(n, total, op):
    if(op == "multiplicacion"):
        if(n//100 == 0):
            return n
        elif(0<= n <= 9):
            return n
        else:                         
            return n%100*calculadora(n//100, op)
    elif(op == "suma"):
        if(n//100 == 0):
            return n
        elif(0<= n <= 9):
            return n
        else:                         
            return n%100+calculadora(n//100, op)
    elif(op == "promedio"):
        if(n//100 == 0):
            return n
        elif(0<= n <= 9):
            return n
        else:                         
            return (n%100+calculadora(n//100, op)//total)
    else:
        print("Error en la operacion ingresada")



#Funcion para calcular la cantidad de digitos dentro de un numero

def largo(num):
    if isinstance(num,int):
        if(num!=0):
            return largo_aux(num)
        else:
            return 1
    else:
        print("Error")


def largo_aux(num):
    if(num == 0):
        return 0
    else:
        return 1 + largo_aux(num//10)

# Funcion que reciba un digito y un numero entero y
# que cuente la cantidad de veces que aparece el digito en numero


def cuenta(dig, num):
    if isinstance(dig and num, int):
        if(dig == num):
            return 1
        else:
            return cuenta_aux(dig,num)
    else:
        print("Error")

def cuenta_aux(dig,num):
    if(num == 0):
        return 0
    elif(num%10 == dig):
        return 1 + cuenta_aux(dig, num//10)
    else:
        return cuenta_aux(dig, num//10)


# Funcion que se llame forme_pares que reciba un entero y forme otro entero
# con los digitos pares del numero de entrada.

def forme_par(num):
    if isinstance(num,int):
        exp = 0
        return forme_par_aux(num,exp)
    else:
        return "Error"

def forme_par_aux(num,exp):
    if(num==0):
        return 0
    elif(num%2 == 0):
        return num%10*10**exp+forme_par_aux(num//10,exp+1)
    else:
        return forme_par_aux(num//10,exp)



    
#El caso de Jose

def forme_pares(num):
    return forme_pares_aux(num,0)

def forme_pares_aux(num,nuevo_num):
    if (num == 0):
        return nuevo_num
    elif((num%10)%2 == 0):
        return forme_pares_aux(num//10, nuevo_num*10+num%10)
    else:
        return forme_pares_aux(num//10, nuevo_num)


#Introduccion a Listas

#La indexacion nos permite acceder elementos utilizando una posicion. Siempre
#se inicia en 0 

#Un programa que lea 20 numeros (entre el 1 y el 10) y que los almacene en una
#lista y muestre aquellos numeros que hayan aparecido mas de una vez

    # append | count | index | insert | pop | remove | reverse | sort 


lista=[]
def lectura():
    if len(lista)==20:
        lectura_aux(1)
    else:
        conjunto=int(input(str(len(lista))+"Ingrese un número entre el 1 y 10: "))
        if conjunto>10 or conjunto<1:
            return "El número no está en el intervalo establecido"
        else:
            lista.append(conjunto)
            lectura()

def lectura_aux(a):
    if a==11:
       return ""
    elif lista.count(a)>2:
        print(a)
        lectura_aux(a+1)
    else:
        lectura_aux(a+1)
    
    

























    






















































        






























