# Pregunta 1
# E: Número entero
# S: lista con el número dividido en partes segun aparecen ceros
6# R: número entero

def split(num):
    if isinstance(num, int):
        return split_aux(abs(num), 0 , 0, [])
    else:
        return "Error"

def split_aux(num ,exp, subn, res):
    if num == 0:
        if subn == 0:
            return res
        else:
            return split_aux(num, 0, 0, [subn] + res)
    elif num % 10 ==0:
        if subn == 0:
            return split_aux(num // 10, 0, 0, res)
        else:
            return split_aux(num // 10, 0, 0, [subn] + res)
    else:
        return split_aux(num // 10, exp + 1, subn + (num % 10) * 10 ** exp, res)

# Pregunta 2
# E: lista
# S: lista cambiado por cero elementos que se repiten 2 veces o mas
# R: lista no nula

# Parte a. Recursividad de cola

def cambie_r(lista):
    if  lista != []:
        return cambier_aux(lista, 0, len(lista))
    else:
        return "Error"

def cambier_aux(lista, i, n,):
    if i == n:
        return lista
    if not isinstance(lista[i], int):
        return "Error"
    if cuente(i, n, lista[i], lista, 0) >= 2:
        lista = cambier_0(i, n, lista[i], lista)
    return cambier_aux(lista, i + 1, n)
    
def cambier_0(i, n, ele, lista):
    if i == n:
        return lista
    elif lista[i] == ele:
        lista[i] = 0
    return cambier_0(i + 1, n, ele, lista)

def cuente(i, n, ele, lista, cuantos):
    if i == n:
        return cuantos
    elif lista[i] == ele:
        cuantos += 1
    return cuente(i + 1, n, ele, lista, cuantos)

# Parte b. Iteracion

def cambie_i(lista):
    if  lista != []:
        i = 0
        n = len(lista)
        for i in range(n):
            if not isinstance(lista[i], int):
                return "Error"
            if cuente(i, n, lista[i], lista, 0) >= 2:
                lista = cambiei_0(i, n, lista[i], lista)
        return lista
    else:
        return "Error"

def cambiei_0(i, n, ele, lista):
    for i in range(n):
        if lista[i] == ele:
            lista[i] = 0
    return lista

# Pregunta 3
# E: lista
# S: (velocidades mas de 300, velocidades menos 300, mayor, menor, promedio)
# R: lista no nula

def velocidades(lista):
    if lista != []:
        return velocidades_aux(lista, 0, 0, lista[0], lista[0], 0)
    else:
        return "Error"

def velocidades_aux(lista, mas, menos, mayor, menor, suma):
    if lista == []:
        return mas, menos, mayor, menor, suma / (mas + menos)
    if lista[0] > 300:
        mas += 1
    else:
        menos += 1
    if lista[0] > mayor:
        mayor = lista[0]
    if lista[0] < menor:
        menor = lista[0]
    return velocidades_aux(lista[1:], mas, menos, mayor, menor, suma + lista[0])


# Pregunta 4

#E: Una matriz
#S: Boolean indicando si es una matriz semi mágica
#R:

def semi_magica(matriz):
   n = len(matriz)
   m = len(matriz[0])
   sumas = suma_filas(matriz, m, n, 0, 0, [], 0)
   return magico(sumas, n, 1, sumas[0])

def suma_filas(matriz, m, n, i, j, suma, fila):
   if n == i:
      return suma
   elif m == j:
      suma.append(fila)
      return suma_filas(matriz, m, n, i+1, 0, suma, 0)
   else:
      return suma_filas(matriz, m, n, i, j+1, suma, fila + matriz[i][j])

def magico(sumas, n, i, anterior):
   if n == i:
      return True
   elif sumas[i] != anterior:
      return False
   else:
      return magico(sumas, n, i+1, sumas[i])

# ---- CASOS DE PRUEBA ----------------
print("Pregunta 1:")
print("split(123029201034)  Correcto: [123,292,1,34] Retorna: ",split(123029201034))
print("split(89762931)      Correcto: [89762931]     Retorna: ",split(89762931))
print("split(12000000)      Correcto: [12]           Retorna: ",split(12000000))
print("split(120)           Correcto: [12]           Retorna: ",split(120))
print("split(-20)           Correcto: [2]            Retorna: ",split(-20))
print("split(1200045)       Correcto: [12, 45]       Retorna: ",split(1200045))
print("split(0)             Correcto: []             Retorna: ",split(0))
print("------------------------------------------------------------")
print("Pregunta 2:")        
print("cambie_r([12,5,31,5,1])    Correcto: [12,0,31,0,1]    Retorna: ",cambie_r([12,5,31,5,1]))
print("cambie_r([2,4,3,1,5,10])   Correcto: [2,4,3,1,5,10]   Retorna: ",cambie_r([2,4,3,1,5,10]))
print("cambie_r([2,2,5,5])        Correcto: [0,0,0,0]        Retorna: ",cambie_r([2,2,5,5]))
print("cambie_r([2,5,2,5])        Correcto: [0,0,0,0]        Retorna: ",cambie_r([2,5,2,5]))
print("cambie_r([2,2,5,'5'])      Correcto: Error            Retorna: ",cambie_r([2,2,5,'5']))
print("------------------------------------------------------------")
print("cambie_i([12,5,31,5,1])    Correcto: [12,0,31,0,1]    Retorna: ",cambie_i([12,5,31,5,1]))
print("cambie_i([2,4,3,1,5,10])   Correcto: [2,4,3,1,5,10]   Retorna: ",cambie_i([2,4,3,1,5,10]))
print("cambie_i([2,2,5,5])        Correcto: [0,0,0,0]        Retorna: ",cambie_i([2,2,5,5]))
print("cambie_i([2,5,2,5])        Correcto: [0,0,0,0]        Retorna: ",cambie_i([2,5,2,5]))
print("cambie_i([2,2,5,'5'])      Correcto: Error            Retorna: ",cambie_i([2,2,5,'5']))
print("------------------------------------------------------------")
# Pregunta 3
print("velocidades([350, 250, 300, 350])")
print("Correcto:  (2, 2, 350, 250, 312.5)")
print("Retorna:  ",velocidades([350, 250, 300, 350]))
print("velocidades([325, 312, 298, 300, 279, 308, 264])")
print("Correcto:  (3, 4, 325, 264, 298.0")
print("Retorna:  ",velocidades([325, 312, 298, 300, 279, 308, 264]))
print("velocidades([])       Correcto: Error       Retorna: ",velocidades([]))
print("------------------------------------------------------------")
# Pregunta 4
print("semi([[6,2,1],[5,4,0],[7,1,1]])  Correcto: True    Retorna: ",semi_magica([[6,2,1],[5,4,0],[7,1,1]]))
print("semi([[6,2,1],[5,4,0],[7,1,2]])  Correcto: False   Retorna: ",semi_magica([[6,2,1],[5,4,0],[7,1,2]]))
print("semi([[6,2],[5,4],[7,1]])        Correcto: False   Retorna: ",semi_magica([[6,2],[5,4],[7,1]]))
print("semi([[6,2,1,3],[5,4,0,3],[7,1,2,2],[0,0,0,12])  Correcto: True   Retorna: ",semi_magica([[6,2,1,3],[5,4,0,3],[7,1,2,2],[0,0,0,12]]))
