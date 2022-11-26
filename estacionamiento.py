
def crearEstacionamiento():
    estacionamiento=[]
    return estacionamiento

def agregarVehiculo(estacionamiento, vehiculo):
    estacionamiento.append(vehiculo)

def eliminarVehiculo(estacionamiento, vehiculo):
    estacionamiento.remove(vehiculo)

def recuperarVehiculo(estacionamiento,i):
    return estacionamiento[i-1]

def tamanio(estacionamiento):
    return len(estacionamiento)


