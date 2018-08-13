

import time , tkinter , os , random
import tkinter
from tkinter import *
from threading import Thread


global lang ,  agenda, contactos
lang="en"
agenda = []
contactos = []



#diccionario con mensajes
configuration = {
	"Lang" : {
		"en" : {
			"V1" :{
				"P1" : "Calculator",
				"P2" : "Agenda",
				"P3" : "Contacts",
				"P4" : "Game",
				"P5" : "Language",
                                "P6" : "About",
                                "P0" : "Back"
			},
			"P1":{
				"m1" : "",
				"m2" : "",
				"m3" : "Invalid Data",
				"m4" : "Y/M/D",
                                "m10": "Name"
			},
                        "P2":{
				"m1" : "Sort ID",
				"m2" : "Sort Name",
				"m3" : "Add",
				"m4" : "Remove",
                                "m5" : "Search",
                                "m6" : "Sort Date"
			},
                        "P3":{
				"m1" : "Telephone",
				"m2" : "Cellphone",
				"m3" : "Email",
				"m4" : "Choose Image"
			},
                        "P4":{
				"m1" : "Victory!",
				"m2" : "Defeat",
				"m3" : "Try",
				"m4" : "Restart",
                                "m5" : "Repeated Letter!"
			},

                        "P0":{
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
				"P1" : "Calculadora",
				"P2" : "Agenda",
				"P3" : "Contactos",
				"P4" : "Juego",
				"P5" : "Idioma",
                                "P6" : "Acerca de",
                                "P0" : "Atras"
			},
			"P1":{
				"m1" : "",
				"m2" : "",
				"m3" : "Dato Invalido",
				"m4" : "A/M/D",
                                "m10": "Nombre"
			},
                        "P2":{
				"m1" : "Ordenar ID",
				"m2" : "Ordenar Nombre",
				"m3" : "Agregar",
				"m4" : "Remover",
                                "m5" : "Buscar",
                                "m6" : "Ordenar Fecha"
			},
                        "P3":{
				"m1" : "Telefono",
				"m2" : "Celular",
				"m3" : "Correo",
				"m4" : "Seleccionar Imagen"
			},
                        "P4":{
				"m1" : "Victoria!",
				"m2" : "Derrota!",
				"m3" : "Intentar",
				"m4" : "Reiniciar",
                                "m5" : "Letra Repetida!"
			},

                        "P0":{
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

#funcion para crear una imagen
def load_img(name):
    path=os.path.join("imgs",name)
    img = PhotoImage(file=path)
    return img

#ventana incial para seleccion de idioma y encender o apagar
def ventana_idioma():
    global lang , inicio, idioma, active
    
    active = True
    idioma = Tk()
    idioma.title(" Idioma/Language ")
    idioma.minsize(400,600)
    idioma.resizable(width= False, height=False)
    
    b_lang1 = Button(idioma,text="EN",width=12,height=3,command=lambda:cambiar_lang(1),bg="white",font=("Arial",8))		
    b_lang1.place(x=100,y=10)
    b_lang2 = Button(idioma,text="ES",width=12,height=3,command=lambda:cambiar_lang(2),bg="white",font=("Arial",8))		
    b_lang2.place(x=10,y=10)
    b_lang3 = Button(idioma,text="ON",width=12,height=3,command=boot,bg="white",font=("Arial",8))		
    b_lang3.place(x=10,y=80)
    b_lang4 = Button(idioma,text="OFF",width=12,height=3,command=off,bg="white",font=("Arial",8))		
    b_lang4.place(x=100,y=80)
    
    
    idioma.mainloop()

#cambia el idioma
def cambiar_lang(id):
    global idioma, inicio, lang , boot
    if id == 1:
        lang = "en"
    elif id == 2:
        lang = "es"
    boot()
        
#leer archivos y despliega inicio
def boot():
    global idioma, agenda, contactos
    leer_agenda()
    leer_contactos()
    idioma.withdraw()
    ventana_inicio()

#guarda datos en archivos
def off():
    global agenda, contactos
    text_agenda = ''
    for fila in agenda:
        for columna in fila:
            y += str(columna) + '\n'
            
    text_contactos = ''
    for fila in contactos:
        for columna in fila:
            y += str(columna) + '\n'

    arch_a = open ("agenda.txt","r+")
    deleteContent(arch_a)
    arch_a.write(text_agenda)
    arch_a.close()
    
    arch_c = open ("contactos.txt","r+")
    deleteContent(arch_c)
    arch_c.write(text_contactos)
    arch_c.close()

    

#borra contenidos de archivo
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

#controla los botones que transitan entre ventanas
def buttons(id):
    global inicio, V1, V2, V3 , V4, idioma, juego, calc
    if False:
        None
    elif id == 0.1:
        idioma.deiconify()
        inicio.destroy()
        
    elif id == 1:
        inicio.withdraw()
        calculadora()
    elif id == 2:
        inicio.withdraw()
        Ventana_agenda()
    elif id == 3:
        inicio.withdraw()
        Ventana_contactos()
    elif id == 4:
        inicio.withdraw()
        ventana_juego()
    elif id == 6:
        inicio.withdraw()
        ventana_about()
        
    elif id == 11:
        try:
            calc.destroy()
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
            V1.destroy()
            inicio.deiconify()
            
        except:
            pass     
    elif id == 41:
        try:
            juego.destroy()
            inicio.deiconify()
            
        except:
            pass        
    elif id == 51:
        try:
            V3.destroy()
            inicio.deiconify()
        except:
            pass


    
        #inicio.deiconify()

#controla treads
def threads(id):
    if False:
        None
    elif id ==1:
        T1_clock = Thread(target=tick,args=())
        T1_clock.start()




def ventana_inicio():
    global inicio, lang, boot, buttons , time1 , clock, c_inicio , ventana
    
    
    inicio = Toplevel()

    inicio.title(" Tablet ")
    inicio.minsize(400,600)
    inicio.resizable(width= False, height=False)
    inicio.focus_force()
    c_inicio= tkinter.Canvas(inicio,width=400,height=600)
    c_inicio.place(x=0,y=0)
    py=load_img("fondo1.PNG")
    bgimg = c_inicio.create_image(200,300,image=py)


    #b_lang = Button(inicio,text=configuration["Lang"][lang]["V1"]["P5"],width=12,height=3,command=idioma,bg="white",font=("Arial",8))		
    #b_lang.place(x=10,y=10)
    b_v1 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P1"],width=15,height=3,command=lambda:buttons(1),bg="white",font=("Arial",8))		
    b_v1.place(x=50,y=150)
    b_v2 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P2"],width=15,height=3,command=lambda:buttons(2),bg="white",font=("Arial",8))		
    b_v2.place(x=250,y=150)
    b_v3 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P3"],width=15,height=3,command=lambda:buttons(3),bg="white",font=("Arial",8))		
    b_v3.place(x=50,y=300)
    b_v4 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P4"],width=15,height=3,command=lambda:buttons(4),bg="white",font=("Arial",8))		
    b_v4.place(x=250,y=300)
    b_v0 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P5"],width=15,height=3,command=lambda:buttons(0.1),bg="white",font=("Arial",8))		
    b_v0.place(x=250,y=500)
    b_v6 = Button(inicio,text=configuration["Lang"][lang]["V1"]["P6"],width=15,height=3,command=lambda:buttons(6),bg="white",font=("Arial",8))		
    b_v6.place(x=50,y=500)
    


    
    
    
    #reloj = Label(c_inicio, text='' ,font=('times', 20, 'bold'), bg='green').place(x=20,y=50)
    #print (type(a))

        
    threads(1)




    inicio.mainloop()



#reloj
def tick():
    global  clock, inicio, c_inicio , ventana
    while True:
        try:
            time_now = time.strftime('%H:%M:%S')
            clock = Label(inicio, text=time_now ,font=('times', 20, 'bold'), bg='green').place(x=291,y=2)
            time.sleep(0.2)
        except:
            None


######################################
def ventana_about():
    global inicio, quote, T3, V3
    V3 = Toplevel()
    V3.title(configuration["Lang"][lang]["V1"]["P6"])
    V3.minsize(400,600)
    V3.resizable(width= False, height=False)
    c_V3= tkinter.Canvas(V3,width=400,height=600, bg='black')
    c_V3.place(x=0,y=0)
    
    


    #c_V3.create_line(0, 0, 200, 100)
    #c_V3.create_line(0, 100, 200, 0, fill="red")


    T3 = Text(V3, height=4, width=29)
    T3.pack(side=LEFT, fill=Y)

    quote = configuration["Lang"][lang]["P0"]["m1"]
    T3.insert(END, quote)

    mapa=load_img("alexis.PNG")
    foto = c_V3.create_image(300,100,image=mapa)
    
    menubar = Menu(V3)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(51))
    V3.config(menu=menubar)

    
    V3.protocol("WM_DELETE_WINDOW",lambda:buttons(51))
    
    V3.mainloop()


######################################
#calc


global numero1 , numero2 , operando, punto, negativo
numero1 = ''
numero2 = ''
operando = 1
opr = 0
punto = 0
negativo = 0

def calculadora():
    global numero1, numero2 , T1, T2, calc, ventana
    
    calc = Toplevel()
    calc.title( 'titulo')
    calc.minsize(400,600)
    calc.resizable(width= False, height=False)
    calc.focus_force()
    calc_canvas= tkinter.Canvas(calc,width=400,height=600)
    calc_canvas.place(x=0,y=0)

    T1 = Text(calc, height=1, width=20)
    T1.place(x=100,y=100)


    
    #botones de la calculadora
    boton0=Button(calc_canvas, text='0',command=lambda:addN(0)).place(x=150,y=350)
    boton1=Button(calc_canvas, text='1',command=lambda:addN(1)).place(x=100,y=300)
    boton2=Button(calc_canvas, text='2',command=lambda:addN(2)).place(x=150,y=300)
    boton3=Button(calc_canvas, text='3',command=lambda:addN(3)).place(x=200,y=300)
    
    boton4=Button(calc_canvas, text='4',command=lambda:addN(4)).place(x=100,y=250)
    boton5=Button(calc_canvas, text='5',command=lambda:addN(5)).place(x=150,y=250)
    boton6=Button(calc_canvas, text='6',command=lambda:addN(6)).place(x=200,y=250)
    
    boton7=Button(calc_canvas, text='7',command=lambda:addN(7)).place(x=100,y=200)
    boton8=Button(calc_canvas, text='8',command=lambda:addN(8)).place(x=150,y=200)
    boton9=Button(calc_canvas, text='9',command=lambda:addN(9)).place(x=200,y=200)
    
    boton_mas   =Button(calc_canvas, text='+',command=lambda:def_operacion(1)).place(x=250,y=150)
    boton_menos =Button(calc_canvas, text='-',command=lambda:def_operacion(2)).place(x=250,y=200)
    boton_mult  =Button(calc_canvas, text='X',command=lambda:def_operacion(3)).place(x=250,y=250)
    boton_div   =Button(calc_canvas, text='/',command=lambda:def_operacion(4)).place(x=250,y=300)
    
    boton_C     =Button(calc_canvas, text='C',command=lambda:clear(1)).place(x=150,y=150)
    boton_CE    =Button(calc_canvas, text='CE',command=lambda:clear(2)).place(x=200,y=150)
    boton_Punto =Button(calc_canvas, text='.',command=def_punto).place(x=200,y=350)
    boton_Igual =Button(calc_canvas, text='=',command=      resolver).place(x=250,y=350)

    
    calc.bind('<Return>', lambda self:resolver())
    calc.bind('<BackSpace>', lambda self:clear(2))
    calc.bind("<Key>",key_pressed )
    



    menubar = Menu(calc)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(11))

    calc.config(menu=menubar)




    calc.mainloop()




#controla teclas presionadas
def key_pressed(event):
    key = event.char
    #print (event)
    if key == '':
         None
    elif key in '0123456789':
        addN(int(key))
    elif key == '+':
        def_operacion(1)
    elif key == '-':
        def_operacion(2)
    elif key == '*':
        def_operacion(3)
    elif key == '/':
        def_operacion(4)
    elif key == '.':
        def_punto()
        



    
#limpia el cuadro d texto, los operandos y la operacion si es necesario
def clear(id):
    global textField , data1   , T1, numero1, numero2, operando, opr
    T1.delete(1.0, END)
    if id ==1:
        operando = 1
        opr = 0
        numero1= ''
        numero2= ''
    elif id==2:
        if operando == 1:
            numero1= ''
        elif operando ==2:
            numero2= ''
            

        

#agrega numeros a los operandos
def addN(id):
    global numero1, numero2 , operando, T1
    if operando ==1:
        numero1 += str(id)
        T1.insert(END, id)
    elif operando ==2:
        numero2 += str(id)
        T1.insert(END, id)
    
#define las operaciones a realizar
def def_operacion(id):
    global T1, T2, numero1, numero2, operando, opr, negativo
    
    if id == 2 and numero1=='' :
        if negativo == 0:
            negativo = 1
            numero1 = '-'
            T1.insert(END, '-')
        elif negativo ==1:
            negativo = 0
            numero1 = ''
            T1.delete(1.0, END)
                
    elif id == 1:
        opr = 1
        operando = 2
        T1.delete(1.0, END)
    elif id == 2:
        opr = 2
        operando = 2
        T1.delete(1.0, END)
    elif id == 3:
        opr = 3
        operando = 2
        T1.delete(1.0, END)
    elif id == 4:
        opr = 4
        operando = 2
        T1.delete(1.0, END)


#resuelve la operacion
def resolver():
    global numero1, numero2, operando,  opr, T1
    numero1= float(numero1)
    numero2= float(numero2)

    T1.delete(1.0, END)

    if opr == 4 and numero2 == 0:
        T1.insert(END, "Division 0")

    else: 
        if opr == 1:
            r = numero1 + numero2
        elif opr == 2:
            r = numero1 - numero2
        elif opr == 3:
            r = numero1 * numero2
        elif opr == 4:
            r = numero1 / numero2
        elif opr == 0:
            r = numero1
        #print (r)
        T1.insert(END, r)
    
    operando = 1
    opr = 0
    numero1= ''
    numero2= ''
    
    
        
#define el punto decimal
def def_punto():
    global numero1, numero2, operando, punto
    
    if not punto:
        if operando ==1:
            
            numero1 += "."
            
        elif operando ==2:
            numero2 += "."
        T1.insert(END, ".")
    else:
        None
        









        
######################################


def Ventana_agenda():
    global V2, agenda , frame_agenda


    V2 = Toplevel()
    V2.title( 'Agenda')
    V2.minsize(600,900)
    V2.resizable(width= False, height=False)
    V2.focus_force()


    




    menubar = Menu(V2)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(21))
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m1"], command=lambda:matriz_agenda(1))
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m6"], command=lambda:matriz_agenda(2))
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m3"], command=add_event_window)
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m4"], command=remove_event_window)
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m5"], command=ventana_dia)

    V2.config(menu=menubar)
    V2.mainloop()

#ventana para remover un evento en la agenda, puede removerse por ID o por nombre
def remove_event_window():
    global agenda, evento_r



    removeevent = Toplevel()
    removeevent.minsize(200,0)
    Label(removeevent, text="ID").grid(row=0, column=0)
    Label(removeevent, text=configuration["Lang"][lang]["P1"]["m10"]).grid(row=1, column=0)

    
    datar1 = StringVar()
    textField1 = Entry(removeevent,textvariable=datar1).grid(row=0, column=1)
    datar2 = StringVar()
    textField2 = Entry(removeevent,textvariable=datar2).grid(row=1, column=1)

    b_img=Button(removeevent, text="ID",command=lambda:remove_event(0)).grid(row=4, column=0)
    b_add=Button(removeevent, text=configuration["Lang"][lang]["P1"]["m10"],command=lambda:remove_event(1)).grid(row=4, column=1)

    evento_r = [datar1,datar2]
    
    removeevent.mainloop()

#funcion que determina si eliminar evento por nombre o por ID
def remove_event(id):
    global agenda, evento_r
    data1 = evento_r[0].get()
    data2 = evento_r[1].get()
    
    if id == 0:
        try:
            remover_id = int (data1) -1
        except:
            print (configuration["Lang"][lang]["P1"]["m3"])
            
        if remover_id > 0:
            #print (agenda)
            #print("----\n",remover_id)
            agenda = agenda[:remover_id ] + agenda[remover_id+1: ]
            fix_id_agenda()
            #print (agenda)
            
        else:
            print (configuration["Lang"][lang]["P1"]["m3"])
        

        
    elif id == 1 :

        if data2 != '':
            remove_event_x(data2)
        else:
            None

#arregla los IDs de los eventos enumerandolos otra vez
def fix_id_agenda():
    global agenda
    for fila in range(len(agenda)):
        agenda[fila][0] = str(fila+1)
        
#remueve evento por nombre
def remove_event_x(R):
    global agenda, evento_r
    for fila in range(len(agenda)):
        if agenda[fila][2] == R:
            #print (agenda)
            #print("----\n",fila)
            agenda = agenda[:fila]+agenda[fila+1:]
            fix_id_agenda()
            #print(agenda)
            break
        else:
            None

    
#ventana agrega evento
def add_event_window():
    global agenda ,event_N 
    
    newevent = Toplevel()
    newevent.minsize(200,0)
    
    Label(newevent, text="N").grid(row=0, column=0)
    Label(newevent, text=":").grid(row=1, column=0)
    Label(newevent, text="D").grid(row=2, column=0)
    Label(newevent, text="M").grid(row=3, column=0)
    Label(newevent, text=(configuration["Lang"][lang]["P1"]["m4"])[0]).grid(row=4, column=0)
    
    data1 = StringVar()
    textField1 = Entry(newevent,textvariable=data1).grid(row=0, column=1)
    data2 = StringVar()
    textField2 = Entry(newevent,textvariable=data2).grid(row=1, column=1)
    data3 = StringVar()
    textField3 = Entry(newevent,textvariable=data3).grid(row=2, column=1)
    data4 = StringVar()
    textField4 = Entry(newevent,textvariable=data4).grid(row=3, column=1)
    data5 = StringVar()
    textField5 = Entry(newevent,textvariable=data5).grid(row=4, column=1)


    b_add=Button(newevent, text=configuration["Lang"][lang]["P2"]["m3"],command=add_event).grid(row=5, column=1)

    num_last_event = int (agenda[-1][0])
    
    event_N = [str(num_last_event + 1) ,data1, data2, data3, data4 , data5]
    

    newevent.mainloop()

#funcion agrega evento    
def add_event():
    global agenda ,event_N
    
    #event_new = [event_N[0],'','','','','',]
    event_id = event_N[0]
    name = event_N[1].get()
    time = event_N[2].get()
    day = event_N[3].get()
    month = event_N[4].get()
    year = event_N[5].get()
    moment =year+month+day+time[:2]+time[3:]
    event_N = [event_N[0],moment,name]

    #print (event_N)
    
    agenda.append(event_N)
    #print (agenda)

#ventana para buscar una fecha    
def ventana_dia():
    global agenda  , agenda_d
    
    ventanadia = Toplevel()
    ventanadia.minsize(200,0)
    
    Label(ventanadia, text=configuration["Lang"][lang]["P1"]["m4"]).grid(row=1, column=0)

    
    datar1 = StringVar()
    textField1 = Entry(ventanadia,textvariable=datar1).grid(row=0, column=1)


    b_fecha=Button(ventanadia, text=configuration["Lang"][lang]["P2"]["m5"],command=lambda:matriz_agenda_R(datar1)).grid(row=4, column=1)

    

    ventanadia.mainloop()

#crea la matriz del resultado de la busqueda
def matriz_agenda_R(id):
    global V2, agenda , agenda_o , frame_agenda
    agenda = sorted(agenda, key=lambda evento: evento[0])
    agenda_o = sorted(agenda, key=lambda evento: evento[1])
    X = id.get()
    X = X[:4]+ X[5:7]+ X[8:]
    #print (X)
    
    try:
        frame_agenda.destroy()
    except:
        None

    frame_agenda = Frame(V2)
    frame_agenda.grid(row=0,column=0)
    Label(frame_agenda, text="ID").grid(row=0, column=0)

    
    matriz = []
    for fila in range(len(agenda_o)):
        if agenda_o[fila][1][:8]==X:
            matriz.append(agenda_o[fila])
        else:
            None
            
    #print (agenda_o)
    #print (matriz)


    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            if columna == 0:
                Label(frame_agenda, text=matriz[fila][0]).grid(row=fila+1, column=0)    
            elif columna == 1:
                #la fecha y hora estan en un mismo string, se debe separar para ser desplegado
                momento = matriz[fila][1]
                fecha = momento[6:8] + '/' + momento[4:6]+ '/' + momento[:4]
                hora = momento[8:10] + ':' + momento[10:]
                
                Label(frame_agenda, text=fecha).grid(row=fila+1, column=1)
                Label(frame_agenda, text=hora) .grid(row=fila+1, column=2)
            elif columna == 2:
                Label(frame_agenda, text=matriz[fila][2]).grid(row=fila+1, column=4)
                

                


    
    matriz = []


    
#crea la matriz de eventos ordenada por IDs o por fecha de evento
def matriz_agenda(id):
    
    global V2, agenda , agenda_o , frame_agenda

    agenda = sorted(agenda, key=lambda evento: evento[0])
    agenda_o = sorted(agenda, key=lambda evento: evento[1])
    
    try:
        frame_agenda.destroy()
    except:
        None

    frame_agenda = Frame(V2)
    frame_agenda.grid(row=0,column=0)
    Label(frame_agenda, text="ID").grid(row=0, column=0)

    
    if id == 1:
        matriz = agenda
    elif id == 2:
        matriz = agenda_o
    
    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            if columna == 0:
                Label(frame_agenda, text=matriz[fila][0]).grid(row=fila+1, column=0)    
            elif columna == 1:
                #la fecha y hora estan en un mismo string, se debe separar para ser desplegado
                momento = matriz[fila][1]
                fecha = momento[6:8] + '/' + momento[4:6]+ '/' + momento[:4]
                hora = momento[8:10] + ':' + momento[10:]
                
                Label(frame_agenda, text=fecha).grid(row=fila+1, column=1)
                Label(frame_agenda, text=hora) .grid(row=fila+1, column=2)
            elif columna == 2:
                Label(frame_agenda, text=matriz[fila][2]).grid(row=fila+1, column=4)
                

                




#lectura del archivo agenda
def leer_agenda():
    global agenda 
    arch_ag = open ("agenda.txt","r")
    agenda = []
    linea = arch_ag.readline()[:-1]
    agenda_base = []
    agenda_momento = ''
    contador = 1
    while linea !="":
        if contador <4 :
            agenda_base.append(linea)
            contador += 1
            linea = arch_ag.readline()[:-1]

                
        else:
            agenda.append(agenda_base)
            agenda_base = []
            contador = 1
            
    agenda.append(agenda_base)
    agenda_base = []
    contador = 1
    arch_ag.close()
    





######################################





def Ventana_contactos():
    global V1, contactos, Ordenada , frame_contactos


    V1 = Toplevel()
    V1.title( configuration["Lang"][lang]["V1"]["P3"])
    V1.minsize(600,900)
    V1.resizable(width= False, height=False)
    V1.focus_force()







    menubar = Menu(V1)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(31))
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m1"], command=lambda:matriz_contactos(1))
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m2"], command=lambda:matriz_contactos(2))
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m3"], command=add_contact_window)
    menubar.add_command(label=configuration["Lang"][lang]["P2"]["m4"], command=remove_contact_window)
    

    V1.config(menu=menubar)
    V1.mainloop()

