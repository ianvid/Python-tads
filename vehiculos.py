def crearVehiculo():
    vehiculo=["","","","",""]
    return vehiculo
def cargarVehiculo(vehiculo,patente,ingreso,torre,egreso,pago):
    vehiculo[0]=patente
    vehiculo[1]=ingreso
    vehiculo[2]=torre
    vehiculo[3]=egreso
    vehiculo[4]=pago
def verPat(vehiculo):
    return vehiculo[0]
def verIng(vehiculo):
    return vehiculo[1]
def verTor(vehiculo):
    return vehiculo[2]
def verEgre(vehiculo):
    return vehiculo[3]
def verPago(vehiculo):
    return vehiculo[4]

def modPat(vehiculo,n):
    vehiculo[0]=n
def modIng(vehiculo,n):
    vehiculo[1]=n
def modTor(vehiculo,n):
    vehiculo[2]=n
def modEgre(vehiculo,n):
    vehiculo[3]=n
def modPago(vehiculo,n):
    vehiculo[4]=n

def copiar(a1,a2):
    for i in range (0,5):
        a2[i]=a1[i]
 
