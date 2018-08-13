from parcial_1_solucion import *

fallidas = 0
exitosas = 0

def prueba_elim_min_max(num, men, may, esperado):
    global fallidas
    global exitosas
    try:
        print("Probando elim_min_max(). Esperado:", esperado)
        resultado = elim_min_max(num, men, may)
        print("Probando elim_min_max(). Resultado:", resultado)
        if resultado == esperado:
            exitosas += 1
        else:
            fallidas += 1
            print("ERROR")
    except:
        fallidas += 1
        print("ERROR")

def prueba_split(num, dig, esperado):
    global fallidas
    global exitosas
    try:
        print("Probando split(). Esperado:", esperado)
        resultado = split(num, dig)
        print("Probando split(). Resultado:", resultado)
        if resultado == esperado:
            exitosas += 1
        else:
            fallidas += 1
            print("ERROR")
    except:
        fallidas += 1
        print("ERROR")

def prueba_separa(lista, num, esperado):
    global fallidas
    global exitosas
    try:
        print("Probando separa(). Esperado:", esperado)
        resultado = separa(lista, num)
        print("Probando separa(). Resultado:", resultado)
        if resultado == esperado:
            exitosas += 1
        else:
            fallidas += 1
            print("ERROR")
    except:
        fallidas += 1
        print("ERROR")

def prueba_sumatoria_listas(lista, esperado):
    global fallidas
    global exitosas
    try:
        print("Probando sumatoria_listas(). Esperado:", esperado)
        resultado = sumatoria_listas(lista)
        print("Probando sumatoria_listas(). Resultado:", resultado)
        if resultado == esperado:
            exitosas += 1
        else:
            fallidas += 1
            print("ERROR")
    except:
        fallidas += 1
        print("ERROR")
        
def muestra_resultado():
    totales = fallidas + exitosas
    print('Pruebas totales:', exitosas)
    print('Pruebas exitosas:', exitosas)
    print('Pruebas fallidas:', fallidas)
    print('Nota:', exitosas * 100 / totales)
    
######### elim_min_max ##############

prueba_elim_min_max(2345645, 4, 5, 44)
prueba_elim_min_max(0, 4, 4, None)
prueba_elim_min_max(245, -4, 4, None)
prueba_elim_min_max(-245, 4, 4, None)
prueba_elim_min_max(2345645, 4, 4, 0)
prueba_elim_min_max(2345645, 42, 4, None)
prueba_elim_min_max(245, 4, -4, None)
prueba_elim_min_max(123456780, 0, 9, 123456780)

######### split ##############

prueba_split(2345645, 4, [23,56,5])
prueba_split(23445645, 4, [23,56,5])
prueba_split(-23445645, 1, None)
prueba_split(0, 2, None)
prueba_split(23445645, 7, [23445645])
prueba_split(23445645, 17, None)
prueba_split(23445645, -1, None)

######### separa ##############

prueba_separa([1,2,3,30], 3, [[3,30],[1,2]])
prueba_separa([1,2,3,30,11,33], 4, [[],[1,2,3,30,11,33]])
prueba_separa([1,2,3,30,11,33], 1, [[1,2,3,30,11,33], []])
prueba_separa(123, 1, None)
prueba_separa([1,2], 0, None)
prueba_separa([1,2], -10, None)

######### sumatoria_listas ##############

prueba_sumatoria_listas ([1,2,'a',['a',20.4]], 23.4)
prueba_sumatoria_listas ([1,2,'a',['a',20.4, [2]]], 25.4)
prueba_sumatoria_listas([1,2,'a',2,[-10], 1], -4)
prueba_sumatoria_listas ([1,2,'a',-20], -17)
prueba_sumatoria_listas(123, None)

muestra_resultado()
