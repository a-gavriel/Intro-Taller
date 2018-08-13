from tkinter import *

# http://effbot.org/tkinterbook/grid.htm
# Tk() se utiliza para crear una ventana
# Toda aplicacion debe tener una ventana principal
# Todos los widgets deben pertenecer a un widget padre o una ventana
ventana = Tk()
ventana["bg"] = "#AAAAAA"
ventana.title("Taller programacion")
#ventana.minsize(width=300, height=300) # Cambia el tamano minimo de la ventana
#ventana.maxsize(width=400, height=400) # Cambia al tamano maximo de la ventana

# Existen varias formas de posicionar
# widgets dentro de su contenedor. Vamos a ver grid.
# Este metodo divide el padre en filas y columnas y posiciona los
# widgets en la fila y columna especificada
labelEmail = Label(ventana, text="Email")
labelEmail.grid(row=0, column=0, sticky=W)

# sticky dice la posicion dentro de la celda.
# posibles valores: N, S, E, W
labelPassword = Label(ventana, text="Password")
labelPassword.grid(row=1, column=0, sticky="e")

entryEmail = Entry(ventana)
entryEmail.grid(row=0, column=1)

entryPassword = Entry(ventana)
entryPassword.grid(row=1, column=1)

buttonLogin = Button(ventana, text="Iniciar sesion")
buttonLogin.grid(row=2, column=1, sticky="e")

# http://effbot.org/tkinterbook/photoimage.htm
imgPathDefault = "/Users/fabian/Desktop/TKINTER/default.gif"
imgPathDenied = "/Users/fabian/Desktop/TKINTER/denied.gif"
imgPathSuccess = "/Users/fabian/Desktop/TKINTER/success.gif"
img = PhotoImage(file=imgPathDefault) # Debe guardarse en variable sino GC
labelImg = Label(ventana, image = img)
labelImg.image = img
labelImg.grid(row=0, column=2, columnspan=2, rowspan=2, sticky="nswe")

# Declaracion de funciones
def clickButtonLogin(evento):
    #Obtiene los valores ingresados por el usuario
    email = entryEmail.get()
    password = entryPassword.get()
    if email == "fzamora@itcr.ac.cr" and password == "1234":
        nimg = PhotoImage(file=imgPathSuccess)
        labelImg.configure(image=nimg)
        labelImg.image = nimg
    else:
        nimg = PhotoImage(file=imgPathDenied)
        labelImg.configure(image=nimg)
        labelImg.image = nimg

# Asignacion de eventos
buttonLogin.bind("<Button-1>", clickButtonLogin)

# Un programa por si solo no corre indefinidamente
# Se necesita tener un ciclo que este corriendo continuamente
# Esperando eventos del usuario. Esto es lo que se llama el mainLoop
ventana.mainloop()
