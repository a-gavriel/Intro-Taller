

######################
# Funciones Auxiliares
######################

# Esta funcion  N cantidad de ceros a una lista
# E: la lista y la cantidad de ceros por agregar
# R: lista no debe ser nula, n debe ser un numero
def agregue_ceros(lista, n):
    if not isinstance(lista, list) or n <= 0:
        return lista
    lista += [0]
    return agregue_ceros(lista, n-1)

######################
# Ejercicio #1
######################
##Escriba una función llamada frecuencias(lista)
##que reciba una lista conformada por números
##con valores entre 0 y n-1, donde n es
##el tamaño de la lista. La función debe retornar
##una lista que indique la cantidad de apariciones
##en lista de cada número posible. Cada número es representado
##por el índice de la nueva lista
##(en la posición 0, la cantidad de apariciones del número 0,
## en la posición 1, la cantidad de apariciones del número 1,
## y así sucesivamente).
##Debe realizar todas las validaciones para que el programa
##funcione correctamente. En caso de error debe retornar None.
def frecuencias(lista):
    if not isinstance(lista, list):
        return None
    tamano_lista = len(lista)
    resultado = agregue_ceros([], tamano_lista)
    return frecuencias_aux(lista, resultado, tamano_lista)

def frecuencias_aux(lista, resultado, tamano_lista):
    if lista == []:
        return resultado
    num = lista[0]
    if num >= tamano_lista:
        return None
    resultado[num] = resultado[num]+1
    return frecuencias_aux(lista[1:], resultado, tamano_lista)
                           

######################
# Ejercicio #2
######################
##Escriba una función reemplaza_listas(lista) que reciba una lista
##que puede contener cualquier tipo de elementos (int, float, str, list...).
##El algoritmo funciona de la siguiente manera:
##a. Debe recorrer todos los elementos de la lista de entrada y sus sub-listas
##y reemplazar los elementos que no sean int o float por el último int o
##float encontrado durante el recorrido hasta el momento.
##Si no ha encontrado ninguno debe colocar un 0 (cero).
##b. Debe realizar todas las validaciones para que el programa
##funcione correctamente. En caso de error debe retornar None.
def reemplaza_listas(lista):
    if not isinstance(lista, list):
        return None
    return reemplaza_listas_aux(lista, 0, 0)

def reemplaza_listas_aux(lista, ultimo, indice):
    if indice == len(lista):
        return lista
    elem = lista[indice]
    if isinstance(elem, int) or isinstance(elem, float):
        # Si el elemento es un numero, se debe recordar
        ultimo = elem 
    elif isinstance(elem, list):
        # Si es una sublista, se envia a procesar
        reemplaza_listas_aux(elem, ultimo, 0)
    else:
        # Cualquier otra cosa, se reemplaza por el ultimo numero.
        lista[indice] = ultimo
    return reemplaza_listas_aux(lista, ultimo, indice+1)

######################
# Ejercicio #3
######################

class Contenido:

    def __init__(self, nombre, tipo, autor, ano):
        self.nombre = nombre
        self.tipo = tipo
        self.autor = autor
        self.ano = ano
        self.puntuaciones = []

    def puntuar(self, num):
        if not isinstance(num, int) or not (0 <= num <= 5):
            return False
        self.puntuaciones += [num]
        return True

    def puntuacion_media(self, indice=0, sumatoria=0):
        cant = len(self.puntuaciones)
        if cant == 0:
            return 0
        if indice == cant:
            return sumatoria / cant
        sumatoria += self.puntuaciones[indice]
        return self.puntuacion_media(indice+1, sumatoria)
        

######################
# Ejercicio OPCIONAL
######################

##Escriba una función llamada ordena_contenido(lista) que
##reciba una lista conformada por
##instancias de Contenido (ver ejercicio 3) y
##devuelva la lista ordenada de forma descendente (mayor a menor)
##según su puntuación media. El ordenamiento debe realizarse utilizando
##el algoritmo Burbuja.
def ordena_contenido(lista):
    if not isinstance(lista, list):
        return None
    return ordena_contenido_aux(lista, 0, 0);

def ordena_contenido_aux(lista, indice, swaps):
    if indice == len(lista)-1 and swaps == 0:
        return lista
    elif indice == len(lista)-1 and swaps != 0:
        return ordena_contenido_aux(lista, 0, 0)
    else:
        izq = lista[indice]
        der = lista[indice+1]
        if izq.puntuacion_media() < der.puntuacion_media():
            lista[indice] = der
            lista[indice+1] = izq
            swaps += 1
        return ordena_contenido_aux(lista, indice+1, swaps)

######################
# Pruebas #1
######################

puntos_local = 0
puntos_global = 0

try:
    print("Probando:", "frecuencias([1,2,3,0]) == [1,1,1,1]")
    res = frecuencias([1,2,3,0])
    if res == [1,1,1,1]:
        puntos_local+=3
    else:
        print("ERROR:", res)
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "frecuencias([1,2,0,0,4]) == [2,1,1,0,1]")
    res = frecuencias([1,2,0,0,4])
    if res == [2,1,1,0,1]:
        puntos_local+=3
    else:
        print("ERROR:", res)
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "frecuencias([5,5,5,5,5,1]) == [0,1,0,0,0,5]")
    res = frecuencias([5,5,5,5,5,1])
    if res == [0,1,0,0,0,5]:
        puntos_local+=3
    else:
        print("ERROR:", res)
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "frecuencias([0,1,0,1]) == [2,2]")
    res = frecuencias([0,1,0,1])
    if res == [2,2,0,0]:
        puntos_local+=3
    else:
        print("ERROR:", res)
