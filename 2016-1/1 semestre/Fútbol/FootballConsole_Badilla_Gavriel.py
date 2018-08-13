from tkinter import *
from tkinter import messagebox
from threading import Thread
from  tkinter import filedialog
import time, os, winsound, random

import ListaJugadoresPredeterminados as ListaJugadores
import ListaEquipos

global Inicio,window,about,scores,ayuda,configuration_window,select,lang,team,game,canvas,ListaJugadores,ACTIVE,ListaEquipos


ACTIVE = True
lang="en"
jugadores_extra = []

configuration = {
	"APP" : {
		"Institución" : "Tecnológico de Costa Rica",
		"Carrera" : "Ingeniería en Computadores",
		"Curso" : "Taller de Programación",
		"Profesor" : "Ing. Milton Villegas Lemus",
		"Nombre_del_proyecto" : "Football Console",
		"Versión" : "1.0",
		"Fecha de emisión" : "30/05/2016",
		"Autores" : [
			{
				"Nombre" : "Yendry Badilla Gutiérrez",
				"Carné" : "2016113047"
			},
			{
				"Nombre" : "Alexis Gavriel Gómez",
				"Carné" : "2016085662"	
			}
		]
	},
	"Game" : {
		"Width" : 800,
		"Height" : 600,
		"Widthc" : 350,
		"Heightc" : 100,
		"Widths" : 350,
		"Heights" : 100,
		"resizable" : {
			"Width" : False,
			"Height" : False
		},
		"sound" : True,
		"background_color" : "black"
	},
	"Files" : {
		"images" : {
			"background" : "Files/images/background.gif",
			"icon" : "Files/images/icon.ico",
			"USA" : "Files/images/USA.gif",
			"CR" : "Files/images/CR.gif",
			"bg" : "Files/images/bg.gif"
		},
		"sounds" : {
			"inicio" : "Files/sounds/soundtrack.wav",
			"game" : "Files/sounds/game.wav",
		},
		"data" : {
			"scores" : "scores.txt"
		}
	},
	"Lang" : {
		"en" : {
			"Botones" : {
				"Play" : "Play",
				"Return" : "Go Back!",
				"Exit" : "Exit",
				"About" : "About",
				"High_Scores" : "High Scores",
				"Help" : "Help",
				"configuration" : "Configuration",
				"Add" : "Add a new player",
				"addimage" : "Add image",
				"select" : "Select a player",
				"TEAM" : "Select a team"
			},
			"Messages" : {
				"Exit" : "Do you want to exit? :(",
				"Bye" : "Bye!",
				"Return" : "Do you want to return to the home window?",
				"Empty" : "You must type player's name that you want to add",
				"Greeting" : "Continue creating your team to play"
			},
			"Labels" : {
				"Score" : "Score",
				"Create" : "Create your team",
				"new" : "New player",
				"SelectT" : "Select your team"
			},
		},
		"es" : {
			"Botones" : {
				"Play" : "Jugar",
				"Return" : "Regresar",
				"Exit" : "Salir",
				"About" : "Acerca de",
				"High_Scores" : "Máximas\nPuntuaciones",
				"Help" : "Ayuda",
				"configuration" : "Configuración",
				"Add" : "Añadir un nuevo jugador",
				"addimage" : "Añadir imagen",
				"select" : "Selecciona un jugador",
				"TEAM" : "Selecciona un equipo"
			},
			"Messages" : {
				"Exit" : "¿Deseas finalizar el programa? :(",
				"Bye" : "¡Adiós!",
				"Return" : "¿Deseas regresar a la ventana inicial?",
				"Empty" : "Debes indicar el nombre del jugador que deseas agregar",
				"Greeting" : "Continúa formando tu equipo para jugar"
			},
			"Labels" : {
				"Score" : "Puntos",
				"Create" : "Crea tu equipo",
				"new" : "Nuevo jugador",
				"SelectT" : "Selecciona tu equipo"
			}
		}
	}
}


def say(title,msj):	#Mensajes
	messagebox.showinfo(title, msj)
	return 0
def si(title,msj): #Mensajes
	val = messagebox.askokcancel(title,msj)
	return val

def load_image(path):		#Función para cargar las imágenes
	img = PhotoImage(file = path)
	return img

def boot(l):      #Lenguaje inicio
	global Inicio,lang
	if l==0:
		lang="en"
	else:
		lang="es"
	Inicio.destroy()
	home_window()

