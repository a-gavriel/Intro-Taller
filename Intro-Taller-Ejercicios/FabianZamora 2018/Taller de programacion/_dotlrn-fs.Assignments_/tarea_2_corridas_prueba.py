# INSTRUCCIONES:
# Copiar al final del archivo entregado y correr.

###############################
# [INICIO] CORRIDAS DE PRUEBA #
###############################

fallidas = 0
exitosas = 0

######### suma_3_digitos ######

try:
    if suma_3_digitos(447) == 15:
        exitosas += 1
    else:
        fallidas += 1
except:
    fallidas += 1

try:
    if suma_3_digitos(747) == 18:
        exitosas += 1
    else:
        fallidas += 1
except:
    fallidas += 1

try:
    if suma_3_digitos(-747) == 4:
        exitosas += 1
    else:
        fallidas += 1
except:
    fallidas += 1

######### es_par_3 ######

try:
    if es_par_3(447) == False:
        exitosas += 1
    else:
        fallidas += 1
except:
    fallidas += 1

try:
    if es_par_3(747) == True:
        exitosas += 1
    else:
        fallidas += 1
except:
    fallidas += 1

try:
    if es_par_3(-747) == True:
        exitosas += 1
    else:
        fallidas += 1
except:
    fallidas += 1
    
print('Pruebas exitosas:', exitosas)
print('Pruebas fallidas:', fallidas)
totales = fallidas + exitosas
print('NOTA FINAL:', exitosas * 100 / totales)

############################
# [FIN] CORRIDAS DE PRUEBA #
############################
