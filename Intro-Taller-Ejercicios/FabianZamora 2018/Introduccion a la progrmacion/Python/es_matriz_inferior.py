
def es_matriz_inferior(m):
    #Asumimos que es cuadrada
    for indiceA in range(0, len(m)):
        print('Fila', indiceA)
        for indiceB in range(indiceA+1, len(m)):
            print('Col', indiceB)
            if m[indiceA][indiceB] != 0:
                return False
    return True


m1 = [[1,0,0,0],
      [2,1,0,0],
      [3,2,1,0],
      [4,5,6,7]]

m2 = [[11,12,13],
      [14,15,16],
      [17,18,19]]

m2_2 = [[13,12,11],
        [16,15,14],
        [19,18,17]]

def invierte_fila(fila):
    iIzq = 0
    iDer = len(fila)-1
    while iIzq < iDer:
        tmp = fila[iIzq]
        fila[iIzq] = fila[iDer]
        fila[iDer] = tmp
        iDer -= 1
        iIzq += 1

def invierte_matriz(m):
    for fila in m:
        invierte_fila(fila)
        
#print(es_matriz_inferior(m2))

fila1 = [1,2,3,4]
print(fila1)
invierte_fila(fila1)
print(fila1)

invierte_matriz(m2_2)
print(m2_2)
