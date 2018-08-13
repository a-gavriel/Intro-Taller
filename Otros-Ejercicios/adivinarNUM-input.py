import random #importa la libreria Random

Rnumero = random.randrange(100) #crea el numero a adivinar entre 0 y 100

x=0
while(x<20):
    print (random.randrange(2))
    x+=1



bandera = True #crea una bandera para saber cuando se debe finalizar el programa
                #esto es cuando el usuario haya adivinado
print ("Ingrese un numero para intentar adivinar")
while (bandera):#mientras que el ususario no ha adivinado el numero se repetira
    try:
        numero_ingresado = (int)(input()) #toma el dato digitado y lo convierte a numero entero
    
        #print ("Numero Ingresado:" + (str)(numero_ingresado)) #esta linea se puede usar para retornar el valor ingresado
        if ((numero_ingresado)==Rnumero): #si los numeros coinciden
            bandera = False
            print ("Acertó, el numero era: ", numero_ingresado)
        else:
            Rnumero_es_mayor = Rnumero > numero_ingresado #verifica si el numero generado es mayor que el ingresado
            if (Rnumero_es_mayor): #de ser mayor el numero generado
                print ("Falló, el numero era mayor")
            else:
                print ("Falló, el numero era menor")
    except:
        print ("Por Favor Ingrese un numero en base 10") #si no se ingresa un numero manda error