#ventana para remover un contacto por su ID o Nombre
def remove_contact_window():
    global contactos, contacto_r



    removecontact = Toplevel()
    removecontact.minsize(200,0)
    Label(removecontact, text="ID").grid(row=0, column=0)
    Label(removecontact, text=configuration["Lang"][lang]["P1"]["m10"]).grid(row=1, column=0)

    
    datar1 = StringVar()
    textField1 = Entry(removecontact,textvariable=datar1).grid(row=0, column=1)
    datar2 = StringVar()
    textField2 = Entry(removecontact,textvariable=datar2).grid(row=1, column=1)

    b_img=Button(removecontact, text="ID",command=lambda:remove_contact(0)).grid(row=4, column=0)
    b_add=Button(removecontact, text=configuration["Lang"][lang]["P1"]["m10"],command=lambda:remove_contact(1)).grid(row=4, column=1)

    contacto_r = [datar1,datar2]
    
    removecontact.mainloop()

#determina el protocolo para remover el contacto
def remove_contact(id):
    global contactos , contacto_r
    data1 = contacto_r[0].get()
    data2 = contacto_r[1].get()
    
    if id == 0:
        try:
            remover_id = int (data1) -1
        except:
            print (configuration["Lang"][lang]["P1"]["m3"])
            
        if remover_id > 0:
            #print (contactos)
            #print("----\n",remover_id)
            contactos = contactos[:remover_id ] + contactos[remover_id+1: ]
            fix_id()
            #print (contactos)
            
        else:
            print (configuration["Lang"][lang]["P1"]["m3"])
        

        
    elif id == 1 :

        if data2 != '':
            remove_contact_x(data2)
        else:
            None


