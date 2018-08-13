"""
######################################################
| Instituto Tecnológico de Costa Rica                |
| Computer Engineering                               |
| Taller de Programación                             |
|                                                    | 
| SPACE INVADERS                                     |
|                                                    |
| Alexis Gavriel Gómez                               |
|                                                    |
| Versión: 0.8                                       |
| Fecha de Última Modificación: May 9 2016           |
######################################################
"""


import tkinter
from tkinter import *
from random import uniform as Aleatorio
from threading import Thread
import time
import os
import winsound
import random

def load_img(name):
    path=os.path.join("imgs",name)
    img = PhotoImage(file=path)
    return img

global nivel , pts ,bala1 , bala2, bala3 , cantidad , name
name = '-None-'
cantidad = 36
nivel = 1
pts = 0
bala1 = True
#bala2 = True
#bala3 = True


######Ventana about






def winabout():
 #   main.withdraw()
    music_stop()
    winabout = Toplevel()
    winabout.title("About")
    winabout.resizable(width=False,height=False)
    winabout.geometry("360x640")

    arch_about = open('about.txt','r')
    texto = Text(winabout )

    texto.insert(END, arch_about.read())
    texto.pack()
    Back_ini=Button(winabout, text=" Back ", font=21, command=winabout.destroy).place(x=160,y=500)

    
    def on_closing():
        arch_about.close()
        winabout.destroy()
    

    winabout.protocol("WM_DELETE_WINDOW", on_closing)

    winabout.mainloop()
    
############
def scores_win():
    music_stop()
    scores_win = Toplevel()
    scores_win.title("Scores")
    scores_win.resizable(width=False,height=False)
    scores_win.geometry("360x640")

    arch_scores = open('score.txt','r')
    texto = Text(scores_win )

    texto.insert(END, arch_scores.read())
    texto.pack()
    Back_ini=Button(scores_win, text=" Back ", font=21, command=scores_win.destroy).place(x=160,y=500)

    
    def close():
        arch_scores.close()
        scores_win.destroy()
    

    scores_win.protocol("WM_DELETE_WINDOW", close)

    scores_win.mainloop()


#####Ventana juego
def wingame():
    
    music_stop()
    wingame = Toplevel()
    wingame.title('Space Invaders')
    wingame.resizable(width=False,height=False)
    wingame.geometry("500x640")
    

    bicho1=load_img("bicho1.PNG")
    bicho2=load_img("bicho2.PNG")
    bloque3=load_img('bloque3.PNG')
    bloque2=load_img('bloque2.PNG')
    bloque1=load_img('bloque1.PNG')
    nave=load_img('nave.PNG')
    disparo=load_img('disparo.PNG')




    space = tkinter.Canvas(wingame,bg='black',width=500,height=640)
    space.place(x=0,y=0)
    space.create_line(0,529,500,529 ,fill='Yellow')
    space.create_rectangle(0,-20,500,32 ,fill='grey')
    Back_inicio=Button(wingame, text=" Back ", font=21, command=wingame.destroy).place(x=0,y=0)


