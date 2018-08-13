import os.path 

# Genera el path del archivo
csv_path = os.path.join(os.getcwd(), 'example.csv')

# Revisa si el archivo existe
if os.path.exists(csv_path):

    # El archivo existe, entonces lo abre
    with open(csv_path) as csv_file:

        # Carga todas las lineas en una lista
        lines = csv_file.read().splitlines()
        print("Todas las lineas:", lines)
        print("Adivinen:", lines[0].split(','))
else:
    print('No encuentro el archivo example.csv!!!')

