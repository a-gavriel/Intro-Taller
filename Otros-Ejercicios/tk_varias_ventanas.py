import tkinter
from tkinter import*

def abrir1():
    b =Toplevel()
    imagen = PhotoImage(file= "Lab2-3.png")
    la = Label(b,image =imagen)
    la.image = imagen
    la.pack()

def abrir2():
    b =Toplevel()
    imagen = PhotoImage(file= "DiagramaBases.png")
    la = Label(b,image =imagen)
    la.image = imagen # keep a reference!
    la.pack() 


def main():
    a = Tk()
    canvas = Canvas(a, bg ="black",width = 512,height =512)
    canvas.pack()

    imagem = PhotoImage(file = "TareaBases.png")
    a1 = canvas.create_image(256,256,image = imagem)

    btu1 = Button(a,text ="Abri1!",command = abrir1)
    btu1.place(x = 150,y=400)
    btu2 = Button(a,text ="Abri2!",command = abrir2)
    btu2.place(x = 300,y=400)

main()