from tkinter import *
import os , random

ventana=Tk()
ventana.geometry("300x300+250+50")
#------------------------------------------------------------------#


def button_listener(id):
    if id == 0:
        None
    elif id == 30
        



def input_lis(id):
    global p1 , p2, p3, p4 , p5 , p6 , player 
    
    if id == 0:
        None
    elif id == 1:
        p1 = True
    elif id == 1:
        p2 = True
    elif id == 1:
        p3 = True
    elif id == 1:
        p4 = True
    elif id == 1:
        p5 = True
    elif id == 1:
        p6 = True
    elif id == 1:
        if player:
            player = False
        else:
            player = True
    




ventana.bind("<a>", lambda:input_lis(1))
ventana.bind("<b>", lambda:input_lis(2))
ventana.bind("<c>", lambda:input_lis(3))
ventana.bind("<d>", lambda:input_lis(4))
ventana.bind("<e>", lambda:input_lis(5))
ventana.bind("<f>", lambda:input_lis(6))
ventana.bind("<g>", lambda:input_lis(7))


fondo=Canvas(ventana,width=300,height=300,bg="#000000")
b_playerA = Button(ventana,text='Random Player start',width=10,height=2,command=lambda:button_listener(30)).place(x=460,y=200)
b_playerH = Button(ventana,text='Host Player start',width=10,height=2,command=lambda:button_listener(31)).place(x=410,y=200)
b_playerV = Button(ventana,text='Visit Player start',width=10,height=2,command=lambda:button_listener(32)).place(x=360,y=200)


fondo.place(x=0,y=0)


ventana.mainloop()
