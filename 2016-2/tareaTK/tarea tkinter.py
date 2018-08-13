

import time , tkinter , os , winsound
import tkinter
from tkinter import *
from threading import Thread


global lang 
lang="en"


configuration = {
	"Lang" : {
		"en" : {
			"V1" :{
				"P1" : "1. Validation",
				"P2" : "2. Fibonacci",
				"P3" : "3. About",
				"P4" : "4. Screen Saver",
				"P5" : "Change to Spanish",
                                "P0" : "Back"
			},
			"P1":{
				"m1" : "Validation of a number",
				"m2" : "\nEnter a digit and an integer number: digit,number",
				"m3" : "Digit , Integer",
				"m4" : "Verify",
                                "m10": "Clear"
                                
			},
                        "P2":{
				"m1" : "Enter an integer number\n max value = 1800",
				"m2" : "Number of recursive calls used =\n",
				"m3" : "\nNumber ",
				"m4" : " of Fibonacci =\n"
			},

                        "P3":{
                                "m1" : """Alexis Gavriel Gómez
2016085662
Male
18 Years Old
Address: 150m S, 100m W
from Guachipelín's Tunnel
"""
                                
                        },
		},
                "es" : {
			"V1" :{
				"P1" : "1. Validación",
				"P2" : "2. Fibonacci",
				"P3" : "3. Acerca de",
				"P4" : "4. Salva Pantallas",
				"P5" : "Cambiar a Inglés",
                                "P0" : "Atrás"
			},
			"P1":{
				"m1" : "Validación de un número",
				"m2" : "\nIngrese un digito y un numero entero: digito,numero",
				"m3" : "Digito , Entero",
				"m4" : "Verificar",
                                "m10": "Limpiar"
			},
                        "P2":{
				"m1" : "Ingrese un número entero\n valor maximo = 1800",
				"m2" : "Numero de llamadas recursivas usadas =\n",
				"m3" : "\nNumero ",
				"m4" : " de Fibonacci =\n"
			},

                        "P3":{
                                "m1" : """Alexis Gavriel Gómez
2016085662
Hombre
18 Años
Dirección: 150m S, 100m O
del Tunel de Guachipelín
"""
                        },              
                },
	}
}

def load_img(name):
    path=os.path.join("imgs",name)
    img = PhotoImage(file=path)
    return img





def idioma():
    global lang , inicio, idioma
    idioma = Tk()
    idioma.title(" Idioma/Language ")
    idioma.minsize(100,100)
    idioma.resizable(width= False, height=False)
    b_lang1 = Button(idioma,text="EN",width=12,height=3,command=lambda:boot(1),bg="white",font=("Arial",8))		
    b_lang1.place(x=100,y=10)
    b_lang2 = Button(idioma,text="ES",width=12,height=3,command=lambda:boot(2),bg="white",font=("Arial",8))		
    b_lang2.place(x=10,y=10)
    idioma.mainloop()


def boot(id):
    global idioma, inicio, lang
    if id == 1:
        idioma.destroy()
        lang = "en"
        inicio()
    elif id == 2:
        idioma.destroy()
        lang = "es"
        inicio()
    




def buttons(id):
    global inicio, V1, V2, V3 , V4
    if False:
        None
    elif id == 1:
        inicio.withdraw()
        V1()
    elif id == 2:
        inicio.withdraw()
        V2()
    elif id == 3:
        inicio.withdraw()
        V3()
    elif id == 4:
        inicio.withdraw()
        V4()
        
    elif id == 11:
        try:
            V1.destroy()
            inicio.deiconify()
        except:
            pass        
    elif id == 21:
        try:
            V2.destroy()
            inicio.deiconify()
        except:
            pass
    elif id == 31:
        try:
            stop_music()
            V3.destroy()
            inicio.deiconify()
        except:
            pass     
    elif id == 41:
        try:
            V4.destroy()
            inicio.deiconify()
        except:
            pass        
    


    
        #inicio.deiconify()

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
        music_thread.daemon = True		#Le indica que corra asincrónicamente
        music_thread.start()			#Lanza el thread





