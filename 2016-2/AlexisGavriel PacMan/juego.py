import pygame
import time
from random import choice as random_pos


global matriz, size ,capsulas, comida, puntos, temp , nivel
matriz = []
size = 20
capsulas = 0
comida = 0
puntos = 0
temp = 0
nivel = 1 

#funcion lee el archivo que contiene el mapa de juego (matriz)
#y lo guarda en una matriz
def lectura_scores():
    global scores
    scores = []
    fila  = []
    num = 0
    with open('scores.txt') as f:
        lines = f.readlines()
    for line in lines:
        if num == 0:
            fila += [line[:-1]]
            num = 1
        else:
            fila += [int (line[:-1])]
            num = 0
            scores += [fila]
            fila = []
    print (scores)

    f.close()

lectura_scores()

def lectura_matriz():
    global matriz
    fila = []
    matriz = []
    with open('m.txt') as f:
        lines = f.readlines()
    for num in lines:
        for char in num:
            if char != '\n':
                fila += [int(char)]
            else:
                matriz += [fila]
                fila = []
    f.close()
    return matriz



    
    
lectura_matriz()

def write_scores():
    global scores
    arch_scores = open ("scores.txt","r+")
    arch_scores.seek(0)
    arch_scores.truncate()

    scores_text = ''
    for fila in scores:
        for columna in fila:
            scores_text += str(columna) + '\n'
            
    arch_scores.write(scores_text)
    arch_scores.close()


#inicializar pygame
pygame.init()
display_width = len(matriz[0])*size
display_height = len(matriz)*size +size
gameDisplay = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption('Pac Man')
clock = pygame.time.Clock()

#funcion para mostrar texto
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()


#funcion que dibuja la matriz del juego
def creacion_matriz():
    global matriz, size

    for fila in range (len(matriz)):
        for columna in range (len(matriz[0])):
            if matriz[fila][columna] == 1:
                pygame.draw.rect(gameDisplay, (200,200,0),(columna*size+3, fila*size+3, size/2, size/2)  )        
            elif matriz[fila][columna] == 0:               
                pygame.draw.rect(gameDisplay, (0,0,0),(columna*size, fila*size, size, size))
            elif matriz[fila][columna] == 6:               
                pygame.draw.rect(gameDisplay, (150,0,0),(columna*size, fila*size, size, size))
            elif matriz[fila][columna] == 2:
                pygame.draw.rect(gameDisplay, (200,0,200),(columna*size+3, fila*size+3, size/2, size/2)  )   
            elif matriz[fila][columna] == 8:               
                pygame.draw.rect(gameDisplay, (0,0,150),(columna*size, fila*size, size, size))
            
            
            
#######################################################                
from pygame import mixer                 
from threading import Thread

def threads(id):
    if id == 1:
        music_thread = Thread(target=play_music,args=())
        music_thread.daemon = True		#Le indica que corra asincrónicamente
        music_thread.start()	


def play_music():
    global intro
    mixer.init()
    mixer.music.load('Pac.mp3')
    for x in range(3):
        mixer.music.play()
        time.sleep(5)
    mixer.music.stop()

def start_music(event):
    play_music()

def stop_music(event):
    mixer.music.stop()


#######################################################

#funcion que imprime los alrededores del jugador, se utiliza como debugger
#un cuadro alrededor del jugador
def print_around(jugador):
    
    y = jugador.posicion_x  #columna
    x = jugador.posicion_y     #fila
    print (         '__',y,x,'__ ')
    try:
        print (         matriz[x-1][y-1] ,'-',
                       matriz[x-1]   [y]   ,'-',
                       matriz[x-1] [y+1], '\n',
                       
                       matriz[x][y-1] ,'-',
                       matriz[x]   [y]   ,'-',
                       matriz[x] [y+1], '\n',
                       
                       matriz[x+1][y-1] ,'-',
                       matriz[x+1]   [y]   ,'-',
                       matriz[x+1] [y+1]
                       )
    except:
        None


