
def lectura_scores():
	global scores
	scores  = []
	arch = open('scores.txt','r+')
	a = arch.readline()
    while a != '':
		scores.append([int(a[2:5]),int(a[5:8])])
        a = arch.readline()
	arch.close()	
	