






def val_v(vector):
    if len (vector) == 5:
        r = 0
        for a in vector:
            r += a
        if r == 1:
            return True
        else:
            return 'Error, vector debe sumar 1'
    else:
        return 'Error, vector debe tener 5 numeros'


def suma(vect,mat):
        vect = [''] + vect
        v = []
        r = []
        for a in range(len(mat)):
            for b in range(len(mat[0])):
                if isinstance (mat[a][b],int) or isinstance (mat[a][b],float):
                    res = round (mat[a][b] * vect[b] , 3)
                    v.append (res)
                else:
                    v.append (mat[a][b])
            v.append (v[1] +v[2] +v[3] +v[4] +v[5])
            r.append (v)
            v = []
        return r


