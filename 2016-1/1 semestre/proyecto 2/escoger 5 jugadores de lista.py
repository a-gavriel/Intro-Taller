
def random_players(equipocompleto):
    # cambiar valor de a por el equipo completo
    a = [1,2,3,4,5,6,7]
    equipo5 = []
    cont = 0
    while cont <5:
        cont += 1
        b = random.choice(a)
        a.remove(b)
        equipo5.append(b)
        print(b)
    print (equipo5)
