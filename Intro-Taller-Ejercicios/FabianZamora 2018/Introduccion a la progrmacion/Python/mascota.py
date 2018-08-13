# Representacion de una mascota
class Mascota:

    # Constructor. Se llama cada vez que se crea una nueva instancia
    def __init__(self, nombre, edad, raza):
        # Asigna los atributos
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def hablar(self):
        print("Laughs in spanish")

# Clase Perro que hereda de mascota
class Perro(Mascota):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def guardar_correo(self, correo):
        self.correo = correo

    def guardar_telefono(self, tel):
        self.tel = tel

    

    
