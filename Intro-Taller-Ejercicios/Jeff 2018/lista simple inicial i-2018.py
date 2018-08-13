class Nodo:
    def __init__(self, valor):
        self.next = None
        self.valor = valor

    def __str__(self):
        return str(self.valor)

class Lista:
    def __init__(self):
        self.largo = 0
        self.head = None
        
    def __len__(self):
        return self.largo
    
    def appe(self, dato):
        if isinstance(dato, int):
            self.largo += 1
            if self.head == None :
                self.head = Nodo(valor = dato)
            else:
                tmp = self.head
                while tmp.next != None :
                    tmp = tmp.next
                tmp.next = Nodo(valor = dato)
        else:
            print("Error")

    def printL(self):
        nodo = self.head
        while nodo != None:
            print(nodo.__str__())
            nodo = nodo.next
        
