from persona import *

class Agenda:

    # Atributos
    contactos = []

    # Metodos

    def agregar(self, contacto):
        self.contactos += [contacto]

    def eliminar(self, criterio):
        print("Comenzamos a eliminar:", criterio)
        self.contactos = self.eliminar_aux(criterio, self.contactos,[])
    
    # Devuelve una lista con los contactos que NO hay que eliminar
    def eliminar_aux(self, criterio, tmpContactos, resultado):
        if tmpContactos == []:
            return resultado
        p = tmpContactos[0]
        if not criterio.lower() in p.getInfo().lower():
            resultado += [p]
        return self.eliminar_aux(criterio, tmpContactos[1:], resultado)
    
    def buscar(self, criterio):
        print("Comenzamos a buscar:", criterio)
        return self.buscar_aux(criterio, self.contactos, [])

    # Devuelve una lista con los contactos que hicieron Match
    def buscar_aux(self, criterio, tmpContactos, resultado):
        if tmpContactos == []:
            return resultado
        p = tmpContactos[0]
        if criterio.lower() in p.getInfo().lower():
            resultado += [p]
        return self.buscar_aux(criterio, tmpContactos[1:], resultado)
        
    def getInfo(self):
        print("Cantidad contactos:", len(self.contactos))
        self.getInfoAux(self.contactos)

    def getInfoAux(self, tmpContactos):
        if tmpContactos != []:
            p = tmpContactos[0]
            print(p.getInfo())
            self.getInfoAux(tmpContactos[1:])

    # Guarda en un archivo de texto
    #def guardarEnArchivo(self):
    #    archivo.write(p.getInfo)
    #def cargarDeArchivo(self):
        
        
# Instancia de agenda
agenda = Agenda()
agenda.getInfo() # Muestra 0 contactos

# Instancias de personas
saymon = Persona("Saymon","Astua","1234", "say@gmail.com")
agenda.agregar(saymon)

carlos = Persona("Carlos","Lara","5678", "carlos@gmail.com")
agenda.agregar(carlos)

anthony = Persona("Anthony","Acuna","9876", "anthony@hotmail.com")
agenda.agregar(anthony)

agenda.getInfo() # Muestra 3 contactos

agenda.buscar('Carlos')
agenda.buscar('saymon')

#agenda.eliminar('anthony')
#agenda.getInfo()
