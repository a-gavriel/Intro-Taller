
'''



'''

import tkinter
from tkinter import *
from threading import Thread
import time
import os
import winsound
import random

def load_img(name):
    path=os.path.join("imgs",name)
    img = PhotoImage(file=path)
    return img

#######Ventana about
def about():
    inicio.withdraw()
    about = Toplevel()
    about.title("About")
    about.resizable(width=False,height=False)
    about.geometry("800x600")
    about_canvas = tkinter.Canvas(about,width=800,height=600)
    about_canvas.place(x=0,y=0) 



    def close_about():
        inicio.deiconify()
        about.destroy()
    b_ini=Button(about, text=" Back ", font=21, command=close_about).place(x=160,y=500)            
        

    about.protocol("WM_DELETE_WINDOW", close_about)


    about.mainloop()




######Ventana Puntuacion
def scores():
    
	inicio.withdraw()
	scores = Toplevel()
	scores.title("Highscores")
	scores.resizable(width=False,height=False)
	scores.geometry("800x600")
	scores_canvas = tkinter.Canvas(scores,width=800,height=600)
	scores_canvas.place(x=0,y=0)    



    def close_scores():
  #      arch1.close()
        scores.destroy()
        inicio.deiconify()   

    b_ini=Button(scores, text=" Back ", font=21, command=close_scores).place(x=160,y=500)    

    scores.protocol("WM_DELETE_WINDOW", close_scores)

    scores.mainloop()


######Ventana jugadores


def jugadores():

    inicio.withdraw()
    jugadores = Toplevel()
    jugadores.title("Players")
    jugadores.resizable(width=False,height=False)
    jugadores.geometry("800x600")
    jugadores_canvas = tkinter.Canvas(jugadores,width=800,height=600,bg ="black")
    jugadores_canvas.place(x=0,y=0)

	data = StringVar()
	textField = Entry(jugadores_canvas,textvariable=data).place(x=160,y=400)

    equipo1 = load_img('equipo1.png')
    equipo2 = load_img('equipo2.png')
    equipo3 = load_img('equipo3.png')
    equipo4 = load_img('equipo4.png')

    def equipo1():
        equipo1 = Toplevel()
        equipo1.title("Real Madrid")
        equipo1.resizable(width=False,height=False)
        equipo1.geometry("800x600")
        equipos_canvas = tkinter.Canvas(equipo1,width=800,height=600,bg ="black")
        equipos_canvas.place(x=0,y=0)


        equipo1.mainloop()

    def equipo2():
        equipo2 = Toplevel()
        equipo2.title("Real Madrid")
        equipo2.resizable(width=False,height=False)
        equipo2.geometry("800x600")
        equipos_canvas = tkinter.Canvas(equipo2,width=800,height=600,bg ="black")
        equipos_canvas.place(x=0,y=0)


        equipo2.mainloop()

    def equipo3():
        equipo3 = Toplevel()
        equipo3.title("Real Madrid")
        equipo3.resizable(width=False,height=False)
        equipo3.geometry("800x600")
        equipos_canvas = tkinter.Canvas(equipo3,width=800,height=600,bg ="black")
        equipos_canvas.place(x=0,y=0)


        equipo3.mainloop()

	def equipo4():
        equipo4 = Toplevel()
        equipo4.title("Real Madrid")
        equipo4.resizable(width=False,height=False)
        equipo4.geometry("800x600")
        equipos_canvas = tkinter.Canvas(equipo4,width=800,height=600,bg ="black")
        equipos_canvas.place(x=0,y=0)


        equipo4.mainloop()

	def crear(X):
	    with open('players.txt','r+') as arch:
	        last = None
	        for line in (line for line in arch if line.rstrip('\n')):
	            last = line
	        a = last

	        a = lastline()
	        texto=data.get()
	        arch.seek(0,2)
	        arch.write ('\n')
	        arch.write (str(X))
	        arch.write (str(a+1))
	        arch.write (texto)
	        arch.close()



    b_ini=Button(jugadores, text=" Back ", font=21, command=close_jugadores).place(x=160,y=500)
    b_t1=Button(jugadores, text=" Create Player T1", font=21, command=lambda:crear(1)).place(x=10,y=450)
    b_t2=Button(jugadores, text=" Create Player T2", font=21, command=lambda:crear(2)).place(x=160,y=450)
    b_t3=Button(jugadores, text=" Create Player T3", font=21, command=lambda:crear(3)).place(x=310,y=450)
    t1 = Button(jugadores,command=team1).place(x=10,y=10)
    t1.config( image=equipo1,width="200",height="200" )
    t2 = Button(jugadores,command=team2).place(x=310,y=10)
    t2.config( image=equipo2,width="200",height="200" )
    t3 = Button(jugadores,command=team3).place(x=10,y=310)
    t3.config( image=equipo3,width="200",height="200" )
    t4 = Button(jugadores,command=team4).place(x=310,y=310)
    t4.config( image=equipo4,width="200",height="200" )

    def close_jugadores():
        inicio.deiconify()
        jugadores.destroy()

    jugadores.protocol("WM_DELETE_WINDOW", close_jugadores)

    jugadores.mainloop()
    

def crear_equipos():
    arch = open('players2.txt','r+')
    global equipo1 , equipo2, equipo3, equipo4
    equipo1 = []
    equipo2 = []
    equipo3 = []
    equipo4 = []
    a = arch.realine()
    while a != '':
        if a[2] == 1:
            equipo1.append((a[0:2],a[3:-1]))
            a = arch.realine()
        elif a[2] == 2:
            equipo2.append((a[0:2],a[3:-1]))
            a = arch.realine()
        elif a[2] == 3:
            equipo3.append((a[0:2],a[3:-1]))
            a = arch.realine()                                        
        elif a[2] == 4:
            equipo4.append((a[0:2],a[3:-1]))
            a = arch.realine()
        else:
            a = arch.readline()
    arch.close()
                









        

######Ventana Ayuda
def ayuda():

    inicio.withdraw()
    ayuda = Toplevel()
    ayuda.title("Help")
    ayuda.resizable(width=False,height=False)
    ayuda.geometry("800x600")
    ayuda_canvas = tkinter.Canvas(ayuda,width=800,height=600)
    ayuda_canvas.place(x=0,y=0)


    def close_ayuda():
        inicio.deiconify()
        ayuda.destroy()
    b_ini=Button(ayuda, text=" Back ", font=21, command=close_ayuda).place(x=160,y=500)            
        

    ayuda.protocol("WM_DELETE_WINDOW", close_ayuda)

    ayuda.mainloop()
    
######Ventana inicio
inicio = Tk()
inicio.title('Penales Futbol')
inicio.minsize(800,600)
inicio.resizable(width= False, height=False)

inicio_canvas = tkinter.Canvas(inicio,width=800,height=600,bg='black')
inicio_canvas.place(x=0,y=0)



b_score=Button(inicio, text=" Highscores ", font=21, command=scores).place(x=160,y=500)
b_ayuda=Button(inicio, text=" Help ", font=21, command=ayuda).place(x=160,y=450)
b_about=Button(inicio, text=" About ", font=21, command=about).place(x=160,y=400)
b_about=Button(inicio, text=" Players ", font=21, command=jugadores).place(x=160,y=350)



def close_inicio():

    inicio.destroy()
        
    

inicio.protocol("WM_DELETE_WINDOW", close_inicio)




inicio.mainloop()






