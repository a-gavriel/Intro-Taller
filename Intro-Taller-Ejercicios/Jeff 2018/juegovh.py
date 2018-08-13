# Juego Heroes vs Villanos
# Ejemplo POO

import random

# Clase Personaje:
# Atributos:
#  nombre: string
#  color: string
#  pts_vida: int
#######################
# Metodos:
# get_nombre()
# get_color()
# get_vida()
# set_vida()
# muestra_info()

class Personaje:
    nombre = ''
    color = ''
    pts_vida = 100

    def __init__(self, nombre, color, pts_vida):
        self.nombre = nombre
        self.color = color
        self.pts_vida = pts_vida

    def get_nombre(self):
        return self.nombre

    def get_color(self):
        return self.color

    def get_vida(self):
        return self.pts_vida

    def set_vida(self, ataque):
        self.pts_vida -= ataque
        return self.pts_vida

    def muestra_info(self):
        print("\n" + self.get_nombre() + ' ' + self.get_color())
        if self.get_vida() <= 0:
            print("MUERTO")
        else:
            print("Pts vida: " + str(self.get_vida()))

# Clase Juego:
# Atributos:
#  no tiene
#######################
# Metodos:
# set_heroe()
# set_villano()
# ataque_heroe()
# ataque_villano()
# ataque_random()

class Juego:

    heroe = None
    villano = None

    def set_heroe(self, nombre, color, pts_vida):
        self.heroe = Personaje(nombre, color, pts_vida)
        self.heroe.muestra_info()

    def set_villano(self, nombre, color, pts_vida):
        self.villano = Personaje(nombre, color, pts_vida)
        self.villano.muestra_info()

    def ataque_heroe(self):
        ataque = random.randint(0, 50) # ataque aleatorio entre 0 y 50
        print(self.heroe.get_nombre() + " realiza un ataque de: " +  str(ataque) + " a " + self.villano.get_nombre())
        self.villano.set_vida(ataque)
        self.villano.muestra_info()

    def ataque_villano(self):
        ataque = random.randint(0, 40)
        print("\n" + self.villano.get_nombre() + " realiza un ataque de: " +  str(ataque) + " a " + self.heroe.get_nombre())
        self.heroe.set_vida(ataque)
        self.heroe.muestra_info()

    def ataque_random(self):
        if random.randint(0, 1) == 0:
            self.ataque_heroe()
        else:
            self.ataque_villano()

# .... JUEGO ......

juego = Juego()
juego.set_heroe('Mario', 'amarillo', 100)
juego.set_villano('Bowser', 'azul', 200)
juego.ataque_heroe()
juego.ataque_heroe()
juego.ataque_heroe()
# El juego puede continuar con diferentes ataques - PROBAR!!