#    bloqueA3= space.create_image(105,550,image=bloque3)
 #   bloqueA2= space.create_image(105,550,image=bloque2)
 #   bloqueA1= space.create_image(105,550,image=bloque1)
    
  #  bloqueB3= space.create_image(250,550,image=bloque3)
  #  bloqueB2= space.create_image(250,550,image=bloque2)
  #  bloqueB1= space.create_image(250,550,image=bloque1)
    
  #  bloqueC3= space.create_image(395,550,image=bloque3)
  #  bloqueC2= space.create_image(395,550,image=bloque2)
  #  bloqueC1= space.create_image(395,550,image=bloque1)

    Nave= space.create_image(250,600,image=nave)

    def add0(A):
        if len(A)==5:
            return A
        elif len(A)<5:
            return add0('0'+ A )
        elif len(A)>5:
            return add0(A[1:])

    
    def winner():
        print (space.find_overlapping(0,32,500,528))
        space.delete('all')
        Tit= Label(space, text="Victory!",bg="black",fg = "white", font=180).place(x=250,y=300)
        
        global pts
        print (pts)
        puntos = add0(str(pts))
        
        scores = open('score.txt','r+')
        scores.seek(1)
        P1 = scores.read(6)
        scores.seek(11)
        P1s = scores.read(5)
        scores.seek(18)
        P2 = scores.read(6)
        scores.seek(25)
        P2s = scores.read(5)
        scores.seek(33)
        P3 = scores.read(6)
        scores.seek(40)
        P3s = scores.read(5)

        if pts > int(P3):
            if pts > int (P2):
                if pts > int (P3):
                    scores.seek(8)
                    scores.write(puntos)
                else:
                    scores.seek(22)
                    scores.write(puntos) 

            else:
                scores.seek(30)
                scores.write(puntos)
        else:
            None
            
        def ask():
            messagebox.askyesno("Exit?", "Return?")
            if messagebox.askyesno() == True:
                scores.close()
                wingame.destroy()
            else:
                wingame.destroy()
                main.destroy()
        ask()
     #   texto = Text(winabout )

      #  texto.insert(END, arch_about.read())
      #  texto.pack()


    fin=Button(wingame, text="Finish", font=21, command=winner).place(x=70,y=0)
        
    def MoveRight(event):
        coords_nave = space.coords(Nave)
        if coords_nave[0] < 475:
            space.move(Nave,10,0)
        else:
            print("Error Movimiento hacia derecha")


    def MoveLeft(event):
        coords_nave = space.coords(Nave)
        if coords_nave[0] >25:
            space.move(Nave,-10,0)
        else:
            print("Error Movimiento hacia izquierda")



    space.bind("<Right>",MoveRight)
    space.bind("<Left>",MoveLeft)
    space.bind("<d>",MoveRight)
    space.bind("<a>",MoveLeft)

    space.focus_set()





















#Invasores


    
#######fila 1
    
    global fila1 , invasor11,invasor12,invasor13,invasor14,invasor15,invasor16,invasor17,invasor18,invasor19,invasor1A,invasor1B ,invasor1C
    global inv11 , inv12 , inv13, inv14, inv15, inv16, inv17, inv18, inv19, inv1A, inv1B, inv1C
    
    invasor11= space.create_image(14 +0*26,60,image=bicho1,tags='invasores')
    inv11= 1
    invasor12= space.create_image(14 +1*26,60,image=bicho1,tags='invasores')
    inv12= 1
    invasor13= space.create_image(14 +2*26,60,image=bicho1,tags='invasores')
    inv13= 1
    invasor14= space.create_image(14 +3*26,60,image=bicho1,tags='invasores')
    inv14= 1
    invasor15= space.create_image(14 +4*26,60,image=bicho1,tags='invasores')
    inv15= 1
    invasor16= space.create_image(14 +5*26,60,image=bicho1,tags='invasores')
    inv16= 1
    invasor17= space.create_image(14 +6*26,60,image=bicho1,tags='invasores')
    inv17= 1
    invasor18= space.create_image(14 +7*26,60,image=bicho1,tags='invasores')
    inv18= 1
    invasor19= space.create_image(14 +8*26,60,image=bicho1,tags='invasores')
    inv19= 1
    invasor1A= space.create_image(14 +9*26,60,image=bicho1,tags='invasores')
    inv1A= 1
    invasor1B= space.create_image(14 +10*26,60,image=bicho1,tags='invasores')
    inv1B= 1
    invasor1C= space.create_image(14 +11*26,60,image=bicho1,tags='invasores')
    inv1C= 1

    fila1 = [invasor11,invasor12,invasor13,invasor14,invasor15,invasor16,invasor17,invasor18,invasor19,invasor1A,invasor1B,invasor1C]
   


