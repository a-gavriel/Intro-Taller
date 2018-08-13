def crear(X):
    with open('players.txt','r+') as arch:
        last = None
        for line in (line for line in arch if line.rstrip('\n')):
            last = line
        ultimalinea = last
        ultimonum = ultimalinea[0:2]
        print (ultimonum)
