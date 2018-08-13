def presión_hidro(P,d,g,h): #Se agrego :
    if P =='' and d !='' and g !='' and h!='':
        return 'La presion en Pascales es de:' + str(d*g*h)
    elif P !='' and d =='' and g !='' and h!='':
        return 'La densidad en Kg/m3 es de:' + str(P/(g*h))
    elif P !='' and d !='' and g =='' and h!='':
        return 'La gravedad en m/s2 es de:' + str(P/(d*h))
    elif P !='' and d !='' and g !='' and h=='':
        return 'La altura o profundidad en mts es de:' + str(P/(g*d))
    elif P !='' and d !='' and g !='' and h!='':
        return 'Debe existir una incognita'
    else:
        return 'Parámetros inválidos'