#arregla las IDs de los contactos enumerandolos nuevamente
def fix_id():
    global contactos
    for fila in range(len(contactos)):
        contactos[fila][0] = str(fila+1)
        
#remueve un contacto por el nombre
def remove_contact_x(R):
    global contactos , contacto
    for fila in range(len(contactos)):
        if contactos[fila][1] == R:
            #print (contactos)
            #print("----\n",fila)
            contactos = contactos[:fila]+contactos[fila+1:]
            fix_id()
            #print(contactos)
            break
        else:
            None

    
#ventana para agregar contacto
def add_contact_window():
    global contactos , nuevos_contactos, contacto_N , img_path, newcontact
    
    newcontact = Toplevel()
    Label(newcontact, text=configuration["Lang"][lang]["P1"]["m10"]).grid(row=0, column=0)
    Label(newcontact, text=configuration["Lang"][lang]["P3"]["m1"]).grid(row=1, column=0)
    Label(newcontact, text=configuration["Lang"][lang]["P3"]["m2"]).grid(row=2, column=0)
    Label(newcontact, text=configuration["Lang"][lang]["P3"]["m3"]).grid(row=3, column=0)
    
    data1 = StringVar()
    textField1 = Entry(newcontact,textvariable=data1).grid(row=0, column=1)
    data2 = StringVar()
    textField2 = Entry(newcontact,textvariable=data2).grid(row=1, column=1)
    data3 = StringVar()
    textField3 = Entry(newcontact,textvariable=data3).grid(row=2, column=1)
    data4 = StringVar()
    textField4 = Entry(newcontact,textvariable=data4).grid(row=3, column=1)


    img_path = '8.PNG'
    b_img=Button(newcontact, text="Img",command=get_image).grid(row=4, column=0)
    b_add=Button(newcontact, text=configuration["Lang"][lang]["P2"]["m3"],command=add_contact).grid(row=4, column=1)

   


    num_last_contact = int (contactos[-1][0])
    
    contacto_N = [str(num_last_contact + 1) ,data1, data2, data3, data4 , img_path]

    newcontact.mainloop()

