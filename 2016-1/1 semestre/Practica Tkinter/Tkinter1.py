import tkinter
from tkinter import *
from random import uniform as Aleatorio
from threading import Thread
import time
import os
import winsound


def load_img(name):
    path=os.path.join("imgs",name)
    img = PhotoImage(file=path)
    return img

main = Tk()
main.title("Taller de Tkinter")
main.minsize(750,450)
main.resizable(width= False, height=False)


bg=load_img("Android.PNG")
ball_img=load_img("esfera.GIF")


Canvas1 = tkinter.Canvas(main,width=800,height=500)
Canvas1.place(x=0,y=0)
Canvas1.create_image(300,350,image=bg)
ball=Canvas1.create_image(200,200,image=ball_img)

Titulo= Label(Canvas1, text="Welcome to Tkinter",bg="#20B2A9",fg = "#000000", font=180).place(x=325,y=25)

def getTextField():
    texto=data.get()
    if texto.lower()== "yes":
        Label(Canvas1,text="You have confirmed!",bg="#cdc7c9",font=10).place(x=320,y=50)
    elif texto.lower()=="no":
        Label(Canvas1,text="You have denied!",bg="#cdc7c9",font=10).place(x=320,y=50)
    else:
        Label(Canvas1,text="You shall not pass!",bg="#cdc7c9",font=10).place(x=320,y=50)

data = StringVar()
textField = Entry(Canvas1,textvariable=data).place(x=550,y=400)
bget=Button(Canvas1, text="Press me!",command=getTextField).place(x=675,y=400)


def move():
    number=0
    while True:
        Canvas1.move(ball,Aleatorio(-10,10),Aleatorio(-10,10))
        time.sleep(1)
        
def Rep():
    global mythr
    mythr = Thread(target=move,args=())
    mythr.start()

Rep()

Mover=Button(Canvas1, text="Mover",command=Rep).place(x=675,y=250)



def MoveRight(event):
    try:
        Canvas1.move(ball,10,0)
    except:
        print("Error Movimiento hacia derecha")

def MoveLeft(event):  
    try:
        Canvas1.move(ball,-10,0)
    except:
        print("Error Movimiento hacia izquierda")

def MoveDown(event): 
    try:
        Canvas1.move(ball,0,10)
    except:
        print("Error Movimiento hacia abajo")

def MoveUp(event):  
    try:
        Canvas1.move(ball,0,-10)
    except:
        print("Error Movimiento hacia arriba")


Canvas1.bind("<Right>",MoveRight)
Canvas1.bind("<Left>",MoveLeft)
Canvas1.bind("<Up>",MoveUp)
Canvas1.bind("<Down>",MoveDown)
Canvas1.focus_set()

def run():
    number=0
    while(number < 100):
        Label(Canvas1,text=str(number),bg="#cdc7c9",font=10).place(x=20,y=20)
        number+=1
        time.sleep(0.5)

def myThread():
    global mythr
    mythr = Thread(target=run,args=())
    mythr.start()


myThread()

def musica():
    winsound.PlaySound("golf.wav",winsound.SND_ASYNC)

def music_stop():
    winsound.PlaySound(None,0)

def play_music():
    music_thread=Thread(target=musica,args=())
    music_thread.daemon = True
    music_thread.start()

play_music()
    
suena=Button(Canvas1, text="Golf",command=play_music).place(x=675,y=150)   
main.mainloop()  
