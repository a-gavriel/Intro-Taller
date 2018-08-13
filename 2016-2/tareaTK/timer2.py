import time , tkinter , os , winsound
import tkinter
from tkinter import *
from threading import Thread

def threads(id):
    if False:
        None
    elif id ==1:
        T4_cont = Thread(target=contador,args=())
        T4_cont.start()
    elif id == 2:
        T4_dir = Thread(target=direccion,args=())
        T4_dir.start()

    elif id == 3:
        music_thread = Thread(target=play_music,args=())
        music_thread.daemon = True		
        music_thread.start()			



def V4():
    global V4 , c_V4 

    V4 = Tk()
    V4.title("_ _")
    w,h =300,300
    V4.minsize(w,h)
    V4.resizable(width= False, height=False)
    V4.focus_set() 
    c_V4= tkinter.Canvas(V4,width=w,height=h, bg="#252525")
    c_V4.place(x=0,y=0)


    threads(1)

  
    V4.bind('<space>',reiniciar)
    V4.mainloop()


def reiniciar(event):
	global number
	number = 10


def contador():
    global c_V4, number

    number=5
    finish = False
    while not finish:
        if (number > 0 ):          
            L = Label(c_V4,text=str(number),bg="#FF0000",font=10).place(x=20,y=20)
            number -= 1
            time.sleep(1)

        else:
            L = Label(c_V4,text=str(number),bg="#FF0000",font=10).place(x=20,y=20)
            finish = True
            
    print ('done')

    
V4()
