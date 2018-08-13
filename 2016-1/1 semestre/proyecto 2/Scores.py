from tkinter import *


def lectura_tabla():
    jugadores = open('players.txt','r')
    scores = open('scores.txt','r')
    R = 'Numero\tTiros\tGoles\tNombre\n'
    a = jugadores.readline()
    b = scores.readline()
    while b != '':
        x = b[0:2] + '\t' + b[2:5] + '\t' + b[5:8]+ '\t'+ a[3:] 
        R = R+x
        b = scores.readline()
        a = jugadores.readline()

    return R


scores = Tk()
scores.geometry("400x500+250+50")
scores.title('scores')
S = Scrollbar(scores)
T = Text(scores, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = lectura_tabla()
T.insert(END, quote)
mainloop(  )


    
            


    