except Exception as e:
    print("ERROR:", e)
    
try:
    print("Probando:", "frecuencias(66) == None")
    res = frecuencias(66)
    if res == None:
        puntos_local+=3
    else:
        print("ERROR:", res)
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "frecuencias([]) == []")
    res = frecuencias([])
    if res == []:
        puntos_local+=3
    else:
        print("ERROR:", res)
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "frecuencias([1,21,23]) == None")
    res = frecuencias([1,21,23])
    if res == None:
        puntos_local+=3
    else:
        print("ERROR:", res)
except Exception as e:
    
    print("ERROR:", e)

######################
# FIN
######################

print("[FRECUENCIAS] Puntos totales:", puntos_local)
puntos_global += puntos_local
puntos_local = 0
print("\n")
    
######################
# Pruebas #2
######################

try:
    print("Probando:", "reemplaza_listas([2,'a',['a',20.4]]) == [2,2,[2,20.4]]")
    res = reemplaza_listas([2,'a',['a',20.4]])
    if res == [2,2,[2,20.4]]:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "reemplaza_listas(['a',['e',20']]) == [0,[0,20]]")
    res = reemplaza_listas(['a',['e',20]])
    if res == [0,[0,20]]:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)
    
try:
    print("Probando:", "reemplaza_listas([1,’a’,[‘a’,20.4, [‘x’]]]) == [1 ,1,[1,20.4, [20.4]]]")
    res = reemplaza_listas([1,'a',['a',20.4, ['x']]])
    if res == [1 ,1,[1,20.4, [20.4]]]:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)


try:
    print("Probando:", "reemplaza_listas(['a',2,[-10], 1]) == [0,2,[-10],1]")
    res = reemplaza_listas(['a',2,[-10], 1])
    if res == [0,2,[-10],1]:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)


try:
    print("Probando:", "reemplaza_listas([1,2,’a’,-20]) == [1,2,2,-20]")
    res = reemplaza_listas([1,2,'a',-20])
    if res == [1,2,2,-20]:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)


try:
    print("Probando:", "reemplaza_listas(123) == None")
    res = reemplaza_listas(123)
    if res == None:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)


try:
    print("Probando:", "reemplaza_listas([]) == []")
    res = reemplaza_listas([])
    if res == []:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)


######################
# FIN
######################

print("[REEMPLAZA_LISTAS] Puntos totales:", puntos_local)
puntos_global += puntos_local
puntos_local = 0
print("\n")

######################
# Pruebas #3
######################


try:
    print("Probando:", "contenido.puntuar(-2) == False")
    cont = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    res = cont.puntuar(-2)
    if res == False:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)


try:
    print("Probando:", "contenido.puntuar(7) == False")
    cont = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    res = cont.puntuar(7)
    if res == False:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)


try:
    print("Probando:", "contenido.puntuacion_media() == 0")
    cont = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    res = cont.puntuacion_media()
    if res == 0:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "contenido.puntuacion_media() == 1.5")
    cont = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    cont.puntuar(3)
    cont.puntuar(0)
    res = cont.puntuacion_media()
    if res == 1.5:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "contenido.puntuacion_media() == 3")
    cont = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    cont.puntuar(4)
    cont.puntuar(3)
    cont.puntuar(2)
    res = cont.puntuacion_media()
    if res == 3:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)


try:
    print("Probando:", "contenido.puntuacion_media() == 4")
    cont = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    cont.puntuar(5)
    cont.puntuar(3)
    res = cont.puntuacion_media()
    if res == 4:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:
    print("ERROR:", e)

try:
    print("Probando:", "contenido.puntuacion_media() == 2.5")
    cont = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    cont.puntuar(4)
    cont.puntuar(2)
    cont.puntuar(1)
    cont.puntuar(3)
    res = cont.puntuacion_media()
    if res == 2.5:
        puntos_local+=3
    else:
        print("ERROR:", res)
        
except Exception as e:    
    print("ERROR:", e)

######################
# FIN
######################

print("[CONTENIDO] Puntos totales:", puntos_local)
puntos_global += puntos_local
puntos_local = 0
print("\n")

######################
# Pruebas OPCIONAL
######################

try:
    print("Probando:", "OPCIONAL")
    peli1 = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    peli1.puntuar(5)
    peli2 = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    peli2.puntuar(4)
    peli3 = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    peli4 = Contenido("Deadpool 2", "pelicula", "Fabian Zamora", 2018)
    peli4.puntuar(3)
    peli4.puntuar(3)
    ordenada = [peli1, peli2, peli4, peli3]
    desordenada1 = [peli3, peli4, peli2, peli1]
    desordenada2 = [peli1, peli3, peli4, peli2]
    if ordena_contenido(desordenada1) == ordenada and ordena_contenido(desordenada2) == ordenada:
        print("[OPCIONAL]. Suma 20 pts.")
        puntos_global += 20
    else:
        print("ERROR","Opcional INCORRECTA")
    
except Exception as e:
    print("ERROR:", e)
    
######################
# FIN
######################
print("\n")
print("Puntos totales (sin comentarios):", puntos_global)
asumiendo_comentarios = puntos_global + 12
print("Puntos totales (asumiendo comentarios):", asumiendo_comentarios)
print("Nota (asumiendo comentarios):", asumiendo_comentarios * 100 / 75)
