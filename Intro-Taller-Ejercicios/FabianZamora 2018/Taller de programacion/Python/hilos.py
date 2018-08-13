
import threading
import time

def trabaja():
    print("Comenzado a trabajar...")
    time.sleep(10)
    print("Terminando de trabajar...")

def trabaja_en_paralelo():
    w = threading.Thread(target=trabaja)
    w.start()
    
def imprime_lista(lista):
    for elem in lista:
        print(elem)
        time.sleep(1)

def imprime_lista_en_paralelo(lista):
    w = threading.Thread(target=imprime_lista, args=(lista,))
    w.start()
    