######fila 2

    global fila2,invasor21,invasor22,invasor23,invasor24,invasor25,invasor26,invasor27,invasor28,invasor29,invasor2A,invasor2B,invasor2C
    global inv21 , inv22 , inv23, inv24, inv25, inv26, inv27, inv28, inv29, inv2A, inv2B, inv2C 
    invasor21= space.create_image(14 +0*26,90,image=bicho1,tags='invasores')
    inv21= 1
    invasor22= space.create_image(14 +1*26,90,image=bicho1,tags='invasores')
    inv22= 1
    invasor23= space.create_image(14 +2*26,90,image=bicho1,tags='invasores')
    inv23= 1
    invasor24= space.create_image(14 +3*26,90,image=bicho1,tags='invasores')
    inv24= 1
    invasor25= space.create_image(14 +4*26,90,image=bicho1,tags='invasores')
    inv25= 1
    invasor26= space.create_image(14 +5*26,90,image=bicho1,tags='invasores')
    inv26= 1
    invasor27= space.create_image(14 +6*26,90,image=bicho1,tags='invasores')
    inv27= 1
    invasor28= space.create_image(14 +7*26,90,image=bicho1,tags='invasores')
    inv28= 1
    invasor29= space.create_image(14 +8*26,90,image=bicho1,tags='invasores')
    inv29= 1
    invasor2A= space.create_image(14 +9*26,90,image=bicho1,tags='invasores')
    inv2A= 1
    invasor2B= space.create_image(14 +10*26,90,image=bicho1,tags='invasores')
    inv2B= 1
    invasor2C= space.create_image(14 +11*26,90,image=bicho1,tags='invasores')
    inv2C= 1

    fila2 = [invasor21,invasor22,invasor23,invasor24,invasor25,invasor26,invasor27,invasor28,invasor29,invasor2A,invasor2B,invasor2C]
   


##fila 3

    global fila3,invasor31,invasor32,invasor33,invasor34,invasor35,invasor36,invasor37,invasor38,invasor39,invasor3A,invasor3B,invasor3C
    global inv31 , inv32 , inv33, inv34, inv35, inv36, inv37, inv38, inv39, inv3A, inv3B, inv3C 
    invasor31= space.create_image(14 +0*26,120,image=bicho1,tags='invasores')
    inv31= 1
    invasor32= space.create_image(14 +1*26,120,image=bicho1,tags='invasores')
    inv32= 1
    invasor33= space.create_image(14 +2*26,120,image=bicho1,tags='invasores')
    inv33= 1
    invasor34= space.create_image(14 +3*26,120,image=bicho1,tags='invasores')
    inv34= 1
    invasor35= space.create_image(14 +4*26,120,image=bicho1,tags='invasores')
    inv35= 1
    invasor36= space.create_image(14 +5*26,120,image=bicho1,tags='invasores')
    inv36= 1
    invasor37= space.create_image(14 +6*26,120,image=bicho1,tags='invasores')
    inv37= 1
    invasor38= space.create_image(14 +7*26,120,image=bicho1,tags='invasores')
    inv38= 1
    invasor39= space.create_image(14 +8*26,120,image=bicho1,tags='invasores')
    inv39= 1
    invasor3A= space.create_image(14 +9*26,120,image=bicho1,tags='invasores')
    inv3A= 1
    invasor3B= space.create_image(14 +10*26,120,image=bicho1,tags='invasores')
    inv3B= 1
    invasor3C= space.create_image(14 +11*26,120,image=bicho1,tags='invasores')
    inv3C= 1

    fila3 = [invasor31,invasor32,invasor33,invasor34,invasor35,invasor36,invasor37,invasor38,invasor39,invasor3A,invasor3B,invasor3C]
  

    global matriz
    matriz = [fila1,fila2,fila3]


    def gameover():
        
        space.delete('all')
        Titulo= Label(space, text="You have lost",bg="black",fg = "white", font=180).place(x=250,y=300)


    

    
    def mov1():
        global nivel , max_der, max_izq, max_abajo, N , M, Etapa , alive
        global fila3x , fila3,fila2x , fila2,fila1x , fila1 , cantidad
        alive = True
        Etapa = 1
        N = 0
        M = 0
        speedini = nivel
        move = 10

        while M < 5:
            if move > 0:
                   # print (max_der)
                while  N < 20:
                    space.move('invasores',move,0)
                    time.sleep(speedini)
                    N +=1
                        
                    
                space.move('invasores',0,30)               
                move = -move
                M +=1
                N = 0
            elif move < 0:
                while N < 20:
                    space.move('invasores',move,0)
                    time.sleep(speedini)
                    N+=1
                space.move('invasores',0,30)
                move = -move
                M+=1
                N = 0
    #############

        while M < 10:
            speedini = speedini *4 /5
            Etapa = 2
            if move > 0:
            
                while  N < 20:
                    space.move('invasores',move,0)
                    time.sleep(speedini)
                    N +=1
                        
                    
                space.move('invasores',0,30)               
                move = -move
                M +=1
                N = 0
            elif move < 0:
                while N < 20:
                    space.move('invasores',move,0)
                    time.sleep(speedini)
                    N+=1
                space.move('invasores',0,30)
                move = -move
                M+=1
                N = 0


    ###############                
        while M < 15:
            speedini = speedini *4 /5
            Etapa = 3
            if move > 0:
                   # print (max_der)
                while  N < 20:
                    space.move('invasores',move,0)
                    time.sleep(speedini)
                    N +=1
                        
                    
                space.move('invasores',0,30)               
                move = -move
                M +=1
                N = 0
            elif move < 0:
                while N < 20:
                    space.move('invasores',move,0)
                    time.sleep(speedini)
                    N+=1
                space.move('invasores',0,30)
                move = -move
                M+=1
                N = 0
        gameover()
        alive = False





        
