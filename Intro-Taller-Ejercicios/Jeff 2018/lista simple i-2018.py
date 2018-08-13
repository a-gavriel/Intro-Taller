class Nodo:
    def __init__(self, valor=None):
        self.next = Nobe
        self.valor = valor

    def __str__(self):
        return str(self.valor)

    def get_valor(self):
        return self.valor

class Lista:
    def __init__(self):
        self.largo = 0
        self.head = None
        
    def __len__(self):
        return self.largo
    
    def insertar(self, dato):
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

    def suma(self):
        result = 0
        nodo = self.head
        while nodo != None:
            result += nodo.valor
            nodo = nodo.next
        return result

    def sumar(self):
        result = 0
        nodo = self.head
        return self.sumar_aux(nodo, result)

    def sumar_aux(self, nodo, result):
        if nodo == None:
            return result
        else:
            return self.sumar_aux(nodo.next, result + nodo.valor)

    def printL(self):
        nodo = self.head
        print('[', end = '')
        if nodo != None:
            print(nodo, end = '')
            nodo = nodo.next
        while nodo != None:
            print(',' ,nodo.__str__(), end = '')
            nodo = nodo.next
        print(']')
    def find(self, dato):
        i = 0
        nodo = self.head
        result=-1
        while nodo != None:
            if nodo.valor == dato:
                result = i
            nodo = nodo.next
            i+=1
        return result

    def index(self, i):
        indice = 0
        nodo = self.head
        res = "Fuera de Rango"
        while nodo != None:
            if indice == i:
                res = nodo.valor
            indice+=1
            nodo = nodo.next
        return res

    def delete(self, valor):
        if self.head == None:
            return "Lista vacía :(("
        elif self.head.valor == valor:
            self.head = self.head.next
        else:
            booli = False
            nodo = self.head
            while nodo.next != None:
                if nodo.next.valor == valor:
                    booli = True
                    nodo.next = nodo.next.next
                else:
                    nodo = nodo.next
            if booli ==  False:
                return "No se encuentra"
            

            
                    
        
