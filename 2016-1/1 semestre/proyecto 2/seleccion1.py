from tkinter import *
from random import uniform
import os , random , tkinter


global equipo1
equipo1 = [['01', 'bale'], ['05', 'cristiano ronaldo'], ['09', 'gotze'], ['13', 'lahm'], ['17', 'neuer'], ['21', 'rakitic'], ['25', 'suarez']]
player1 = []
#------------------------------------------------------------------#

def cambio_str(N):
    R = ''
    cont = 0
    for a in range(len(N)):
        b = str(N[a])
        c = str (cont) + b[8:-2] + '\n'
        R = R + c
        cont +=1
    return R


#------------------------------------------------------------------#

def button_listener(id):
    if id == 0:
        None
    elif id == 30:
        player = random.choice([True,False])
    elif id == 31:
        seleccion1.destroy()
        real()
    elif id == 32:
        seleccion1.destroy()
        barc()
    elif id == 33:
        seleccion1.destroy()
        manc()
    elif id == 34:
        seleccion1.destroy()
        chel()
        
    

#------------------------------------------------------------------#

    
    


def real():
    global equipo1
    real = Tk()
    real.geometry("800x600+250+50")
    
    S = Scrollbar(real)
    T = Text(real, height=20, width=50)
    S.pack(side=RIGHT, fill = Y)
    T.pack(side=LEFT , fill = Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = cambio_str(equipo1)
    T.insert(END, quote)
    
    e = Entry(real)
    e.pack()
    e.focus_set()

    def player1team():
        global player1 , equipo1
        print (e.get())
        num = int (e.get())
        print (num)
        player1.append(equipo1[num])
        print (equipo1[num])
        print (player1)
        e.delete(0, END)

    b = Button(real, text="Choose player number", width=30, command=player1team).place(x=500,y=50)
    #b.pack()
    mainloop()
    
    e = Entry(real, width=50)
    e.pack()
    text = e.get()
        



seleccion1 = Tk()
seleccion1.title('Penales Futbol')
seleccion1.minsize(800,600)
seleccion1.resizable(width= False, height=False)

seleccion1c = tkinter.Canvas(seleccion1,width=800,height=600,bg='blue')
seleccion1c.place(x=0,y=0)


eq1 = Button(seleccion1c,text='Real Madrid',width=10,height=2,command=lambda:button_listener(31)).place(x=100,y=500)
eq2 = Button(seleccion1c,text='Barcelona',width=10,height=2,command=lambda:button_listener(32)).place(x=200,y=500)
eq3 = Button(seleccion1c,text='Manchester United',width=10,height=2,command=lambda:button_listener(33)).place(x=300,y=500)
eq4 = Button(seleccion1c,text='Chelsea',width=10,height=2,command=lambda:button_listener(34)).place(x=400,y=500)



seleccion1.mainloop()