#funcion para agegar un contacto
def add_contact():
    global contactos, nuevos_contactos, contacto_N, img_path
    contacto = [contacto_N[0],'','','','','']
    contacto[1] = contacto_N[1].get()
    contacto[2] = contacto_N[2].get()
    contacto[3] = contacto_N[3].get()
    contacto[4] = contacto_N[4].get()
    contacto[5] = img_path
    #print (contacto)
    contactos.append(contacto)

    


#Crea la matriz de contactos
def matriz_contactos(x):
    
    global V1, contactos, Ordenada ,frame_contactos, imagenes, imagenesOrd

    contactos = sorted(contactos, key=lambda contact: contact[0])
    Ordenada = sorted(contactos, key=lambda contact: contact[1])
    
    t_cont = [list(i) for i in zip(*contactos)]
    imagenes = (t_cont[5])
    t_ord = [list(i) for i in zip(*Ordenada)]
    imagenesOrd = (t_ord[5])



    try:
        frame_contactos.destroy()
    except:
        None

    frame_contactos = Frame(V1)
    frame_contactos.grid(row=0,column=0)
    Label(frame_contactos, text="ID").grid(row=0, column=0)

    
    if x == 1:
        x = contactos
        y = imagenes
    elif x == 2:
        x = Ordenada
        y = imagenesOrd
    
    for fila in range(len(x)):
        for columna in range(0,6):
            if columna != 5:
                Label(frame_contactos, text=x[fila][columna]).grid(row=fila+1, column=columna)
            elif columna == 5:
                #img=load_img("fondo1.PNG")
                #foto = c_inicio.create_image(200,300,image=img)
                None


    for contador in range(len(y)):
        infile = y[contador]

        im=load_img(infile)
        #im = Image.open(infile)

        myvar = Label(frame_contactos, image=im)
        myvar.image = im
        myvar.grid(row=contador+1, column=5)
    