def inicio():
    global inicio, lang
    inicio = Tk()
    inicio.title(" Tkinter ")
    inicio.minsize(750,450)
    inicio.resizable(width= False, height=False)
    c_inicio= tkinter.Canvas(inicio,width=800,height=500)
    c_inicio.place(x=0,y=0)
    py=load_img("py.PNG")
    bgimg = c_inicio.create_image(500,450/2,image=py)


    #b_lang = Button(inicio,text=configuration["Lang"][lang]["V1"]["P5"],width=12,height=3,command=idioma,bg="white",font=("Arial",8))		
    #b_lang.place(x=10,y=10)
    b_v1 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P1"],width=15,height=3,command=V1,bg="white",font=("Arial",8))		
    b_v1.place(x=100,y=150)
    b_v2 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P2"],width=15,height=3,command=V2,bg="white",font=("Arial",8))		
    b_v2.place(x=300,y=150)
    b_v3 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P3"],width=15,height=3,command=V3,bg="white",font=("Arial",8))		
    b_v3.place(x=100,y=300)
    b_v4 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P4"],width=15,height=3,command=V4,bg="white",font=("Arial",8))		
    b_v4.place(x=300,y=300)

    


    inicio.mainloop()






######################################
def V1():
    global V1, data1 , T1
    V1 = Toplevel()
    V1.title( configuration["Lang"][lang]["V1"]["P1"])
    V1.minsize(750,450)
    V1.resizable(width= False, height=False)
    c_V1= tkinter.Canvas(V1,width=750,height=450)
    c_V1.place(x=0,y=0)


    S = Scrollbar(V1)
    T1 = Text(V1, height=4, width=29)
    S.pack(side=RIGHT, fill=Y)
    T1.pack(side=LEFT, fill=Y)
    S.config(command=T1.yview)
    T1.config(yscrollcommand=S.set)
    quote = configuration["Lang"][lang]["P1"]["m2"]
    T1.insert(END, quote)
    
    b_clr=Button(c_V1, text=configuration["Lang"][lang]["P1"]["m10"],command=clear1).place(x=250,y=20)
    data1 = StringVar()
    textField = Entry(c_V1,textvariable=data1).place(x=250,y=60)
    b_add=Button(c_V1, text=configuration["Lang"][lang]["P1"]["m4"],command=add1).place(x=320,y=20)

    menubar = Menu(V1)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(11))
    # display the menu
    V1.config(menu=menubar)
    

    #back1 = Button(V1,text=configuration["Lang"][lang]["V1"]["P0"],width=6,height=2,command=lambda:buttons(11),bg="white",font=("Arial",15))
    #back1.place(x=658,y=0)
    
def add1():
    global data1
    numero = data1.get()
    try:
        num1 = int(numero[0])
        num2 = int(numero[2:])
        #print (num1)
        #print (num2)
        r= menorque (num1,num2)
        r = '\n'+str(r) 
        T1.insert(END, r)
    except:
        E = configuration["Lang"][lang]["P1"]["m2"]
        T1.insert(END, E)


    
def clear1():
    global textField , data1
    data1.set('')
    T1.delete(1.0, END)

def menorque(dig,num):
    if isinstance (dig, int):
        if isinstance (num,int):
            dig = abs (dig)
            num = abs(num)
            if 0<=dig<=9 :
                if num == 0 and dig != 0:
                    return( False)
                elif 0<=num<=9 :
                    return (dig<=num)

                else:
                    return menorque_dig(dig,num)
            else:
                return configuration["Lang"][lang]["P1"]["m2"]
        else:
            return configuration["Lang"][lang]["P1"]["m2"]
    else:
        return configuration["Lang"][lang]["P1"]["m2"]


