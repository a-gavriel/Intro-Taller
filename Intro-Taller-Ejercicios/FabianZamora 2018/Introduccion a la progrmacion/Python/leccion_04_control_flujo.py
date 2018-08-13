# Introduccion a la programacion. Grupo 5.
# Control de flujo con if/elif/else

# Ejemplo que determina el estado final del curso
# segun la nota obtenida
nota_curso = 60
if nota_curso >= 67.5:
    print("Aprobado")
elif nota_curso >= 67.5:
    print("Reprobado")

if nota_curso >=70:
    print("mayor a 70")

# Determina si entra o no a la fiesta
# Indicando por que no pudo entrar
# Las expresiones if y elif validan un boolean
# if (boolean):
# elif (boolean):
trajo_comida = False
trajo_refresco = False
if trajo_comida and trajo_refresco:
    print("Entre porque trajo comida y refresco")
elif trajo_comida and not trajo_refresco:
    print("No entra porque no trajo refresco")
elif trajo_refresco and not trajo_comida:
    print("No entra porque no trajo comida")
else:
    print("No entra porque no trajo nada")

# El if/elif tambien puede recibir una expresion que genera un
# valor booleano. Por ejemplo:
# if numero >= 10
# if numero == 100
# if numero < 100 and numero > 50
if trajo_comida==True and trajo_refresco==True:
    print("Entre porque trajo comida y refresco")
elif trajo_comida==True and trajo_refresco==False:
    print("No entra porque no trajo refresco")
elif trajo_refresco==True and trajo_comida==False:
    print("No entra porque no trajo comida")
else:
    print("No entra porque no trajo nada")

# Condicional con mismo resultado pero diferente logica
# A los anteriores
if trajo_comida and trajo_refresco:
    print("Entre porque trajo comida y refresco")
elif trajo_comida:
    print("No entra porque no trajo refresco")
elif trajo_refresco:
    print("No entra porque no trajo comida")
else:
    print("No entra porque no trajo nada")
    


