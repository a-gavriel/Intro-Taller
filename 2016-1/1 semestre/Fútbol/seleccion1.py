from tkinter import *
from random import uniform
import os , random , tkinter


#global equipo1 , equipo2, equipo3, equipo4
#equipo1 = [['01', 'bale'], ['05', 'cristiano ronaldo'], ['09', 'gotze'], ['13', 'lahm'], ['17', 'neuer'], ['21', 'rakitic'], ['25', 'suarez']]
#equipo2 = [['02', 'benzema'], ['06', 'david'], ['10', 'iniesta'], ['14', 'messi'], ['18', 'neymar'], ['22', 'reus'], ['26', 'torres']]
#equipo3 = [['03', 'boateng'], ['07', 'david luiz'], ['11', 'isco'], ['15', 'modric'], ['19', 'pirlo'], ['23', 'robin'], ['27', 'xabi']]
#equipo4 = [['04', 'celso'], ['08', 'douglas'], ['12', 'james'], ['16', 'muller'], ['20', 'pogba'], ['24', 'sergio'], ['28', 'xavi']]
player1 = []

configuration3 = { #Contiene archivos para usarlos en las ventanas
    "Files" : {
        "images" : {
            "background" : "Files/images/background.gif",
            "icon" : "Files/images/icon.ico",
            "USA" : "Files/images/USA.gif",
            "CR" : "Files/images/CR.gif",
            "gamebg" : "Files/images/gamebg.gif",
            "Yendry" : "Files/images/Árbitros/Yendry.gif",
            "Alexis" : "Files/images/Árbitros/Alexis.gif",
            "playbg" : "Files/images/playbg.gif"
        }
    }
}   

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
        
    
def load_image(path):   #Función para cargar las imágenes
    img = PhotoImage(file = path)
    return img


#------------------------------------------------------------------#

    
    


def real():
    global equipo1
    real = Tk()
    real.geometry("800x600+250+50")
    real.iconbitmap(configuration3["Files"]["images"]["icon"])
    real.config(bg="black")
    
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
        #print (e.get())
        num = int (e.get())
        #print (num)
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

def barc():
    global equipo2
    barc = Tk()
    barc.geometry("800x600+250+50")
    barc.iconbitmap(configuration3["Files"]["images"]["icon"])
    barc.config(bg="black")
    
    S = Scrollbar(barc)
    T = Text(barc, height=20, width=50)
    S.pack(side=RIGHT, fill = Y)
    T.pack(side=LEFT , fill = Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = cambio_str(equipo2)
    T.insert(END, quote)
    
    e = Entry(barc)
    e.pack()
    e.focus_set()

    def player1team():
        global player1 , equipo2
        #print (e.get())
        num = int (e.get())
        #print (num)
        player1.append(equipo2[num])
        print (equipo2[num])
        print (player1)
        e.delete(0, END)

    b = Button(barc, text="Choose player number", width=30, command=player1team).place(x=500,y=50)
    #b.pack()
    mainloop()
    
    e = Entry(barc, width=50)
    e.pack()
    text = e.get()

def manc():
    global equipo3
    manc = Tk()
    manc.geometry("800x600+250+50")
    manc.iconbitmap(configuration3["Files"]["images"]["icon"])
    manc.config(bg="black")
    
    S = Scrollbar(manc)
    T = Text(manc, height=20, width=50)
    S.pack(side=RIGHT, fill = Y)
    T.pack(side=LEFT , fill = Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = cambio_str(equipo3)
    T.insert(END, quote)
    
    e = Entry(manc)
    e.pack()
    e.focus_set()

    def player1team():
        global player1 , equipo3
        #print (e.get())
        num = int (e.get())
        #print (num)
        player1.append(equipo3[num])
        print (equipo3[num])
        print (player1)
        e.delete(0, END)

    b = Button(manc, text="Choose player number", width=30, command=player1team).place(x=500,y=50)
    #b.pack()
    mainloop()
    
    e = Entry(manc, width=50)
    e.pack()
    text = e.get()        

def chel():
    global equipo4
    chel = Tk()
    chel.geometry("800x600+250+50")
    chel.iconbitmap(configuration3["Files"]["images"]["icon"])
    chel.config(bg="black")
    
    S = Scrollbar(chel)
    T = Text(chel, height=20, width=50)
    S.pack(side=RIGHT, fill = Y)
    T.pack(side=LEFT , fill = Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = cambio_str(equipo4)
    T.insert(END, quote)
    
    e = Entry(chel)
    e.pack()
    e.focus_set()

    def player1team():
        global player1 , equipo4
        #print (e.get())
        num = int (e.get())
        #print (num)
        player1.append(equipo4[num])
        print (equipo4[num])
        print (player1)
        e.delete(0, END)

    b = Button(chel, text="Choose player number", width=30, command=player1team).place(x=500,y=50)
    #b.pack()
    mainloop()
    
    e = Entry(chel, width=50)
    e.pack()
    text = e.get()

seleccion1 = Tk()
seleccion1.title('Penales Futbol')
seleccion1.minsize(800,600)
seleccion1.resizable(width= False, height=False)
seleccion1.iconbitmap(configuration3["Files"]["images"]["icon"])

fondo_imagen = load_image(configuration3["Files"]["images"]["playbg"])

seleccion1c = tkinter.Canvas(seleccion1,width=800,height=600,bg='blue')
seleccion1c.place(x=0,y=0)
seleccion1c.create_image(400,300,image=fondo_imagen)


eq1 = Button(seleccion1c,text='Real Madrid',width=12,height=3,command=lambda:button_listener(31)).place(x=100,y=500)
eq2 = Button(seleccion1c,text='Barcelona',width=12,height=3,command=lambda:button_listener(32)).place(x=250,y=500)
eq3 = Button(seleccion1c,text='Manchester\nUnited',width=12,height=3,command=lambda:button_listener(33)).place(x=400,y=500)
eq4 = Button(seleccion1c,text='Chelsea',width=12,height=3,command=lambda:button_listener(34)).place(x=550,y=500)



seleccion1.mainloop()
