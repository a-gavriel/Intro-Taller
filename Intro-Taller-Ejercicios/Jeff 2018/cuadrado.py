class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def getLado(self):
        return self.lado
    def setLado(self, nuevo):
        self.lado = nuevo
    def calculeArea(self):
        return self.lado ** 2
    def calculePerimetro(self):
        return self.lado * 4

c1 = Cuadrado(10)
c2 = Cuadrado(20)
c3 = Cuadrado(50)

lista = [c1, c2, c3]

def muestre_areas(lista):
    if lista == []:
        return 
    else:
        print(lista[0].getLado(),lista[0].calculeArea())
        return muestre_areas(lista[1:])

muestre_areas(lista)




    



    