#obtiene direccion de una imagen que el usuario selecciona
def get_image():
    global img_path, newcontact
    
    newcontact.filename =  filedialog.askopenfilename(initialdir = "E:/Images",title = configuration["Lang"][lang]["P3"]["m4"],filetypes = (("PNG files","*.PNG"),("all files","*.*")))
    img_path = (newcontact.filename)
    newcontact.focus()

#lectura del archivo contactos
def leer_contactos():
    global contactos , Ordenada , imagenes, imagenesOrd
    arch_contc = open ("contactos.txt","r")
    contactos = []
    linea = arch_contc.readline()[:-1]
    contactobase = []
    contador = 1
    while linea !="":
        if contador <7 :
            contactobase.append(linea)
            contador += 1
            linea = arch_contc.readline()[:-1]

                
        else:
            contactos.append(contactobase)
            contactobase = []
            contador = 1
    contactos.append(contactobase)
    contactobase = []
    contador = 1
    arch_contc.close()
    #for contacto in contactos:
    #    contacto[0] = int(contacto[0])

    #print (contactos)
    

    










######################################


from tkinter import *
import tkinter , os
from threading import Thread
import random



global listapalabras , letrasingresadas , letras_palabra, vidas , termino ,  palabra
palabra = ''
listapalabras = []
letras_ingresadas = ['']
vidas = 5
termino = True
letras_palabra = []