def lang_setup():		#Ventana de inicio para seleccionar el lenguaje
	global Inicio
	Inicio = Tk()
	Inicio.title("Language / Idioma")
	Inicio.geometry("502x100+500+100")
	Inicio.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
	Inicio.iconbitmap(configuration["Files"]["images"]["icon"])

	#Objetos secundarios
	img_USA = load_image(configuration["Files"]["images"]["USA"])
	img_CR = load_image(configuration["Files"]["images"]["CR"])

	#Creacion de objetos dentro del formulario
	Boton_USA = Button(Inicio, text="English",image=img_USA,command=lambda: boot(0),width=250,height=100)
	Boton_CR = Button(Inicio,text="Español",image=img_CR,command=lambda: boot(1),width=250,height=100)

	#Dibujar
	Boton_USA.place(x=1,y=0)
	Boton_CR.place(x=251,y=0)
	Inicio.mainloop()
	return 0

def button_listener(id):	#Función que determina la acción de cada boton
	global window,about,lang,game,select,team,configuration_window,ACTIVE
	if id==1:
		window.withdraw()
		select_player()
	elif id==2:
		window.withdraw() #minimiza la ventana home y después window.deiconify() para regresar a la ventana anterior
		about_window()
	elif id==3:
		window.deiconify()
		about.destroy()
	elif id==4:
		if si(configuration["APP"]["Nombre_del_proyecto"],configuration["Lang"][lang]["Messages"]["Exit"]):
			say(configuration["APP"]["Nombre_del_proyecto"],configuration["Lang"][lang]["Messages"]["Bye"])
			exit()
	elif id==5:
		window.withdraw()
		scores()
	elif id==6:
		window.deiconify()
		scores.destroy()
	elif id==7:
		window.withdraw()
		ayuda()
	elif id==8:
		window.deiconify()
		ayuda.destroy()
	elif id==9:
		if si(configuration["APP"]["Nombre_del_proyecto"],configuration["Lang"][lang]["Messages"]["Return"]):
			ACTIVE = False
			game.destroy()
			window.deiconify()
	elif id==10:
		window.withdraw()
		config_win()
	elif id==11:
		window.deiconify()
		configuration_window.destroy()
	elif id==12:
		select.destroy()
		select_team()
	elif id==13:
		team.destroy()
		play()
	else:
		print("Error")


def threads(id):			#Función que contiene los threads necesarios para el juego
	if id == 1:
		music_thread = Thread(target=music,args=())
		music_thread.daemon = True		#Le indica que corra asincrónicamente
		music_thread.start()			#Lanza el thread
	elif id==2:
		game_music_thread = Thread(target=game_music,args=())
		game_music_thread.daemon = True		#Le indica que corra asincrónicamente
		game_music_thread.start()			#Lanza el thread
	else:
		print("Error")


def home_window():		#Ventana de inicio del juego
	global window,lang,ListaJugadores
	window = Tk()
	window.title(configuration["APP"]["Nombre_del_proyecto"]) #Título de la ventana
	window.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])  #El tamaño de la ventana no puede ser cambiado
	window.iconbitmap(configuration["Files"]["images"]["icon"]) #Representación del ícono
	window.protocol("WM_DELETE_WINDOW",lambda:button_listener(4))
	window.geometry(											#Establece la geometría en la que siempre aparece la ventana
		str(configuration["Game"]["Width"])+
		"x"+
		str(configuration["Game"]["Height"])+
		"+"+
		str(int((window.winfo_screenwidth()/2)-configuration["Game"]["Width"]/2))+
		"+"+
		str(int((window.winfo_screenheight()/2)-configuration["Game"]["Height"]/2))
	)
	
	#Background de la ventana
	fondo_imagen = load_image(configuration["Files"]["images"]["background"])
	fondo = Label(window,image=fondo_imagen)
	fondo.pack()
	
	#Botones
	button_play = Button(window,text=configuration["Lang"][lang]["Botones"]["Play"],width=12,height=3,command=lambda:button_listener(1),bg="white",font=("Arial",12))		#Creación del botón para jugar
	button_play.place(x=100,y=100)
	button_about = Button(window,text=configuration["Lang"][lang]["Botones"]["About"],width=12,height=3,command=lambda:button_listener(2),bg="white",font=("Arial",12))		#Creación del botón para mostrar la ventana de about
	button_about.place(x=100,y=400)
	button_help = Button(window,text=configuration["Lang"][lang]["Botones"]["Help"],width=12,height=3,command=lambda:button_listener(7),bg="white",font=("Arial",12))		#Creación del botón para ventana de ayuda
	button_help.place(x=100,y=300)
	button_config = Button(window,text=configuration["Lang"][lang]["Botones"]["configuration"],width=12,height=3,command=lambda:button_listener(10),bg="white",font=("Arial",12))	#Creación del botón para ventana de configuracion del equipo
	button_config.place(x=100,y=200)
	button_exit = Button(window,text=configuration["Lang"][lang]["Botones"]["Exit"],width=12,height=3,command=lambda:button_listener(4),bg="white",font=("Arial",12))  #Creación del botón para salir
	button_exit.place(x=100,y=500)
	

	#play_music()
	stop_game_music()

	window.mainloop()


