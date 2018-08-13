import os.path 

# Genera el path del archivo
path_del_archivo = os.path.join(os.getcwd(), 'example.txt')

lineas_del_archivo = []

# Revisa si el archivo existe
if os.path.exists(path_del_archivo):

    # El archivo existe, entonces lo abre
    # Carga todas las lineas en una lista
    mi_archivo = open(path_del_archivo)
    lineas_del_archivo = mi_archivo.read().splitlines()
    print("Todas las lineas:", lineas_del_archivo)
    print("Adivinen:", lineas_del_archivo[0].split(','))
        
else:
    print('No encuentro el archivo example.csv!!!')


from tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

def agregar_contactos_en_lista(contactos):
    if contactos == []:
        return None
    listbox.insert(END, contactos[0])
    return agregar_contactos_en_lista(contactos[1:])

agregar_contactos_en_lista(lineas_del_archivo)
                                      
def muestra_seleccionado():
    posiciones_seleccionadas = listbox.curselection()
    posicion = posiciones_seleccionadas[0]
    print(lineas_del_archivo[posicion])
    
button = Button(master, text='Deme seleccionado', command=muestra_seleccionado)
button.pack()

mainloop()