#extrae las palaras del archivo dependiendo del idioma
def leer_palabras():
    global listapalabras , lang
    arch_pal = open('palabras.txt','r')
    palabras_es = []
    palabras_en = []
    linea = arch_pal.readline()[:-1]
    lan = False
    while linea != '':
        if linea == "@":
            
            lan = True
            linea = arch_pal.readline()[:-1]
        else:
            if not lan:
                palabras_es += [linea]
            else:
                palabras_en += [linea]
            linea = arch_pal.readline()[:-1]
         
    arch_pal.close()
 
    if lang == 'es':
        listapalabras = palabras_es
    else:
        listapalabras = palabras_en
    #print (listapalabras)
    

    
#selecciona la palabra a utilizar
def seleccionar_palabra():
    global listapalabras, palabra
    
    palabra = random.choice(listapalabras) + ' '
    
    letras_palabra = list(palabra)
    #print (palabra, letras_palabra)


    
#aqui se recibe el input de la letra del cuadro de texto
def ingresoletras(letra):
    global letras_ingresadas , vidas , palabra  , data_letra
    lista_letras = 'abcdefghijklmnopqrstuvwxyz '
    try:
        letra = letra.get()
        data_letra.set('')
    except:
        None
    if isinstance (letra,str) and len(letra) == 1:
        letra = letra.lower()
        if letra in letras_ingresadas:
            print (configuration["Lang"][lang]["P1"]["m3"])
            vidas +=1
        else:
            letras_ingresadas += [letra]
        if letra not in palabra:
            vidas -= 1
            dibujar()
        else:
            None
        escribir_palabra()