def about_window():			#Ventana de about #PONER IMÁGENES de nosotros!!!!
	global window,about
	#Crear ventana
	about = Tk()
	about.config(bg="gray")
	about.title("About")
	about.minsize(configuration["Game"]["Width"], configuration["Game"]["Height"])
	about.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
	about.iconbitmap(configuration["Files"]["images"]["icon"])

	#objetos y titulos
	button_back = Button(about,text="Back",width=10,height=2,command=lambda:button_listener(3),bg="black",fg="white",font=("Arial",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_back.place(x=650,y=500)
	encabezado = configuration["APP"]["Institución"] + "\n" +configuration["APP"]["Carrera"] +"\nProfesor: " + configuration["APP"]["Profesor"] +"\nNombre del Proyecto: " + configuration["APP"]["Nombre_del_proyecto"] +"\nVersión: " + configuration["APP"]["Versión"] +"\nFecha de emisión: " + configuration["APP"]["Fecha de emisión"] +"\nAutores: " + configuration["APP"]["Autores"][0]["Nombre"] + "\n" + "\t" + configuration["APP"]["Autores"][1]["Nombre"] + "\nCarné: " + configuration["APP"]["Autores"][0]["Carné"] + "\n" + "\t" + configuration["APP"]["Autores"][1]["Carné"]

	info = Label(about,text=encabezado,font=("Arial",20),fg="white",bg="gray")  #Label para agregar la información en la ventana about
	info.place(x=170,y=100)


	stop_music()

"""
------En caso de nesecitar una ventana de puntajes------
def scores():		#Ventana Puntajes
    global window,scores,lang
    scores = Tk()
    scores.config(bg="gray")
    scores.title(configuration["Lang"][lang]["Botones"]["High_Scores"])
    scores.minsize(configuration["Game"]["Width"], configuration["Game"]["Height"])
    scores.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
    scores.iconbitmap(configuration["Files"]["images"]["icon"])

    button_back = Button(scores,text="Back",width=10,height=2,command=lambda:button_listener(6),bg="black",fg="white",font=("Arial",12)) #Creación del botón para regresar a la ventana de inicio del juego
    button_back.place(x=650,y=500)

    stop_music()
"""

def ayuda():	#Ventana de ayuda
	global window,ayuda,lang
	#Crear ventana
	ayuda = Tk()
	ayuda.config(bg="gray")
	ayuda.title(configuration["Lang"][lang]["Botones"]["High_Scores"])
	ayuda.minsize(configuration["Game"]["Width"], configuration["Game"]["Height"])
	ayuda.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
	ayuda.iconbitmap(configuration["Files"]["images"]["icon"])

	#crear botones
	button_back = Button(ayuda,text="Back",width=10,height=2,command=lambda:button_listener(8),bg="black",fg="white",font=("Arial",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_back.place(x=650,y=500)

	stop_music()

def Add_Jugador(name): #Eventos para la ventana de configuración, añade los jugadores extra a la lista
	global window,configuration_window,lang ,jugadores_extra
	if name=="":
		say(configuration["APP"]["Nombre_del_proyecto"],configuration["Lang"][lang]["Messages"]["Empty"])
	else:
		open_file = filedialog.askopenfile() #Examinar en los archivos
		if open_file.name == None:
			say(configuration["APP"]["Nombre_del_proyecto"],"Debe indicar una imagen")
		else:
			say(configuration["APP"]["Nombre_del_proyecto"],"Jugador: " + name + " agregado")
			temporal = {
				"Nombre" : name,
				"Imagen" : open_file.name
			}
			jugadores_extra.append(temporal) #añade el jugador extra(nuevo) a la lista
			configuration_window.destroy()
			window.deiconify()


def select_player(): #Seleccionar un jugador predeterminado o extra
	global window,select,jugadores,ListaJugadores
	#crear ventana
	select = Tk()
	select.title(configuration["Lang"][lang]["Labels"]["Create"])
	select.config(bg="black")
	select.minsize(configuration["Game"]["Widths"], configuration["Game"]["Heights"])
	select.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
	select.iconbitmap(configuration["Files"]["images"]["icon"])
	
	####Crear menu button con checkbutton para seleccionar jugadores#### 
	selection = Menubutton(select, activebackground="blue", text=configuration["Lang"][lang]["Botones"]["select"], font=("Consolas",15), relief=RAISED)
	selection.grid()
	selection.menu = Menu(selection, tearoff=0, font=("Consolas",15), activebackground="blue")
	selection["menu"] = selection.menu

	for jugador in ListaJugadores.Jugadores:
		selection.menu.add_checkbutton(label=jugador["Nombre"], font=("Consolas",12))

	for jugador in jugadores_extra:
		selection.menu.add_checkbutton(label=jugador["Nombre"], font=("Consolas",12))

	#crear botones
	button_continue = Button(select,text="Continue",width=10,height=2,command=lambda:button_listener(12),bg="black",fg="white",font=("Consolas",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_continue.grid()

	selection.grid()
	

	

	#stop_music()
	#play_game_music()

	
def config_win():	#Ventana de configuración para añadir jugadores extra
	global window,configuration_window,lang
	#Crear ventana
	configuration_window = Toplevel(window)
	configuration_window.title(configuration["Lang"][lang]["Botones"]["configuration"])
	configuration_window.minsize(configuration["Game"]["Widthc"], configuration["Game"]["Heightc"])
	configuration_window.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
	configuration_window.iconbitmap(configuration["Files"]["images"]["icon"])
	configuration_window.config(bg="black")
	
	#creación de objetos
	titulo = Label(configuration_window, text=configuration["Lang"][lang]["Labels"]["new"],font=("Consolas",15),bg="black",fg="white").grid(row=0,column=0)
	
	variablenombre = StringVar()
	nombre = Entry(configuration_window,font=("Consolas",20),width=20,textvariable=variablenombre)
	nombre.grid(row=1,column=0)
	button_add = Button(configuration_window,width=15,bd=0,bg="black",fg="white",command=lambda:Add_Jugador(nombre.get()),text=configuration["Lang"][lang]["Botones"]["Add"],font=("Consolas",15)).grid(row=2,column=0)
	#button_addimage = Button(configuration_window,width=15,bd=0,bg="black",fg="white",command=lambda:button_listener(12),text=configuration["Lang"][lang]["Botones"]["addimage"],font=("Consolas",15)).grid(row=3,column=0)
	button_return = Button(configuration_window,width=15,bd=0,bg="black",fg="white",command=lambda:button_listener(11),text=configuration["Lang"][lang]["Botones"]["Return"],font=("Consolas",15)).grid(row=3,column=1)
	
	configuration_window.protocol("WM_DELETE_WINDOW", lambda:button_listener(11))

	stop_music()


def select_team(): 
	global team,lang,canvas,window
	#Crear ventana
	team = Toplevel(window)
	team.title(configuration["Lang"][lang]["Labels"]["SelectT"])
	team.minsize(configuration["Game"]["Widths"], configuration["Game"]["Heights"])
	team.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])  #El tamaño de la ventana no puede ser cambiado
	team.config(bg="black")
	team.iconbitmap(configuration["Files"]["images"]["icon"])


	####Crear menu button con checkbutton para seleccionar equipos#### 
	team_selection = Menubutton(team, activebackground="blue", text=configuration["Lang"][lang]["Botones"]["TEAM"], font=("Consolas",15), relief=RAISED)
	team_selection.grid()
	team_selection.menu = Menu(team_selection, tearoff=0, font=("Consolas",15), activebackground="blue")
	team_selection["menu"] = team_selection.menu

	for equipo in ListaEquipos.Equipos:
		team_selection.menu.add_checkbutton(label=equipo["Nombre"], font=("Consolas",12))

	#crear botones
	button_continue = Button(team,text="Continue",width=10,height=2,command=lambda:button_listener(13),bg="black",fg="white",font=("Consolas",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_continue.grid()

	team_selection.grid()



def play():
	pass
	
#Funciones que controlan el sonido del programa
def music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(configuration["Files"]["sounds"]["inicio"],winsound.SND_ASYNC)

def play_music():
	if configuration["Game"]["sound"]:
		threads(1)

def stop_music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(None,0)

def game_music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(configuration["Files"]["sounds"]["game"],winsound.SND_ASYNC)
def play_game_music():
	if configuration["Game"]["sound"]:
		threads(2)
def stop_game_music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(None,0)

lang_setup()