def crearCola():
    cola=[]
    return cola

def esVacia(cola):
    if len(cola)!=0:
        return False
    else:
        return True

def encolar(cola,elem):
    cola.append(elem)

def desencolar(cola):
    elem=cola.pop(0)
    return elem

def tamanio(cola):
    return len(cola)

def copiarCola(c1,c2):
    aux=crearCola()
    while not esVacia(c2):
        elem=desencolar(c1)
        encolar(aux,elem)
    while not esVacia(aux):
        elem=desencolar(aux)
        encolar(c1,elem)
        encolar(c2,elem)