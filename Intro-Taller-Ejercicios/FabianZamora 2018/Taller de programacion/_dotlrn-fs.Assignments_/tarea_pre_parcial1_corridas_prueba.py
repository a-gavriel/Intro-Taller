# INSTRUCCIONES:
# Copiar al final del archivo entregado y correr.

###############################
# [INICIO] CORRIDAS DE PRUEBA #
###############################
import sys

fallidas = 0
exitosas = 0

######### invertir(lista) ######

try:
    if invertir_pila([1,2,3]) == [3,2,1]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if invertir_pila([22,33,44,55]) == [55,44,33,22]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if invertir_pila([2]) == [2]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1
    
try:
    if invertir_cola([1,2,3]) == [3,2,1]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if invertir_cola([22,33,44,55]) == [55,44,33,22]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if invertir_cola([2]) == [2]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

######### cuente_pares_lista(lista) ######

try:
    if cuente_pares_lista([1, 4, [5, 2, [2,2,1]]]) == 4:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if cuente_pares_lista([1, 4, 10, 100, 3]) == 3:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if cuente_pares_lista([1, 4, [5, 2, [1, [8]]]]) == 3:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

######### son_amigos(a, b) ######

try:
    if son_amigos(220, 284) == True:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if son_amigos(220, 500) == False:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1
                         
######### separa(lista) ######

try:
    if separa(['a', 'e']) == [['e'], ['a']]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if separa(['a', 'b', 'c', 'd', 'e']) == [['b', 'd'], ['a', 'c', 'e']]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if separa([1,2,3,4]) == [[2,4], [1,3]]:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1


######### coincide(lista) ######

try:
    if coincide([2, 4, 3, 9, 14]) == True:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1


try:
    if coincide([5, 6, 14, 18, 20, 41]) == False:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1

try:
    if coincide([5, 6, -6, 5, 20, 41]) == True:
        exitosas += 1
    else:
        fallidas += 1
except Exception as e:
    print(e)
    fallidas += 1
                          
print('Pruebas exitosas:', exitosas)
print('Pruebas fallidas:', fallidas)
totales = fallidas + exitosas
print('NOTA FINAL:', exitosas * 100 / totales)

############################
# [FIN] CORRIDAS DE PRUEBA #
############################