#escribe la palabra        
def escribir_palabra():
    global letras_ingresadas , palabra, canv_juego , canv_palabra
    try:
        None
        #canv_palabra.destroy()
    except:
        None
    #print (letras_ingresadas, '\n' , palabra)
    canv_palabra = tkinter.Canvas(canv_juego,width=600,height=300, bg='white').place(x=0,y=600)
    cont = 1
    for letra in palabra:
        if letra in letras_ingresadas:
            Label(canv_juego, text=letra, font=("Helvetica", 20)).place(x=cont*50,y=700)
        else:
            Label(canv_juego, text='_', font=("Helvetica", 20)).place(x=cont*50,y=700)
        cont += 1
            
            
            


    

#dibuja el ahorcado
def dibujar():
    global juego , canv_juego, vidas
    
    if vidas == 0:
        Label(canv_juego, text=configuration["Lang"][lang]["P4"]["m2"]).place(x=200,y=100, tags='bicho')
        canv_juego.create_line(300, 450, 350, 500, fill="red", tags='bicho')
    elif vidas == 1:
        canv_juego.create_line(300, 450, 250, 500, fill="red", tags='bicho')
    elif vidas == 2:
        canv_juego.create_line(250, 400, 350, 400, fill="red", tags='bicho')
    elif vidas == 3:
        canv_juego.create_line(300, 350, 300, 450, fill="red", tags='bicho')
    elif vidas == 4:
        l4 = canv_juego.create_oval(275, 350, 325, 300, fill="red", tags='bicho')
    else:
        None