#clases
###################################################################################
class Juego:
    def __init__(self):
        global scores
        self.numero_de_juego = 0
        self.matriz =  lectura_matriz()
        self.capsulas =  0
        self.comida =  0
        self.scores = scores
        
    def get_capsulas(self):
        return (self.capsulas)
    def get_comida(self):
        return (self.comida)
    def comida(self):
        self.comida -= 1
    def capsulas(self):
        self.capsulas -= 1
    

###########################################       
class PacMan:
    global matriz , puntos 
    
    def __init__(self):
        self.estado = False
        self.posicion_x = 1
        self.posicion_y = 1
        self.velocidad = 10

    def get_color(self):
        if self.estado:
            return (0,50,150)
        else:
            return (0,200,200)
    def get_velocidad(self):
        return self.velocidad
    def get_estado(self):
        return self.estado
    def cambio(self):
        self.estado = not self.estado
    
    def mov_izq(self):
        global puntos, temp, comida, capsulas
        if self.posicion_x > 0:
            if matriz[self.posicion_y][self.posicion_x -1] == 1 or matriz[self.posicion_y][self.posicion_x -1] == 7 or matriz[self.posicion_y][self.posicion_x -1] == 2:
                self.posicion_x -= 1
                if matriz[self.posicion_y][self.posicion_x] == 1:
                    matriz[self.posicion_y][self.posicion_x ] = 7
                    puntos += 1
                    comida += 1
                    
                elif matriz[self.posicion_y][self.posicion_x] == 2:
                    matriz[self.posicion_y][self.posicion_x ] = 7
                    self.estado = True
                    temp = 0
                    self.velocidad = 7
                    capsulas +=1
        elif self.posicion_x == 0 and self.posicion_y == 14:
            self.posicion_x = 27

    def mov_der(self):
        global puntos, temp, comida, capsulas
        if self.posicion_x < 27:
            if matriz[self.posicion_y][self.posicion_x +1] == 1 or matriz[self.posicion_y][self.posicion_x +1] == 7 or matriz[self.posicion_y][self.posicion_x +1] == 2:
                self.posicion_x += 1
                if matriz[self.posicion_y][self.posicion_x] == 1:
                    matriz[self.posicion_y][self.posicion_x ] = 7
                    puntos += 1
                    comida += 1
                    
                elif matriz[self.posicion_y][self.posicion_x] == 2:
                    matriz[self.posicion_y][self.posicion_x ] = 7
                    self.estado = True
                    temp = 0
                    self.velocidad = 7
                    capsulas +=1
        elif self.posicion_x == 27 and self.posicion_y == 14:
            self.posicion_x = 0

    def mov_arriba(self):
        global puntos, temp, comida, capsulas
        if self.posicion_y > 1:
            if matriz[self.posicion_y -1][self.posicion_x] == 1 or matriz[self.posicion_y -1][self.posicion_x] == 7 or matriz[self.posicion_y -1][self.posicion_x] == 2:
                self.posicion_y -= 1
                if matriz[self.posicion_y][self.posicion_x] == 1:
                    matriz[self.posicion_y][self.posicion_x ] = 7
                    puntos += 1
                    comida += 1
                    
                elif matriz[self.posicion_y][self.posicion_x] == 2:
                    matriz[self.posicion_y][self.posicion_x ] = 7
                    self.estado = True
                    temp = 0
                    self.velocidad = 7
                    capsulas +=1

    def mov_abajo(self):
        global puntos, temp, comida, capsulas
        if self.posicion_y < 28:
            if matriz[self.posicion_y +1][self.posicion_x] == 1 or matriz[self.posicion_y +1][self.posicion_x] == 7 or matriz[self.posicion_y +1][self.posicion_x] == 2:
                self.posicion_y += 1
                if matriz[self.posicion_y][self.posicion_x] == 1:
                    matriz[self.posicion_y][self.posicion_x ] = 7
                    puntos += 1
                    comida += 1
                    
                elif matriz[self.posicion_y][self.posicion_x] == 2:
                    matriz[self.posicion_y][self.posicion_x ] = 7
                    self.estado = True
                    temp = 0
                    self.velocidad = 7
                    capsulas +=1
        
