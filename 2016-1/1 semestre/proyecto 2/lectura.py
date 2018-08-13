def leer_equipos(): 
    arch = open('players2.txt','r+')
    global equipo1 , equipo2, equipo3, equipo4
    equipo1 = []
    equipo2 = []
    equipo3 = []
    equipo4 = []
    a = arch.readline()
    while a != '':
        if a[2] == '1':
            equipo1.append([a[0:2],a[3:-1]])
            a = arch.readline()
        elif a[2] == '2':
            equipo2.append([a[0:2],a[3:-1]])
            a = arch.readline()
        elif a[2] == '3':
            equipo3.append([a[0:2],a[3:-1]])
            a = arch.readline()                                        
        elif a[2] == '4':
            equipo4.append([a[0:2],a[3:-1]])
            a = arch.readline()
        else:
            a = arch.readline()
    arch.close()
    print (equipo1)
    




def cambio_str(N):
    R = ''
    for a in range(len(N)):
        b = str(N[a])
        c = b[2:4] + b[8:-2] + '\n'
        R = R + c
    return R


            
        