###############



        
            



###

    def moverbichos1():
        global mythr1 
        mythr1 = Thread(target=mov1,args=())
        mythr1.start()

    moverbichos1()
    



    def moverDisparo1():
        global mythr 
        mythr = Thread(target=shoot1,args=())
        mythr.start()
          
#    def moverDisparo2():
#        global mythr 
#        mythr = Thread(target=shoot2,args=())
#        mythr.start()
#
#    def moverDisparo3():
#        global mythr 
#        mythr = Thread(target=shoot3,args=())
#        mythr.start()





    def overlap(A):
        try:
            
     #       print ( [space.coords(A)[0]-12],[space.coords(A)[1]-10] ,[space.coords(A)[0]+12],[space.coords(A)[1]+10])
            a= [space.coords(A)[0]-12],[space.coords(A)[1]-10] ,[space.coords(A)[0]+12],[space.coords(A)[1]+10]
            b = space.find_overlapping(a[0],a[1],a[2],a[3])
            return b
        except:
            None

    def elimbala():
        global Disparo1 , bala1
        if Disparo1 in space.find_all():
                space.move(Disparo1,-10,-10)
        bala1 = True
       
    

    def coli():
        global invasor11,invasor12,invasor13,invasor14,invasor15,invasor16,invasor17,invasor18,invasor19,invasor1A,invasor1B ,invasor1C
        global inv11 , inv12 , inv13, inv14, inv15, inv16, inv17, inv18, inv19, inv1A, inv1B, inv1C
        global invasor21,invasor22,invasor23,invasor24,invasor25,invasor26,invasor27,invasor28,invasor29,invasor2A,invasor2B,invasor2C
        global inv21 , inv22 , inv23, inv24, inv25, inv26, inv27, inv28, inv29, inv2A, inv2B, inv2C
        global invasor31,invasor32,invasor33,invasor34,invasor35,invasor36,invasor37,invasor38,invasor39,invasor3A,invasor3B,invasor3C
        global inv31 , inv32 , inv33, inv34, inv35, inv36, inv37, inv38, inv39, inv3A, inv3B, inv3C
        global bala1 , Disparo1 , cantidad , pts , Etapa 

       # print (space.find_overelapping(0,32,500,528))
