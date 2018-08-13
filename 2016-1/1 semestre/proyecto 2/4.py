import random

def ghost(): 
    global g1, g2, g3, g4, g5, g6
    g1 = False
    g2 = False
    g3 = False
    g4 = False
    g5 = False
    g6 = False
    port = random.choice([1, 2, 3, 4])
    if port == 1:
        a = random.choice([1,2,3,4,5,6])
        if a == 1:
            g1 = True
        elif a == 2:
            g2 = True
        elif a == 3:
            g3 = True
        elif a == 4:
            g4 = True
        elif a == 5:
            g5 = True
        elif a == 6:
            g6 = True
    elif port == 2:
        a = random.choice([1,2,3]) 
        if a == 1:
            g1 = True
            g2 = True
        elif a == 2:
            g3 = True
            g4 = True
        elif a == 3:
            g5 = True
            g6 = True
    elif port == 3:
        a = random.choice([1,2])
        if a == 1:
            g1 = True
            g2 = True
            g3 = True
        elif a == 2:
            g4 = True
            g5 = True
            g6 = True
    elif port == 4:
        a = random.choice([1,2])
        if a == 1:
            g1 = True
            g3 = True
            g5 = True
        elif a == 2:
            g2 = True
            g4 = True
            g6 = True
        
    print ('g=',g1,g2,g3,g4,g5,g6)