def menorque_dig(dig,num):
    if num == 0:
        return True
    elif dig <= num%10:
        return menorque_dig(dig,num//10)
    elif dig > num%10:
        return False

        
######################################
def V2():
    global inicio, quote, T2, data2 , V2
    V2 = Toplevel()
    V2.title(configuration["Lang"][lang]["V1"]["P2"])
    V2.minsize(750,450)
    V2.resizable(width= False, height=False)
    c_V2= tkinter.Canvas(V2,width=750,height=450)
    c_V2.place(x=0,y=0)
    fb=load_img("fb.PNG")
    bgimg = c_V2.create_image(750/2,450/2,image=fb)



    S = Scrollbar(V2)
    T2 = Text(V2, height=4, width=29)
    S.pack(side=RIGHT, fill=Y)
    T2.pack(side=LEFT, fill=Y)
    S.config(command=T2.yview)
    T2.config(yscrollcommand=S.set)
    quote = configuration["Lang"][lang]["P2"]["m1"]
    T2.insert(END, quote)


    
    b_clr=Button(c_V2, text=configuration["Lang"][lang]["P1"]["m10"],command=clear2).place(x=250,y=60)
    

    data2 = StringVar()
    textField = Entry(c_V2,textvariable=data2, bg="black", fg="white").place(x=250,y=100)
    
    b_add=Button(c_V2, text=configuration["Lang"][lang]["P1"]["m4"],command=add2).place(x=320,y=60)

    menubar = Menu(V2)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(21))
    # display the menu
    V2.config(menu=menubar)
    
    #back2 = Button(V2,text=configuration["Lang"][lang]["V1"]["P0"],width=6,height=2,command=lambda:buttons(21),bg="white",font=("Arial",15))
    #back2.place(x=658,y=0)
    

    V2.mainloop()





def add2():
    global data2, T2
    numero1 = data2.get()
    
    numero = int(numero1)
    r = fib (numero)
    r1 = str(r[1])
    r = str(r[2])
    result = configuration["Lang"][lang]["P2"]["m2"]+r+ configuration["Lang"][lang]["P2"]["m3"]+ numero1 +configuration["Lang"][lang]["P2"]["m4"] + r1
    
    T2.insert(END, result)


    
def clear2():
    global textField , data2, T2
    data2.set('')
    T2.delete(1.0, END)


    
    

def fib(n):
    if isinstance (n,int) and  n>0:
        global numeroit
        numeroit = 0
        if n>1800:
            return False
        elif n==1 or n==2:
            return 1
        elif n >990:
            [x,y] = fib_aux(1,1,2,900)

            return fib_aux(x,y,900,n) + [numeroit]
        else:
            return fib_aux(1,1,2,n) + [numeroit]

    



        

def fib_aux(a,b,c,n):
    global numeroit
    numeroit +=1
    if c == n:
        return [a,b]
    else:
        c+=1
        h=b
        b=a+b
        a=h
        return fib_aux(a,b,c,n)

 
######################################