############ Fila1
#        if cantidad <1:
      #           
      #      return winner()
        if overlap(invasor11) != (4,) and invasor11 in space.find_all():
            
                space.delete(invasor11)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
         
        elif overlap(invasor12) != (5,) and invasor12 in space.find_all():
            
                space.delete(invasor12)            
                elimbala()                            
                inv12 =0                
                pts += Etapa
                cantidad -=1
         
        elif overlap(invasor13) != (6,) and invasor13 in space.find_all():
                space.delete(invasor13)            
                elimbala()                            
                inv13 =0                
                pts += Etapa
                cantidad -=1
           
        elif overlap(invasor14) !=(7,)             and invasor14 in space.find_all():
                space.delete(invasor14)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
         
        elif overlap(invasor15) !=(8,)             and invasor15 in space.find_all():
                space.delete(invasor15)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
         
        elif overlap(invasor16) !=(9,)             and invasor16 in space.find_all():
                space.delete(invasor16)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
          
        elif overlap(invasor17) !=(10,)             and invasor17 in space.find_all():
                space.delete(invasor17)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
      
        elif overlap(invasor18) !=(11,)             and invasor18 in space.find_all():
                space.delete(invasor18)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
        
        elif overlap(invasor19) !=(12,)             and invasor19 in space.find_all():
                space.delete(invasor19)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
         
        elif overlap(invasor1A) !=(13,)             and invasor1A in space.find_all():
                space.delete(invasor1A)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
       
        elif overlap(invasor1B) !=(14,)             and invasor1B in space.find_all():
                space.delete(invasor1B)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
       
        elif overlap(invasor1C) !=(15,)             and invasor1C in space.find_all():
                space.delete(invasor1C)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
         
        
############ Fila2
        elif overlap(invasor21) !=(16,)            and invasor21 in space.find_all():
                space.delete(invasor21)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor22) !=(17,)          and invasor22 in space.find_all():
                space.delete(invasor22)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor23) !=(18,)            and invasor23 in space.find_all():
                space.delete(invasor23)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor24) !=(19,)          and invasor24 in space.find_all():
                space.delete(invasor24)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor25) !=(20,)            and invasor25 in space.find_all():
                space.delete(invasor25)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
       
        elif overlap(invasor26) !=(21,)          and invasor26 in space.find_all():
                space.delete(invasor26)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
     
        elif overlap(invasor27) !=(22,)          and invasor27 in space.find_all():
                space.delete(invasor27)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor28) !=(23,)          and invasor28 in space.find_all():
                space.delete(invasor28)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor29) !=(24,)           and invasor29 in space.find_all():
                space.delete(invasor29)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor2A) !=(25,)           and invasor2A in space.find_all():
                space.delete(invasor2A)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
     
        elif overlap(invasor2B) !=(26,)            and invasor2B in space.find_all():
                space.delete(invasor2B)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor2C) !=(27,)          and invasor2C in space.find_all():
                space.delete(invasor2C)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
  
        