#######################################
class Fantasma:
    global matriz
    def __init__(self, color):
        self.estado = 0
        self.posicion_x = 14
        self.posicion_y = 12
        self.velocidad = 10
        if color == "celeste":
            self.color = (0,200,200)
        elif color == "rojo":
            self.color = (255,0,0)
            self.velocidad = 15
        elif color == "rosado":
            self.color = (255,100,150)
        elif color == "naranja":
            self.color = (255,100,0)
        else:
            self.color = (200,0,200)
    def get_color(self):
        return self.color
    
    def get_velocidad(self):
        return self.velocidad
        
    def mov(self):
        random = random_pos([1,2,3,4])
        try:
            if random == 1:
                self.mov_izq()
            elif random == 2:
                self.mov_der()
            elif random == 3:
                self.mov_arriba()
            elif random == 4:
                self.mov_abajo()
        except:
            self.mov()


        
    def mov_izq(self):
        if self.posicion_x > 0:
            if matriz[self.posicion_y][self.posicion_x -1] == 1 or matriz[self.posicion_y][self.posicion_x -1] == 7 or matriz[self.posicion_y][self.posicion_x -1] == 2 or matriz[self.posicion_y][self.posicion_x -1] == 8:
                self.posicion_x -= 1
            else:
                self.mov()
    def mov_der(self):
        if self.posicion_x < 27:
            if matriz[self.posicion_y][self.posicion_x +1] == 1 or matriz[self.posicion_y][self.posicion_x +1] == 7 or matriz[self.posicion_y][self.posicion_x +1] == 2 or matriz[self.posicion_y][self.posicion_x -1] == 8:
                self.posicion_x += 1
            else:
                self.mov()
    def mov_arriba(self):
        if self.posicion_y > 1:
            if matriz[self.posicion_y -1][self.posicion_x] == 1 or matriz[self.posicion_y -1][self.posicion_x] == 7 or matriz[self.posicion_y -1][self.posicion_x] == 2 or matriz[self.posicion_y][self.posicion_x -1] == 8:
                self.posicion_y -= 1
            else:
                self.mov()
    def mov_abajo(self):
        if self.posicion_y < 28:
            if matriz[self.posicion_y +1][self.posicion_x] == 1 or matriz[self.posicion_y +1][self.posicion_x] == 7 or matriz[self.posicion_y +1][self.posicion_x] == 2 or matriz[self.posicion_y][self.posicion_x -1] == 8:
                self.posicion_y += 1
            else:
                self.mov()


