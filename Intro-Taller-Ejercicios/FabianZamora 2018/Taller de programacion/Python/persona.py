class Persona:

    # Se definen los atributos
    nombre=None
    apellido=None
    numero=None
    correo=None
    estado=None

    # Constructor
    def __init__(self, nombre, apellido, numero, correo=None):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.correo = correo

    def getInfo(self):
        info = self.nombre + " " + self.apellido + " " + self.numero
        if self.correo != None:
            info += (" " + self.correo)
        if self.estado != None:
            info += (" " + self.estado)
        return info