############ Fila3
        elif overlap(invasor31) !=(28,)         and invasor31 in space.find_all():
                space.delete(invasor31)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor32) !=(29,)         and invasor32 in space.find_all():
                space.delete(invasor32)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
   
        elif overlap(invasor33) !=(30,)        and invasor33 in space.find_all():
                space.delete(invasor33)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
   
        elif overlap(invasor34) !=(31,)           and invasor34 in space.find_all():
                space.delete(invasor34)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor35) !=(32,)          and invasor35 in space.find_all():
                space.delete(invasor35)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor36) !=(33,)          and invasor36 in space.find_all():
                space.delete(invasor36)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor37) !=(34,)            and invasor37 in space.find_all():
                space.delete(invasor37)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1

        elif overlap(invasor38) !=(35,)         and invasor38 in space.find_all():
                space.delete(invasor38)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
   
        elif overlap(invasor39) !=(36,)           and invasor39 in space.find_all():
                space.delete(invasor39)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
     
        elif overlap(invasor3A) !=(37,)         and invasor3A in space.find_all():
                space.delete(invasor3A)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
  
        elif overlap(invasor3B) !=(38,)           and invasor3B in space.find_all():
                space.delete(invasor3B)            
                elimbala()                            
                inv3B =0                
                pts += Etapa
                cantidad -=1
  
        elif overlap(invasor3C) !=(39,)           and invasor3C in space.find_all():
                space.delete(invasor3C)            
                elimbala()                            
                inv11 =0                
                pts += Etapa
                cantidad -=1
                  
        else:
            None



    def shoot(event):
        global bala1 , bala2 , bala3
        if bala1:
            bala1 = False
            return moverDisparo1()
#        elif bala2:
#            bala2 = False
#            return moverDisparo2()
#        elif bala3:
#            bala3 = False
#            return moverDisparo3()
        else:
            print ('1 bala al mismo tiempo')

    

        
    def shoot1():
        global bala1 , Disparo1 , invasor11
      
        Disparo1= space.create_image(space.coords(Nave)[0],space.coords(Nave)[1]-25,image=disparo)
        try:
            while space.coords(Disparo1)[1] > 10 and bala1 == False: 
                space.move(Disparo1,0,-5)
                
                time.sleep(0.01)
                coli()

            space.delete(Disparo1)
            bala1 = True
        except:
            space.delete(Disparo1)
            bala1 = True
    






    space.bind("<space>",shoot)



    
    wingame.update() 
    wingame.mainloop()




#########

    

    
#########Ventana menu    
main = Tk()
main.title("Space Invaders")
main.minsize(360,640)
main.resizable(width= False, height=False)

bgini=load_img("fondo_inicio.PNG")
tituloini=load_img("titulo.PNG")
bichotitulo=load_img("bichotit.PNG")



Canvas1 = tkinter.Canvas(main,width=360,height=640)
Canvas1.place(x=0,y=0)
Canvas1.create_image(180,320,image=bgini)
Canvas1.create_image(180,100,image=tituloini)
Canvas1.create_image(180,300,image=bichotitulo)
aboutbut=Button(Canvas1, text=" About ", font=21, command=winabout).place(x=290,y=600)
playbut=Button(Canvas1, text=" Play ", font=21, command=wingame).place(x=160,y=460)
scores=Button(Canvas1, text="Scores", font=21, command=scores_win).place(x=10,y=600)

def nombre():
    global name
    texto=data.get()
    if len (texto) == 6:
        name = texto
    else:
        messagebox.showinfo(message="Name must be 6 characters")

data = StringVar()
textField = Entry(Canvas1,textvariable=data).place(x=125,y=435)
savename=Button(Canvas1, text="Set Name",command=nombre).place(x=255,y=435)

def nivel_1():
        global nivel
        nivel = 1
        
def nivel_2():
        global nivel
        nivel = 0.6
       
def nivel_3():
        global nivel
        nivel = 0.3
      
        
lvl1=Button(Canvas1, text="Level 1", font=21, command=nivel_1).place(x=90,y=540)
lvl2=Button(Canvas1, text="Level 2", font=21, command=nivel_2).place(x=160,y=540)
lvl3=Button(Canvas1, text="Level 3", font=21, command=nivel_3).place(x=230,y=540)


def musica():
    winsound.PlaySound("kingsplan.wav",winsound.SND_ASYNC)

def music_stop():
    winsound.PlaySound(None,0)

def play_music():
    music_thread=Thread(target=musica,args=())
    music_thread.daemon = True
    music_thread.start()

play_music()


def closing():
    music_stop()    
    main.destroy()
    

main.protocol("WM_DELETE_WINDOW", closing)    
main.mainloop()  
