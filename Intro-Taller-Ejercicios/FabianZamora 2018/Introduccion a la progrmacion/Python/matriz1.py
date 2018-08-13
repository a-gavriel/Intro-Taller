

# matriz = [[1,2,3], [4,5,6], [7,8,9]]

def debug(matriz):
    print("La matriz es:")
    for fila in range(len(matriz)):
        print(" ")
        for columna in range(len(matriz[0])):
            elem = matriz[fila][columna]
            print(elem," ", end="")
    print(" ")

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

debug(matriz)

tmp = matriz[0][0]
matriz[0][0] = matriz[2][2]
matriz[2][2] = tmp

debug(matriz)






            
