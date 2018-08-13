from tkinter import *
import tkinter

'''
def load_img(name):
    path=os.path.join("imgs",name)
    img = PhotoImage(file=path)
    return img
'''
global V2 , main
############################################################
def getTextField():
    texto=data.get()
    global tiempo
    try:
        xint = (int)(texto)
        Label(Canvas1,text="You have confirmed!",bg="#cdc7c9",font=10).place(x=320,y=50)
        tiempo = (xint//100)*60 + xint%100
        
    except:
        Label(Canvas1,text="You shall not pass!",bg="#cdc7c9",font=10).place(x=320,y=50)
        
def abrirV2():
    global main
    main.withdraw()
    Ventana2()

def inicio():
    global main
    main = Tk()
    main.title("Taller de Tkinter")
    main.minsize(750,450)
    main.resizable(width= False, height=False)

    Canvas1 = tkinter.Canvas(main,width=800,height=500)
    Canvas1.place(x=0,y=0)
    Titulo= Label(Canvas1, text="Welcome to Tkinter",bg="#20B2A9",fg = "#000000", font=180).place(x=325,y=25)

    data = StringVar()
    textField = Entry(Canvas1,textvariable=data).place(x=550,y=400)

    bget=Button(Canvas1,text="Press me!",command=getTextField).place(x=675,y=400)

    Mover=Button(Canvas1, text="Ventana2",command=abrirV2).place(x=675,y=250)

    Canvas1.focus_set()
    main.mainloop()  


####################################################
def regresar_inicio():
    global main , V2
    V2.destroy()
    main.deiconify()
    
def Ventana2():
    global V2
    V2 = Toplevel()
    V2.title( 'Ventana 2')
    V2.minsize(800,500)
    V2.resizable(width= False, height=False)
    V2.focus_force()

    V2.protocol("WM_DELETE_WINDOW",lambda:regresar_inicio())
    V2.mainloop()





inicio()