def V3():
    global inicio, quote, T3, V3
    V3 = Toplevel()
    V3.title(configuration["Lang"][lang]["V1"]["P3"])
    V3.minsize(750,450)
    V3.resizable(width= False, height=False)
    c_V3= tkinter.Canvas(V3,width=750,height=450, bg='black')
 
    c_V3.place(x=0,y=0)
    does=load_img("does.PNG")
    img = c_V3.create_image(750-154/2,450-154/2,image=does)
    #c_V3.create_line(0, 0, 200, 100)
    #c_V3.create_line(0, 100, 200, 0, fill="red")
    li = c_V3.create_line(100,295 , 750, 295, fill="red")

    T3 = Text(V3, height=4, width=29)
    T3.pack(side=LEFT, fill=Y)

    quote = configuration["Lang"][lang]["P3"]["m1"]
    T3.insert(END, quote)

    b_play=Button(c_V3, text="Play",command=lambda:threads(3)).place(x=420,y=305)
    b_stop=Button(c_V3, text="Stop",command=stop_music).place(x=470,y=305)
    Banda= Label(c_V3, text="DOES",bg="#000000",fg = "#FFFFFF", font=("Helvetica", 20)).place(x=312,y=300)
    nombre= Label(c_V3, text="Know Know Know",bg="#000000",fg = "#FFFF00", font=("Helvetica", 20)).place(x=312,y=350)
    mapa=load_img("map.PNG")
    foto = c_V3.create_image(450,144,image=mapa)
    
    menubar = Menu(V3)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(31))
    # display the menu
    V3.config(menu=menubar)
    #back3 = Button(V3,text=configuration["Lang"][lang]["V1"]["P0"],width=6,height=2,command=lambda:buttons(31),bg="white",font=("Arial",15))
    #back3.place(x=650,y=0)
    
    V3.protocol("WM_DELETE_WINDOW",lambda:buttons(31))
    
    V3.mainloop()


    
def play_music():
    winsound.PlaySound("tk2.wav",winsound.SND_ASYNC)

def stop_music():
    winsound.PlaySound(None,0)
		



######################################
def V4():
    global V4 , img_f , c_V4 , w, h, star
    screen = True
    V4 = Toplevel()
    V4.title(configuration["Lang"][lang]["V1"]["P4"])
    w, h = V4.winfo_screenwidth(), V4.winfo_screenheight()

    V4.geometry("%dx%d+0+0" % (w, h))
    V4.resizable(width= False, height=False)
    V4.focus_set() 
    c_V4= tkinter.Canvas(V4,width=w,height=h, bg="#252525")
    c_V4.place(x=0,y=0)


    points = [10,h/2+40,40,h/2+40,50,h/2+10,60,h/2+40,90,h/2+40,65,h/2+60,75,h/2+90,50,h/2+70,25,h/2+90,35,h/2+60]
    star = c_V4.create_polygon(points, fill = 'yellow')

    #c_V4.move(img_f,50,250)

    threads(1)
    #threads(2)

    #V4.bind('<space>',lambda: threads(2))
    V4.bind('<space>',reiniciar)

    
    #V4.bind('<Motion>', val)

    menubar = Menu(V4)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(41))
    # display the menu
    V4.config(menu=menubar)
    
    #back4 = Button(V4,text=configuration["Lang"][lang]["V1"]["P0"],width=6,height=2,command=lambda:buttons(41),bg="white",font=("Arial",15))
    #back4.place(x=50,y=2)
        
    V4.mainloop()

def reiniciar(event):
	global number
	number = 10


def contador():
    global c_V4, number, w, h , star, star_x, star_y, vel_x, vel_y
    
    coords = c_V4.coords(star)
    #print (coords)
    #print (coords[0])
    
    number=5
    coords = c_V4.coords(star)
    star_x = coords[0]
    star_y = coords[1]
    vel_x = 5
    vel_y = 4

    while True:
        coords = c_V4.coords(star)
        star_x = coords[0]
        star_y = coords[1]

        if False:
        	None
        elif star_x<0:
            vel_x = abs(vel_x)
            c_V4.move(star,vel_x, 0)


        elif star_y<0:

            vel_y = abs(vel_y)
            c_V4.move(star,0, vel_y)


        elif star_x>=w:
            vel_x = -1*abs(vel_x)
            c_V4.move(star,vel_x, 0)



        elif star_y>h:
            vel_y = -1*abs(vel_y)
            c_V4.move(star,0, vel_y)

        elif (number > 0 ):

            
            
            L = Label(c_V4,text=str(number),bg="#FF0000",font=10).place(x=20,y=20)
            number -= 1
            time.sleep(1)



        else:


            c_V4.move(star,vel_x, vel_y)
            
            
            time.sleep(0.01)
    

######################################





idioma()
