from vehiculos import *
from estacionamiento import *
from cola import *
from datetime import datetime, time

vehiculosHoraPico = 0
op=-1

valorestadia = float(input("¡Bienvenido!, ingrese el valor de la estadia: "))

estac=crearEstacionamiento()



while (op != 0):
    print("1. ingresar vehiculo\n2. modificar vehiculo\n3. registrar salida del vehiculo\n4. ver vehiculos\n5. ver monto recaudado por cada torre\n6. ver vehiculos que ingresaron en hora pico\n7. Eliminar los vehículos que ingresaron luego de las 18 hs a una torre determinada\n8.generar una cola con los vehiculos en una torre determinada\n0. salir")
    op = int(input("Su opcion: "))

    if (op == 1):
        vehiculo=crearVehiculo()
        pat=input("Ingrese la patente del coche: ")
        ing=datetime.now().time().hour
        torre=int(input("Ingrese la torre:"))
        cargarVehiculo(vehiculo,pat,ing,torre,0,0)
        agregarVehiculo(estac,vehiculo)

    if(op == 2):
        patente=input("Ingrese la patente del vehiculo: ")
        l=tamanio(estac)
        for i in range(1,l+1):
            v=recuperarVehiculo(estac,i)
            p=verPat(v)
            if p==patente:
                print("Patente encontrada")
                quedato = int(input("¿Que dato del vehiculo desea modificar?\n1. patente\n2. hora ingreso\n3. torre: "))
                if quedato==1:
                    modPat(v,input("Ingrese la nueva patente: "))
                if quedato==2:
                    modIng(v,int(input("Ingrese la nueva hora")))
                if quedato==3:
                    modTor(v,int(input("Ingrese la nueva torre")))
                break
        
    if(op==3):
        patente=input("Ingrese la patente del vehiculo: ")
        l=tamanio(estac)
        for i in range(1,l+1):
            v=recuperarVehiculo(estac,i)
            p=verPat(v)
            if (p==patente and verEgre(v)==0):
                i=verIng(v)
                modEgre(v,datetime.now().time().hour)
                e=verEgre(v)
                t=i-e
                modPago(v,t*valorestadia)
                if verTor(v)==3:
                    p=verPago(v)
                    modPago(v,p-p*0.15)
                print("El vehiculo ha salido.")
                break
    if(op == 4):
        l=tamanio(estac)
        for i in range(1,l+1):
            v=recuperarVehiculo(estac,i)
            print(f"Patente: {verPat(v)}")
            print(f"Hora de ingreso: {verIng(v)}")
            print(f"Torre: {verTor(v)}")
            if verEgre(v)!=0:
                print(f"Hora de egreso: {verEgre(v)}")
                print(f"Importe: {verPago(v)}")
        print("No hay mas vehiculos")
    if(op==5):
        torre1 = 0
        torre2 = 0
        torre3 = 0
        l=tamanio(estac)
        for i in range(1,l+1):
            v=recuperarVehiculo(estac,i)
            p = verPago(v)
            if(p > 0):
                if(verTor(v)==1):
                    torre1 += p
                if (verTor(v) == 2):
                    torre2 += p
                if (verTor(v) == 3):
                    torre3 += p
        print(f"torre1: {torre1}\ntorre2: {torre2}\ntorre 3: {torre3}")
        break
    if(op==6):
        l=tamanio(estac)
        for i in range(1,l+1):
            v=recuperarVehiculo(estac,i)
            if(verEgre(v)==0):
                if(7<verIng(v)<10 or 17<verIng(v)<20):
                    vehiculosHoraPico += 1
        print(f"cantidad de vehiculos ingresados en hora pico: {vehiculosHoraPico}")
        break
# Eliminar los vehículos que ingresaron luego de las 18 hs a una torre determinada
    if(op==7):
        torre = input("que torre?: ")
        l=tamanio(estac)
        for i in range(1,l+1):
            v=recuperarVehiculo(estac,i)
            if(torre == verTor(v)):
                if(verIng(v)>18):
                    eliminarVehiculo(estac,v)
        print("terminado")
        break
    if (op==8):
        cola = crearCola()
        torre = input("que torre?: ")
        l=tamanio(estac)
        for i in range(1,l+1):
            v=recuperarVehiculo(estac,i)
            if(torre == verTor(v)):
                encolar(cola,v)
        print("terminado")
        break


print("Fin del programa.")
print("Desarrollado por: Ian Vidmar, Maximo Preneste y Rodrigo Rial.")