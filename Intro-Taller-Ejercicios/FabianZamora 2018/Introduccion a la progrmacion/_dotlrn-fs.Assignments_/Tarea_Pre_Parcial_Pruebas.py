#___________________________________________________________________

fallidas = 0
exitosas = 0


fallidas_total = 0
exitosas_total = 0

try:
    if natural([3, 4, 5, 1, 2, 3, 4, 7, 3, 2, 1]) == [[3, 4, 5], [1, 2, 3, 4, 7], [3], [2], [1]]:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if natural([3, 4, 5, 1, 2, 3, 4, 7, 3, 2, 1]) == [[3, 4, 5], [1, 2, 3, 4, 7], [3], [2], [1]]:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if natural(2) == None:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1
    
print("Problema 1: ", exitosas, fallidas)
exitosas = 0
fallidas = 0

try:
    if elimine([4,8,2,4,0,1], 4) == [4,8,2,0,1]:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if elimine([3, 4, 5, 1, 2, 3, 4, 7, 3, 2, 1],9) == [3, 4, 5, 1, 2, 3, 4, 7, 3, 2, 1]:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if elimine(243,3) == None:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

print("Problema 2: ",exitosas, fallidas)
exitosas = 0
fallidas = 0

try:
    if revise_num(482401) == (5,1):
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if revise_num(4) == (1,0):
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if revise_num("a") == None:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

print("Problema 3: ",exitosas, fallidas)
exitosas = 0
fallidas = 0

try:
    if intersec([1,2,3], [6,9,2]) == [2]:
        exitosas += 1
        exitosas_total += 1
        
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if intersec([4,3],[2,0]) == []:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if intersec([4,3],2) == None:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

print("Problema 4: ",exitosas, fallidas)
exitosas = 0
fallidas = 0

try:
    if salarios([1000000,470000,2500000]) == [1, 2, 1323333]:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if salarios(1000000) == None:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

try:
    if salarios([2500000]) == [0, 1, 2500000]:
        exitosas += 1
        exitosas_total += 1
    else:
        fallidas += 1
        fallidas_total += 1
except:
    fallidas += 1
    fallidas_total += 1

print("Problema 5: ",exitosas, fallidas)
print("Total Exitosas: ",exitosas_total)
print("Total Fallidas: ",fallidas_total)
print("Nota obtenida: ",exitosas_total/15*100)