#reinicia el juego
def reiniciar():
    global  listapalabras , letrasingresadas , letras_palabra, vidas , termino ,  palabra ,canv_juego
    letras_ingresadas = ['']
    vidas = 5
    termino = True
    letras_palabra = []
    seleccionar_palabra()
    canv_juego.delete('bicho')
    ingresoletras(' ')
    #print (letras_ingresadas,vidas)
    






def ventana_juego():
    global juego , canv_juego , data_letra


    juego = Toplevel()
    juego.title(" Tkinter ")
    juego.minsize(600,900)
    juego.resizable(width= False, height=False)
    canv_juego= tkinter.Canvas(juego,width=600,height=900, bg='grey')
    canv_juego.place(x=0,y=0)




    data_letra = StringVar()
    textField_juego = Entry(canv_juego,textvariable=data_letra).place(x=100,y=100)
    
    b1=Button(canv_juego, text=configuration["Lang"][lang]["P4"]["m3"],command=lambda:ingresoletras(data_letra)).place(x=100,y=150)    
    b2=Button(canv_juego, text=configuration["Lang"][lang]["P4"]["m4"],command=reiniciar).place(x=150,y=150)
    
    canv_palabra = tkinter.Canvas(canv_juego,width=600,height=300, bg='white').place(x=0,y=600)


    leer_palabras()
    seleccionar_palabra()

    menubar = Menu(juego)
    menubar.add_command(label=configuration["Lang"][lang]["V1"]["P0"], command=lambda:buttons(41))
    juego.config(menu=menubar)


    
    

    juego.mainloop()






    

######################################





ventana_idioma()
