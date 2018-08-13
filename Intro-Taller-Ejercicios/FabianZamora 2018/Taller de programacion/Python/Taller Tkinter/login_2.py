from tkinter import *

# Creamos nuestra ventana principal
ventana = Tk()
ventana.title("Login taller")
#ventana.minsize(width=200, height=300)
#ventana.maxsize(width=200, height=300)

# Se crea un label y se le enviar el contenedor
labelEmail = Label(ventana, text="Email")
labelEmail.grid(row=0, column=0, sticky="e")

labelPassword = Label(ventana, text="Password")
labelPassword.grid(row=1, column=0)

entryEmail = Entry(ventana, width=15)
entryEmail.grid(row=0, column=1)

entryPassword = Entry(ventana, width=15)
entryPassword.grid(row=1, column=1)

buttonLogin = Button(ventana, text="Login")
buttonLogin.grid(row=2, column=1, sticky="e")

# La ubicacion de las imagenes en la computadora
imgDefaultPath = "/Users/fabian/Desktop/TKINTER/default.gif"
imgSuccessPath = "/Users/fabian/Desktop/TKINTER/success.gif"
imgFailurePath = "/Users/fabian/Desktop/TKINTER/failure.gif"
# Esta linea carga la imagen desde el archivo
img = PhotoImage(file=imgDefaultPath)
#Ahora se crea el label y se le indica que muestre
#La imagen
labelIcono = Label(ventana, image=img, width=100, height=100)
labelIcono.grid(row=0, column=2)
labelIcono["bg"] = "#0FF"

#Agregamos un evento al boton
def clickButtonLogin(evento):
    print("Click en el boton")

buttonLogin.bind("<Button-1>", clickButtonLogin)