##################################################################################
    
        
#ventana de inicio
def game_intro():
    global intro
    intro = True
    x = 0
    text_input = ''
    threads(1)
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos =(pygame.mouse.get_pos())
                if 130<mouse_pos[0]<190 and 300<mouse_pos[1]<360:                    
                    x = 1
                    intro = False
                elif 230<mouse_pos[0]<290 and 300<mouse_pos[1]<360:
                    x = 2
                    intro = False
                elif 360<mouse_pos[0]<420 and 300<mouse_pos[1]<360:
                    x = 3
                    intro = False
                
                    

            elif event.type == pygame.KEYDOWN:
                if event.unicode in "abcdefghijklmnñopqrstuvwxyz":
                    text_input += event.unicode
                if event.unicode == "\x08":
                    text_input = text_input[:-1]
                
              

        #dibuja en la pantalla        
        gameDisplay.fill((255,255,255))
        inicio_img = pygame.image.load('inicio.png')
        gameDisplay.blit(inicio_img,    (0, 0))
        

        
        largeText = pygame.font.Font('freesansbold.ttf',55)
        TextSurf, TextRect = text_objects("Pac Man", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        input_text, input_rec = text_objects(text_input, largeText)
        input_rec.center = ((display_width/2),(display_height/2))
        

        
        
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(input_text, input_rec)
        pygame.draw.rect(gameDisplay, (0,200,0),(130, 300, 60, 60))
        pygame.draw.rect(gameDisplay, (200,0,0),(230, 300, 60, 60))
        pygame.draw.rect(gameDisplay, (0,0,200),(360, 300, 60, 60))
        
        pygame.display.update()
        clock.tick(15)
        
    global scores
    scores[3][0] = text_input
    if x == 1:
        game_loop()
    elif x == 2:
        hall_of_fame()
    elif x == 3:
        ventana_ayuda()
    





############################################
def ventana_ayuda():

    ventana = True
    global scores
    nombres = scores[0][0] +" | "+ scores[1][0] +' | '+scores[2][0]
    numeros = str(scores[0][1])+' | ' + str(scores[1][1]) +' | '+ str(scores[2][1])
    
    while ventana:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos =(pygame.mouse.get_pos())
                if 0<mouse_pos[0]<160 and 0<mouse_pos[1]<160:                    
                    ventana = False

        


        gameDisplay.fill((255,255,255))
        ayuda_img = pygame.image.load('ayuda.png')
        gameDisplay.blit(ayuda_img,    (0, 0))
        
        largeText = pygame.font.Font('freesansbold.ttf',55)
        #text_nombres, nombres_rec = text_objects('Ayuda', largeText)
        #nombres_rec.center = ((display_width/2),(display_height/4))
        #gameDisplay.blit(text_nombres, nombres_rec)



        pygame.draw.rect(gameDisplay, (200,0,0),(0, 0, 60, 60))
        pygame.display.update()
        clock.tick(15)

    
    





    game_intro()
############################################
def hall_of_fame():

    hall = True
    global scores
    nombres = scores[0][0] +" | "+ scores[1][0] +' | '+scores[2][0]
    numeros = str(scores[0][1])+' | ' + str(scores[1][1]) +' | '+ str(scores[2][1])
    
    while hall:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos =(pygame.mouse.get_pos())
                if 200<mouse_pos[0]<320 and 0<mouse_pos[1]<60:                    
                    hall = False

        


        gameDisplay.fill((255,255,255))
        hall_img = pygame.image.load('hall.png')
        pygame.draw.rect(gameDisplay, (200,0,0),(220, 0, 120, 60))
        gameDisplay.blit(hall_img,    (0, 0))
        
        largeText = pygame.font.Font('freesansbold.ttf',25)
        text_nombres, nombres_rec = text_objects(nombres, largeText)
        nombres_rec.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(text_nombres, nombres_rec)

        text_numeros, numeros_rec = text_objects(numeros, largeText)
        numeros_rec.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(text_numeros, numeros_rec)



 


        
        pygame.display.update()
        clock.tick(15)

    
    





    game_intro()










#ventana de juego 
def game_loop():
    global matriz,size, capsulas, comida, puntos , nivel
    capsulas = 0
    comida = 0
    nivel = 0
    
    
    clock = pygame.time.Clock()
    contador = 0
    x = len(matriz)*size 
    y = len(matriz[0])*size +size
    
    
    jugador = PacMan()
    tablero = Juego()
    puntos = 0
    tablero.numero_de_juego +=1
    
    pacman_img = pygame.image.load('pacman.png')



    
    fantasma_celeste = Fantasma("celeste")
    fantasma_rojo = Fantasma("rojo")
    fantasma_rosado = Fantasma("rosado")
    fantasma_naranja = Fantasma("naranja")
    
    
    
 

 
    gameExit = False
    
    
    posx = jugador.posicion_x
    posy = jugador.posicion_y

    #loop para jugar
    while not gameExit:
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT: #cierra el programa si se cierra la ventana
                        done = True
                        pygame.quit()
                        quit()
                        
        #reconocimiento de las teclas de movimiento
        pressed = pygame.key.get_pressed()
        if contador % (jugador.get_velocidad()) == 0:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                jugador.mov_izq()
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                jugador.mov_der()
            if pressed[pygame.K_UP]or pressed[pygame.K_w]:
                jugador.mov_arriba()
            if pressed[pygame.K_DOWN]or pressed[pygame.K_s]:
                jugador.mov_abajo()
            #if pressed[pygame.K_SPACE]:
            #    print_around(jugador)
            #    tablero.mostrar()
            #if pressed[pygame.K_i]:
            #    fantasma_celeste.mov()
            #if pressed[pygame.K_j]:
            #    fantasma_rosado.mov()
            #if pressed[pygame.K_k]:
            #    fantasma_rojo.mov()
            #if pressed[pygame.K_l]:
            #    fantasma_naranja.mov()
            #if pressed[pygame.K_m]:
            #    jugador.cambio()
            
            
            

        #dibuja en la pantalla
        gameDisplay.fill((255,255,255))
        creacion_matriz()
        gameDisplay.blit(pacman_img,    (jugador.posicion_x*size , jugador.posicion_y*size))
        
        pygame.draw.rect(gameDisplay, fantasma_celeste.get_color() ,(fantasma_celeste.posicion_x*size, fantasma_celeste.posicion_y*size , size, size))
        pygame.draw.rect(gameDisplay, fantasma_rosado.get_color() ,(fantasma_rosado.posicion_x*size, fantasma_rosado.posicion_y*size , size, size))
        pygame.draw.rect(gameDisplay, fantasma_rojo.get_color() ,(fantasma_rojo.posicion_x*size, fantasma_rojo.posicion_y*size , size, size))
        pygame.draw.rect(gameDisplay, fantasma_naranja.get_color() ,(fantasma_naranja.posicion_x*size, fantasma_naranja.posicion_y*size , size, size))
        

####################
        global puntos

        if jugador.posicion_x == fantasma_rojo.posicion_x and jugador.posicion_y == fantasma_rojo.posicion_y:
            if not jugador.get_estado():
                gameExit =  True
            else:
                puntos += 15
                fantasma_rojo.posicion_x = 14
                fantasma_rojo.posicion_y = 12
        elif jugador.posicion_x == fantasma_celeste.posicion_x and jugador.posicion_y == fantasma_celeste.posicion_y:
            if not jugador.get_estado():
                gameExit =  True
            else:
                puntos += 10
                fantasma_celeste.posicion_x = 14
                fantasma_celeste.posicion_y = 12
            
        elif jugador.posicion_x == fantasma_rosado.posicion_x and jugador.posicion_y == fantasma_rosado.posicion_y:
            if not jugador.get_estado():
                gameExit =  True
            else:
                puntos += 10
                fantasma_rosado.posicion_x = 14
                fantasma_rosado.posicion_y = 12
        elif jugador.posicion_x == fantasma_naranja.posicion_x and jugador.posicion_y == fantasma_naranja.posicion_y:
            if not jugador.get_estado():
                gameExit =  True
            else:
                puntos += 10
                fantasma_naranja.posicion_x = 14
                fantasma_naranja.posicion_y = 12
        else:
            gameExit =  False

################################################        
        
        pygame.display.update()
        
        if contador% (fantasma_rosado.get_velocidad()) == 0:
            fantasma_celeste.mov()
            fantasma_rosado.mov()
            fantasma_naranja.mov()
            
        if contador% (fantasma_rojo.get_velocidad()) == 0:
            fantasma_rojo.mov()

        if contador % 100 == 0:
            if jugador.estado:
                global temp
                temp += 1
                if temp == 5:
                    temp = 0
                    jugador.estado = False
                    jugador.velocidad = 10

            if capsulas == 4  and comida == 238  :
                print ("win")
                clock.tick(5)
                matriz = lectura_matriz()
                fantasma_celeste.velocidad += 2*nivel
                fantasma_rosado.velocidad += 2*nivel
                fantasma_naranja.velocidad += 2*nivel
                fantasma_rojo.velocidad += 2*nivel

                fantasma_celeste.posicion_x = 14
                fantasma_celeste.posicion_y = 12
                fantasma_rosado.posicion_x  = 14
                fantasma_rosado.posicion_y  = 12
                fantasma_naranja.posicion_x = 14
                fantasma_naranja.posicion_y = 12
                fantasma_rojo.posicion_x    = 14
                fantasma_rojo.posicion_y    = 12

                jugador.posicion_x = 1
                jugador.posicion_y = 1
                capsulas = 0
                comida = 0
                nivel += 1



                
            print (puntos, comida, capsulas, jugador.get_estado(), tablero.numero_de_juego)
            
        contador +=1
        clock.tick(100)




    
    global scores
    print ("Fin")
    print (puntos, comida, capsulas)
    scores[3][1] = puntos
    scores = sorted(scores, key=lambda scores: scores[1])
    scores = [scores[3],scores[2],scores[1],['',0]]
    
    write_scores()



    
    game_intro()







#game_loop()
game_intro()

