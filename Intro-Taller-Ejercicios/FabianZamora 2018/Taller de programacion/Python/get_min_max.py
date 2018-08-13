# Obtiene el minimo y el maximo de una lista
# E: una lista con 4 numeros
# S: una tupla (min, max) o None en caso de error
# R: la lista debe tener 4 numeros
def get_min_max(lista):
 
    # Obtengo los valores min y max.
    # Estos valores, segund las otras funciones,
    # Pueden ser None en caso de que la lista
    # ingresada
    # Sea incorrecta
    min_val = get_min(lista)
    max_val = get_max(lista)
    if min_val == None or max_val == None:
        print("entrada invalida")
        return None
    return min_val, max_val, 3, 4

# Obtiene el maximo de una lista de 4 numeros
# E: una lista de 4 numeros
# S: el elemento mayor o None si hubo error.
# R: la lista debe contener 4 elementos
def get_max(lista):
    if isinstance(lista, list) and len(lista)==4:
        mayor = lista[0]
        if mayor < lista[1]:
            mayor = lista[1]
        if mayor < lista[2]:
            mayor = lista[2]
        if mayor < lista[3]:
            mayor = lista[3]
        return mayor
    else:
        return None


# Busca el mayor de una lista e imprime un mensaje
# En case de que este sea mayor que 10
# E: tiene que ser una lista con 4 numeros
def verifica_max(lista):
    mayor = get_max(lista)
    if mayor == None:
        print("Entrada invalida")
    else:
        if mayor > 100:
            print("es mayor a 100")
        elif mayor > 50:
            print("es mayor a 50")
        else:
            print("no es mayor a 50")
                    
# Obtiene el minimo de una lista de 4 numeros
# E: una lista de 4 numeros
# S: el elemento menor o None en caso de error
# R: la lista debe contener 4 elementos
def get_min(lista):
    if isinstance(lista, list) and len(lista) == 4:
        menor2 = lista[0]
        if menor2 > lista[1]:
            menor2 = lista[1]
        if menor2 > lista[2]:
            menor2 = lista[2]
        if menor2 > lista[3]:
            menor2 = lista[3]
        return menor2
    else:
        return None


def multiplicador():
    numero = input("Deme un numero menor a 100")
    numero = int(numero)
    if isinstance(numero, int):
        if numero < 100:
            print("Numero:", numero * 3)
            multiplicador()
        else:
            multiplicador()
    else:
        print("Error, adios...")
