from tkinter import *
from tkinter import messagebox
from threading import Thread
from  tkinter import filedialog
import time, os, winsound, random

import ListaJugadoresPredeterminados as ListaJugadores
import ListaEquipos

global Inicio,window,about,scores,ayuda,configuration_window,select,lang,team,game,portero,arbitro,canvas,ListaJugadores,ACTIVE,ListaEquipos


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
			"gamebg" : "Files/images/gamebg.gif",
			"Yendry" : "Files/images/Árbitros/Yendry.gif",
			"Alexis" : "Files/images/Árbitros/Alexis.gif",
			"playbg" : "Files/images/playbg.gif"
		},
		"sounds" : {
			"inicio" : "Files/sounds/soundtrack.wav",
			"game" : "Files/sounds/game.wav",
			"play" : "Files/sounds/play.wav"
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
				"TEAM" : "Select a team",
				"Continue" : "Continue",
				"goalkeeper" : "Select a goalkeeper",
				"referee" : "Select a referee"
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
				"SelectT" : "Select your team",
				"SelectA" : "Select a referee"
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
				"TEAM" : "Selecciona un equipo",
				"Continue" : "Continuar",
				"goalkeeper" : "Selecciona un portero",
				"referee" : "Selecciona un árbitro"
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
				"SelectT" : "Selecciona tu equipo",
				"SelectA" : "Selecciona un árbitro"
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
	Inicio.withdraw()
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
	global window,about,lang,game,ayuda,select,team,configuration_window,ACTIVE, boot, Inicio
	if id==1:
		window.withdraw()
		stop_music()
		play_game_music()
		select_team()
	elif id==2:
		window.withdraw() #minimiza la ventana home y después window.deiconify() para regresar a la ventana anterior
		stop_music()
		about_window()
	elif id==3:
		window.deiconify()
		play_music()
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
		stop_music()
		ayuda()
	elif id==8:
		window.deiconify()
		play_music()
		ayuda.destroy()
	elif id==9:
		if si(configuration["APP"]["Nombre_del_proyecto"],configuration["Lang"][lang]["Messages"]["Return"]):
			ACTIVE = False
			game.destroy()
			window.deiconify()
	elif id==10:
		window.withdraw()
		stop_music()
		play_game_music()
		config_win()
	elif id==11:
		window.deiconify()
		configuration_window.destroy()
		stop_game_music()
		play_music()
	elif id==12:
		team.deiconify()
		select_player()
	elif id==13:
		select.destroy()
		select_goalkeeper()
	elif id==14:
		game.destroy()
		team.destroy()
		stop_start_music()
		play_music()
		window.deiconify()
	elif id==15:
		select.destroy()
		window.deiconify()
		stop_game_music()
		play_music()
	elif id==16:
		team.destroy()
		window.deiconify()
		stop_game_music()
		play_music()
	elif id==17:
		portero.destroy()
		select_arbitro()
	elif id==18:
		portero.destroy()
		stop_start_music()
		play_music()
		window.deiconify()
	elif id==19:
		arbitro.destroy()
		stop_game_music()
		play_music()
		window.deiconify()
	elif id==20:
		arbitro.destroy()
		play_start_music()
		play()

	elif id==50:
		window.withdraw() #minimiza la ventana home y después window.deiconify() para regresar a la ventana anterior
		stop_music()
		play2()
	elif id==51:
		window.withdraw() #minimiza la ventana home y después window.deiconify() para regresar a la ventana anterior
		stop_music()
		config2()
	elif id == 100:
                Inicio.deiconify()
                window.destroy
	
	else:
		print("Error")


def threads(id):		#Función que contiene los threads necesarios para el juego
	if id == 1:
		music_thread = Thread(target=music,args=())
		music_thread.daemon = True		#Le indica que corra asincrónicamente
		music_thread.start()			#Lanza el thread
	elif id==2:
		game_music_thread = Thread(target=game_music,args=())
		game_music_thread.daemon = True		#Le indica que corra asincrónicamente
		game_music_thread.start()			#Lanza el thread
	elif id==3:
		start_music_thread = Thread(target=start_music,args=())
		start_music_thread.daemon = True		#Le indica que corra asincrónicamente
		start_music_thread.start()			#Lanza el thread
	else:
		print("Error")

############HAY QUE AÑADIR EL NOMBRE DEL JUEGO EN HOME#####################
def home_window():		#Ventana de inicio (principal) del juego
	global window,lang,ListaJugadores
	window = Toplevel()
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
	button_play2 = Button(window,text='Play2',width=12,height=3,command=lambda:button_listener(50),bg="white",font=("Arial",12))		#Creación del botón para jugar
	button_play2.place(x=220,y=100)        
	button_config2 = Button(window,text="configuration2",width=12,height=3,command=lambda:button_listener(51),bg="white",font=("Arial",12))	#Creación del botón para ventana de configuracion del equipo
	button_config2.place(x=220,y=200)
	button_config2 = Button(window,text="configuration2",width=12,height=3,command=lambda:button_listener(100),bg="white",font=("Arial",12))	#Creación del botón para ventana de configuracion del equipo
	button_config2.place(x=300,y=200)
	

	play_music()

	window.mainloop()


def about_window():		#Ventana de about
	global about,lang
	#Crear ventana
	about = Toplevel(window)
	about.config(bg="gray")
	about.title("About")
	about.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
	about.iconbitmap(configuration["Files"]["images"]["icon"])
	about.protocol("WM_DELETE_WINDOW",lambda:button_listener(3))
	about.geometry(											#Establece la geometría en la que siempre aparece la ventana
		str(configuration["Game"]["Width"])+
		"x"+
		str(configuration["Game"]["Height"])+
		"+"+
		str(int((about.winfo_screenwidth()/2)-configuration["Game"]["Width"]/2))+
		"+"+
		str(int((about.winfo_screenheight()/2)-configuration["Game"]["Height"]/2))
	)
	
	#Background de la ventana
	fondo_imagen = load_image(configuration["Files"]["images"]["gamebg"])
	fondo = Label(about,image=fondo_imagen)
	fondo.pack()

	#objetos y titulos
	button_back = Button(about,text="Back",width=10,height=2,command=lambda:button_listener(3),bg="black",fg="white",font=("Arial",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_back.place(x=650,y=500)
	encabezado = configuration["APP"]["Institución"] + "\n" +configuration["APP"]["Carrera"] +"\nProfesor: " + configuration["APP"]["Profesor"] +"\nNombre del Proyecto: " + configuration["APP"]["Nombre_del_proyecto"] +"\nVersión: " + configuration["APP"]["Versión"] +"\nFecha de emisión: " + configuration["APP"]["Fecha de emisión"] +"\nAutores: " + configuration["APP"]["Autores"][0]["Nombre"] + "\n" + "\t" + configuration["APP"]["Autores"][1]["Nombre"] + "\nCarné: " + configuration["APP"]["Autores"][0]["Carné"] + "\n" + "\t" + configuration["APP"]["Autores"][1]["Carné"]

	info = Label(about,text=encabezado,font=("Arial",20),fg="white",bg="blue")  #Label para agregar la información en la ventana about
	info.place(x=170,y=100)

	yendry = load_image(configuration["Files"]["images"]["Yendry"])
	alexis = load_image(configuration["Files"]["images"]["Alexis"])

	image_y = Label(about,image=yendry)
	image_a = Label(about,image=alexis)
	image_y.place(x=50,y=100)
	image_a.place(x=670,y=100)

	about.mainloop()



#-----ventana de puntajes------




	
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


def ayuda():	#Ventana de ayuda
	global window,lang,ayuda
	ayuda = Toplevel(window)
	ayuda.title(configuration["APP"]["Nombre_del_proyecto"]) #Título de la ventana
	ayuda.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])  #El tamaño de la ventana no puede ser cambiado
	ayuda.iconbitmap(configuration["Files"]["images"]["icon"]) #Representación del ícono
	ayuda.protocol("WM_DELETE_WINDOW",lambda:button_listener(8))
	ayuda.geometry(											#Establece la geometría en la que siempre aparece la ventana
		str(configuration["Game"]["Width"])+
		"x"+
		str(configuration["Game"]["Height"])+
		"+"+
		str(int((ayuda.winfo_screenwidth()/2)-configuration["Game"]["Width"]/2))+
		"+"+
		str(int((ayuda.winfo_screenheight()/2)-configuration["Game"]["Height"]/2))
	)
	
	#Background de la ventana
	fondo_imagen = load_image(configuration["Files"]["images"]["gamebg"])
	fondo = Label(ayuda,image=fondo_imagen)
	fondo.pack()
	
	#Botones
	button_back = Button(ayuda,text="Back",width=10,height=2,command=lambda:button_listener(8),bg="black",fg="white",font=("Arial",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_back.place(x=650,y=500)

	ayuda.mainloop()


def Add_Jugador(name): #Eventos para la ventana de configuración, añade los jugadores extra a la lista
	global window,configuration_window,lang,jugadores_extra
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


def select_team(): 
	global team,lang,window
	#Crear ventana
	team = Toplevel(window)
	team.title(configuration["Lang"][lang]["Labels"]["SelectT"])
	team.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])  #El tamaño de la ventana no puede ser cambiado
	team.config(bg="black")
	team.iconbitmap(configuration["Files"]["images"]["icon"])
	team.protocol("WM_DELETE_WINDOW",lambda:button_listener(16))
	team.geometry(											#Establece la geometría en la que siempre aparece la ventana
		str(configuration["Game"]["Width"])+
		"x"+
		str(configuration["Game"]["Height"])+
		"+"+
		str(int((team.winfo_screenwidth()/2)-configuration["Game"]["Width"]/2))+
		"+"+
		str(int((team.winfo_screenheight()/2)-configuration["Game"]["Height"]/2))
	)
	
	#Background de la ventana
	fondo_imagen = load_image(configuration["Files"]["images"]["gamebg"])
	fondo = Label(team,image=fondo_imagen)
	fondo.pack()

	####Crear menu button con checkbutton para seleccionar equipos#### 
	team_selection = Menubutton(team, activebackground="blue", text=configuration["Lang"][lang]["Botones"]["TEAM"], font=("Consolas",15), relief=RAISED)
	team_selection.menu = Menu(team_selection, tearoff=0, font=("Consolas",15), activebackground="blue")
	team_selection["menu"] = team_selection.menu

	for equipo in ListaEquipos.Equipos:
		team_selection.menu.add_checkbutton(label=equipo["Nombre"], font=("Consolas",12))

	#crear botones
	button_continue = Button(team,text=configuration["Lang"][lang]["Botones"]["Continue"],width=10,height=2,command=lambda:button_listener(12),bg="white",fg="black",font=("Consolas",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_continue.place(x=650,y=500)

	team_selection.place(x=50,y=50)

	team.mainloop()


def select_player(): #Seleccionar un jugador predeterminado o extra
	global window,select,jugadores,ListaJugadores
	#crear ventana
	select = Toplevel(window)
	select.title(configuration["Lang"][lang]["Labels"]["Create"])
	select.config(bg="black")
	select.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
	select.iconbitmap(configuration["Files"]["images"]["icon"])
	select.protocol("WM_DELETE_WINDOW",lambda:button_listener(15))
	select.geometry(											#Establece la geometría en la que siempre aparece la ventana
		str(configuration["Game"]["Width"])+
		"x"+
		str(configuration["Game"]["Height"])+
		"+"+
		str(int((select.winfo_screenwidth()/2)-configuration["Game"]["Width"]/2))+
		"+"+
		str(int((select.winfo_screenheight()/2)-configuration["Game"]["Height"]/2))
	)
	
	
	#Background de la ventana
	fondo_imagen = load_image(configuration["Files"]["images"]["gamebg"])
	fondo = Label(select,image=fondo_imagen)
	fondo.pack()

	####Crear menu button con checkbutton para seleccionar jugadores#### 
	selection = Menubutton(select, activebackground="blue", text=configuration["Lang"][lang]["Botones"]["select"], font=("Consolas",15), relief=RAISED)
	selection.menu = Menu(selection, tearoff=0, font=("Consolas",15), activebackground="blue")
	selection["menu"] = selection.menu

	for jugador in ListaJugadores.Jugadores:
		selection.menu.add_checkbutton(label=jugador["Nombre"], font=("Consolas",12))

	for jugador in jugadores_extra:
		selection.menu.add_checkbutton(label=jugador["Nombre"], font=("Consolas",12))

	#crear botones
	button_continue = Button(select,text=configuration["Lang"][lang]["Botones"]["Continue"],width=10,height=2,command=lambda:button_listener(13),bg="white",fg="black",font=("Consolas",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_continue.place(x=650,y=500)

	selection.place(x=50,y=50)

	select.mainloop()

def select_goalkeeper():
	global portero,lang,window
	#Crear ventana
	portero = Toplevel(window)
	portero.title(configuration["Lang"][lang]["Labels"]["SelectT"])
	portero.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])  #El tamaño de la ventana no puede ser cambiado
	portero.config(bg="black")
	portero.iconbitmap(configuration["Files"]["images"]["icon"])
	portero.protocol("WM_DELETE_WINDOW",lambda:button_listener(18))
	portero.geometry(											#Establece la geometría en la que siempre aparece la ventana
		str(configuration["Game"]["Width"])+
		"x"+
		str(configuration["Game"]["Height"])+
		"+"+
		str(int((portero.winfo_screenwidth()/2)-configuration["Game"]["Width"]/2))+
		"+"+
		str(int((portero.winfo_screenheight()/2)-configuration["Game"]["Height"]/2))
	)
	
	#Background de la ventana
	fondo_imagen = load_image(configuration["Files"]["images"]["gamebg"])
	fondo = Label(portero,image=fondo_imagen)
	fondo.pack()

	####Crear menu button con checkbutton para seleccionar portero#### 
	portero_selection = Menubutton(portero, activebackground="blue", text=configuration["Lang"][lang]["Botones"]["goalkeeper"], font=("Consolas",15), relief=RAISED)
	portero_selection.menu = Menu(portero_selection, tearoff=0, font=("Consolas",15), activebackground="blue")
	portero_selection["menu"] = portero_selection.menu

	#crear botones
	button_continue = Button(portero,text=configuration["Lang"][lang]["Botones"]["Continue"],width=10,height=2,command=lambda:button_listener(17),bg="white",fg="black",font=("Consolas",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_continue.place(x=650,y=500)

	portero_selection.place(x=50,y=50)

	portero.mainloop()


def select_arbitro():
	global arbitro,lang,window
	#Crear ventana
	arbitro = Toplevel(window)
	arbitro.title(configuration["Lang"][lang]["Labels"]["Create"])
	arbitro.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])  #El tamaño de la ventana no puede ser cambiado
	arbitro.config(bg="black")
	arbitro.iconbitmap(configuration["Files"]["images"]["icon"])
	arbitro.protocol("WM_DELETE_WINDOW",lambda:button_listener(19))
	arbitro.geometry(											#Establece la geometría en la que siempre aparece la ventana
		str(configuration["Game"]["Width"])+
		"x"+
		str(configuration["Game"]["Height"])+
		"+"+
		str(int((arbitro.winfo_screenwidth()/2)-configuration["Game"]["Width"]/2))+
		"+"+
		str(int((arbitro.winfo_screenheight()/2)-configuration["Game"]["Height"]/2))
	)
	
	#Background de la ventana
	fondo_imagen = load_image(configuration["Files"]["images"]["gamebg"])
	fondo = Label(arbitro,image=fondo_imagen)
	fondo.pack()

	####Crear menu button con checkbutton para seleccionar arbitro#### 
	arbitro_selection = Menubutton(arbitro, activebackground="blue", text=configuration["Lang"][lang]["Botones"]["referee"], font=("Consolas",15), relief=RAISED)
	arbitro_selection.menu = Menu(arbitro_selection, tearoff=0, font=("Consolas",15), activebackground="blue")
	arbitro_selection["menu"] = arbitro_selection.menu

	#crear botones
	button_continue = Button(arbitro,text=configuration["Lang"][lang]["Botones"]["Continue"],width=10,height=2,command=lambda:button_listener(20),bg="white",fg="black",font=("Consolas",12)) #Creación del botón para regresar a la ventana de inicio del juego
	button_continue.place(x=650,y=500)

	arbitro_selection.place(x=50,y=50)

	arbitro.mainloop()


def config_win():	#Ventana de configuración para añadir jugadores extra
	global window,configuration_window,lang
	#Crear ventana
	configuration_window = Toplevel(window)
	configuration_window.title(configuration["Lang"][lang]["Botones"]["configuration"])
	configuration_window.minsize(configuration["Game"]["Widthc"], configuration["Game"]["Heightc"])
	configuration_window.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])
	configuration_window.iconbitmap(configuration["Files"]["images"]["icon"])
	configuration_window.config(bg="black")
	configuration_window.protocol("WM_DELETE_WINDOW", lambda:button_listener(11))
	
	#creación de objetos
	titulo = Label(configuration_window, text=configuration["Lang"][lang]["Labels"]["new"],font=("Consolas",15),bg="black",fg="white").grid(row=0,column=0)
	
	variablenombre = StringVar()
	nombre = Entry(configuration_window,font=("Consolas",20),width=20,textvariable=variablenombre)
	nombre.grid(row=1,column=0)
	button_add = Button(configuration_window,width=15,bd=0,bg="black",fg="white",command=lambda:Add_Jugador(nombre.get()),text=configuration["Lang"][lang]["Botones"]["Add"],font=("Consolas",15)).grid(row=2,column=0)
	#button_addimage = Button(configuration_window,width=15,bd=0,bg="black",fg="white",command=lambda:button_listener(12),text=configuration["Lang"][lang]["Botones"]["addimage"],font=("Consolas",15)).grid(row=3,column=0)
	button_return = Button(configuration_window,width=15,bd=0,bg="black",fg="white",command=lambda:button_listener(11),text=configuration["Lang"][lang]["Botones"]["Return"],font=("Consolas",15)).grid(row=3,column=1)

	


def play():
	global game,lang,canvas,window
	#Crear ventana
	game = Toplevel(window)
	game.title(configuration["APP"]["Nombre_del_proyecto"])
	game.resizable(width=configuration["Game"]["resizable"]["Width"],height=configuration["Game"]["resizable"]["Height"])  #El tamaño de la ventana no puede ser cambiado
	game.config(bg="black")
	game.iconbitmap(configuration["Files"]["images"]["icon"])
	game.protocol("WM_DELETE_WINDOW",lambda:button_listener(14))
	game.geometry(											#Establece la geometría en la que siempre aparece la ventana
		str(configuration["Game"]["Width"])+
		"x"+
		str(configuration["Game"]["Height"])+
		"+"+
		str(int((game.winfo_screenwidth()/2)-configuration["Game"]["Width"]/2))+
		"+"+
		str(int((game.winfo_screenheight()/2)-configuration["Game"]["Height"]/2))
	)
	
	#background de la ventana
	fondo_imagen = load_image(configuration["Files"]["images"]["playbg"])
	fondo = Label(game,image=fondo_imagen)
	fondo.pack()
	

	game.mainloop()


#------Funciones que controlan el sonido del programa------#

#<Sonido para ventana principal>#
def music(): #Sonido para ventana principal
	if configuration["Game"]["sound"]:
		winsound.PlaySound(configuration["Files"]["sounds"]["inicio"],winsound.SND_ASYNC)

def play_music():
	if configuration["Game"]["sound"]:
		threads(1)

def stop_music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(None,0)

#<Sonido para ventanas de configuracion y selección>#
def game_music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(configuration["Files"]["sounds"]["game"],winsound.SND_ASYNC)

def play_game_music():
	if configuration["Game"]["sound"]:
		threads(2)

def stop_game_music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(None,0)

#<Sonido para comenzar el juego> (Mostrar equipos seleccionados antes de comenzar a jugar)#
def start_music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(configuration["Files"]["sounds"]["play"],winsound.SND_ASYNC)

def play_start_music():
	if configuration["Game"]["sound"]:
		threads(3)

def stop_start_music():
	if configuration["Game"]["sound"]:
		winsound.PlaySound(None,0)


lang_setup()
