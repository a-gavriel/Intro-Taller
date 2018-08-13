class Nodo:
    def __init__(self, next=None, prev=None, valor=None):
        self.next = next
        self.prev = prev
        self.valor = valor

    def __str__(self):
        return str(self.valor)

class Lista:
    def __init__(self):
        self.largo = 0
        self.head = None
        self.tail = None
        
    def __len__(self):
        return self.largo
    
    def appe(self, dato):
        if isinstance(dato, int):
            self.largo += 1
            if self.head == None :
                self.head = Nodo(valor = dato)
                self.tail = self.head
            else:
                tmp = self.tail
                ant = tmp
                tmp.next = Nodo(valor = dato)
                tmp = tmp.next
                tmp.prev = ant
                self.tail = tmp
        else:
            print("Error")

    def printL(self):
        nodo = self.head
        print('[', end = '')

        if nodo != None:
            print(nodo.__str__(), end = '')
            nodo = nodo.next
        while nodo != None:
            print(',' ,nodo.__str__(), end = '')
            nodo = nodo.next
        print(']')

    def rprintL(self):
        nodo = self.tail
        print('[', end = '')
        if nodo != None:
            print(nodo.__str__(), end = '')
            nodo = nodo.prev
        while nodo != None:
            print(',' ,nodo.__str__(), end = '')
            nodo = nodo.prev
        print(']')
