from tkinter import *
from threading import Thread
import os ,  random , time

global p1 , p2, p3, p4 , p5 , p6 , player , arbitro , g1, g2, g3, g4, g5, g6 , score1, score2 , turno
p1 = False
p2 = False
p3 = False
p4 = False
p5 = False
p6 = False
player = False
arbitro = False
g1 = False
g2 = False
g3 = False
g4 = False
g5 = False
g6 = False
player1 = [1,2,3,4,5]
player2 = [6,7,8,9,0]
score1 = 0
score2 = 0
turno = 1



def threads(id):
    if id:
        None
    elif id == 5:
        None
        #    music_thread = Thread(target=visit_sound,args=())
        #    music_thread.daemon = True		#Le indica que corra asincrónicamente
        #    music_thread.start()
    elif id == 6:
        None
    #    music_thread = Thread(target=home_sound,args=())
    #    music_thread.daemon = True		#Le indica que corra asincrónicamente
    #    music_thread.start()
    elif id == 7:
        cont = Thread(target=contador,args=())
        cont.daemon = True		#Le indica que corra asincrónicamente
        cont.start()

def contador():
    for i in range(5,0,-1):
        countdown(i)
        time.sleep(1)
    print ('Se acabo el tiempo')
    cambio()
    

def ghost(): 
    global g1, g2, g3, g4, g5, g6
    g1 = False
    g2 = False
    g3 = False
    g4 = False
    g5 = False
    g6 = False
    port = random.choice([1, 2, 3, 4])
    if port == 1:
        a = random.choice([1,2,3,4,5,6])
        if a == 1:
            g1 = True
        elif a == 2:
            g2 = True
        elif a == 3:
            g3 = True
        elif a == 4:
            g4 = True
        elif a == 5:
            g5 = True
        elif a == 6:
            g6 = True
    elif port == 2:
        a = random.choice([1,2,3]) 
        if a == 1:
            g1 = True
            g2 = True
        elif a == 2:
            g3 = True
            g4 = True
        elif a == 3:
            g5 = True
            g6 = True
    elif port == 3:
        a = random.choice([1,2])
        if a == 1:
            g1 = True
            g2 = True
            g3 = True
        elif a == 2:
            g4 = True
            g5 = True
            g6 = True
    elif port == 4:
        a = random.choice([1,2])
        if a == 1:
            g1 = True
            g3 = True
            g5 = True
        elif a == 2:
            g2 = True
            g4 = True
            g6 = True
        
    print ('g=',g1,g2,g3,g4,g5,g6)

def cambio():

    
    global p1 , p2, p3, p4 , p5 , p6 , player , arbitro , g1, g2, g3, g4, g5, g6 , score1, score2 , turno
    p1 = False
    p2 = False
    p3 = False
    p4 = False
    p5 = False
    p6 = False

    if player:
        None
        #stop music
        #musica1
    else:
        None
        #stop music
        #musica2
    #threads(7)
    turno += 1
    print ('turno',turno)

        
    

def input_lis(id):
    global p1 , p2, p3, p4 , p5 , p6 , player 
    
    if id == 0:
        None
    elif id == 1:
        p1  = False if p1 else True
        #print (p1)
    elif id == 2:
        p2  = False if p2 else True
    elif id == 3:
        p3  = False if p3 else True
    elif id == 4:
        p4  = False if p4 else True
    elif id == 5:
        p5  = False if p5  else True
    elif id == 6:
        p6 = False if p6 else True
    elif id == 7:
        
        cambio()
        player = False if player else True

        
    elif id == 8:
        arbitro = False
    elif id == 9:
        arbitro = True


def puntuacion():
    ghost()
    global p1 , p2, p3,player, p4 , p5 , p6 , arbitro , g1, g2, g3, g4, g5, g6 , score1, score2 , turno
    if p1 and not g1:
        if turno%2 == 2:
            score2 += 1
        elif turno%2 == 1:
            score1 += 1
        #score2 += 1 if player else (score1 += 1)
    elif p2 and not g2:
        if turno%2 == 2:
            score2 += 1
        elif turno%2 == 1:
            score1 += 1
#        score2 += 1 if player else score1 += 1
    elif p3 and not g3:
        if turno%2 == 2:
            score2 += 1
        elif turno%2 == 1:
            score1 += 1
#        score2 += 1 if player else score1 += 1
    elif p4 and not g4:
        if turno%2 == 2:
            score2 += 1
        elif turno%2 == 1:
            score1 += 1
#        score2 += 1 if player else score1 += 1
    elif p5 and not g5:
        if turno%2 == 2:
            score2 += 1
        elif turno%2 == 1:
            score1 += 1
#        score2 += 1 if player else score1 += 1
    elif p6 and not g6:
        if turno%2 == 2:
            score2 += 1
        elif turno%2 == 1:
            score1 += 1


#        score1 += 1 if player else score2 += 1
    print ('p=',p1,p2,p3,p4,p5,p6)
    #print (g1,g2,g3,g4,g5,g6)
    print ('score1',score1)
    print ('score2',score2)
            
        
def clear():
    global p1 , p2, p3, p4 , p5 , p6 , player , arbitro , g1, g2, g3, g4, g5, g6 , score1, score2
    p1 = False
    p2 = False
    p3 = False
    p4 = False
    p5 = False
    p6 = False
    g1 = False
    g2 = False
    g3 = False
    g4 = False
    g5 = False
    g6 = False


def juego():
    global player
    juego = Tk()
    #juego=Toplevel()
    juego.geometry("800x600+250+50")
    player = random.choice([True ,False])
    print ('player',player)
    print ('turno',turno)
    

    
    

    

    
    inputA = Button(juego,text='A',width=1,height=1,command=lambda:input_lis(1)).place(x=0,y=0)
    inputB = Button(juego,text='B',width=1,height=1,command=lambda:input_lis(2)).place(x=20,y=0)
    inputC = Button(juego,text='C',width=1,height=1,command=lambda:input_lis(3)).place(x=40,y=0)
    inputD = Button(juego,text='D',width=1,height=1,command=lambda:input_lis(4)).place(x=60,y=0)
    inputE = Button(juego,text='E',width=1,height=1,command=lambda:input_lis(5)).place(x=80,y=0)
    inputF = Button(juego,text='F',width=1,height=1,command=lambda:input_lis(6)).place(x=100,y=0)
    inputG = Button(juego,text='G',width=1,height=1,command=lambda:input_lis(7)).place(x=120,y=0)
    arb1 = Button(juego,text='Arbitro1',width=10,height=1,command=lambda:input_lis(8)).place(x=200,y=0)
    arb2 = Button(juego,text='Arbitro2',width=10,height=1,command=lambda:input_lis(9)).place(x=300,y=0)
    punt = Button(juego,text='Gol',width=10,height=1,command=puntuacion).place(x=200,y=100)
    #clr = Button(juego,text='Clear',width=10,height=1,command=clear).place(x=200,y=130)




    juego.mainloop()


juego()
