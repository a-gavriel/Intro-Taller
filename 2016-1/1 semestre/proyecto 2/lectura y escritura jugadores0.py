

import time, os, winsound, random , tkinter
from tkinter import *
from threading import Thread

def button_listener(id):
	if False:
		None
	elif id == 25:
		jugadores.destroy()
		equipo1()
	elif id == 26:
		jugadores.destroy()
		equipo2()
	elif id == 27:
		jugadores.destroy()
		equipo3()
	elif id == 28:
		jugadores.destroy()
		equipo4()
	elif id == 29:
		leer_jugadores()



##ventanas de equipos	
def equipo1():
	None
def equipo2():
	None
def equipo3():
	None
def equipo4():
	None
	

#funcion para leer archivo y clasificar jugadores por equipo
def leer_jugadores(): 
	arch = open('players2.txt','r+')
	global equipo1 , equipo2, equipo3, equipo4 , scores
	equipo1 = []
	equipo2 = []
	equipo3 = []
	equipo4 = []
	scores  = []
	a = arch.readline()
	while a != '':
        if a[2] == '1':
            equipo1.append([a[0:2],a[3:-1]])
            a = arch.readline()
        elif a[2] == '2':
            equipo2.append([a[0:2],a[3:-1]])
            a = arch.readline()
        elif a[2] == '3':
            equipo3.append([a[0:2],a[3:-1]])
            a = arch.readline()                                        
        elif a[2] == '4':
            equipo4.append([a[0:2],a[3:-1]])
            a = arch.readline()
        else:
            a = arch.readline()
    arch.close()
	
	arch = open('scores.txt','r+')
	a = arch.readline()
    while a != '':
		scores.append([int(a[2:5]),int(a[5:8])])
        a = arch.readline()
	arch.close()	
		
		
    print (equipo1)
		
##funcion para cambiar la informacion del equipo a un string simple
##de forma numero+jugador\n
##no esta siendo utilizada
def cambio_str(N):
    R = ''
    for a in range(len(N)):
        b = str(N[a])
        c = b[2:4] + b[8:-2] + '\n'
        R = R + c
    return R


	
#funcion para crear jugadores
def crear(X): 
    with open('players2.txt','r+') as arch: #abre el archivo de jugadores y guarda la ultima linea
        last = None
        for line in (line for line in arch if line.rstrip('\n')): 
            last = line
        ultimalinea = last
        ultimonum = int(ultimalinea[0:2]) #guarda el numero del ultimo jugador
        texto=data.get()
        arch.seek(0,2)
        arch.write ('\n')
        arch.write (str(ultimonum+1))
        arch.write (str(X))
        arch.write (texto)
        
        hs = open('scores.txt','r+')
        hs.seek(0,2)
        hs.write ('\n')
        hs.write (str(ultimonum+1)+'000000')
        hs.close()
        arch.close()   
		


#jugadores = Toplevel()
jugadores = Tk()
jugadores.title("Players")
jugadores.minsize(800,600)
jugadores.resizable(width= False, height=False)
jugadores_canvas = tkinter.Canvas(jugadores,width=800,height=600,bg ="black")
jugadores_canvas.place(x=0,y=0)


t1=Button(jugadores, text=" T1 ", font=21, command=lambda:button_listener(25)).place(x=160,y=500)
t2=Button(jugadores, text=" T2 ", font=21, command=lambda:button_listener(26)).place(x=160,y=450)
t3=Button(jugadores, text=" T3 ", font=21, command=lambda:button_listener(27)).place(x=160,y=400)
t4=Button(jugadores, text=" T4 ", font=21, command=lambda:button_listener(28)).place(x=160,y=350)
actualizar=Button(jugadores, text=" Leer archivo ", font=21, command=lambda:button_listener(29)).place(x=160,y=550)


data = StringVar()
textField = Entry(jugadores_canvas,textvariable=data).place(x=200,y=250)
b_t1=Button(jugadores, text=" Create Player T1", font=21, command=lambda:crear(1)).place(x=10,y=200)
b_t2=Button(jugadores, text=" Create Player T2", font=21, command=lambda:crear(2)).place(x=160,y=200)
b_t3=Button(jugadores, text=" Create Player T3", font=21, command=lambda:crear(3)).place(x=310,y=200)
b_t3=Button(jugadores, text=" Create Player T4", font=21, command=lambda:crear(4)).place(x=460,y=200)


jugadores.mainloop()



