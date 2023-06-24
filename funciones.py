import numpy as np

ciudadanos={}


def grabar(nif,nombre,edad):
    longnif=len(nif)
    if longnif<0 or longnif<12 or longnif>12:
        print("el nif ingresado no cumple con los requisitos.")
        return
    longnom=len(nombre)
    if longnom<8:
        print("el nombre ingresado no cumple con longitud.")
        return
    if edad<0:
        print("la edad ingresada no es valida.")
    if edad>=0 and longnom>=8 and longnif>0 and longnif==12:
        ciudadanos[nif]=nombre,edad
        print("Registro Exitoso")
        return

def buscar(nif): ## KeyError
    if nif== KeyError:
        print("El ciudadano no pertenece la Union Europea")
        return
    else:
        print("El ciudadano de nombre: ",ciudadanos[nif][0])
        print("Edad: ", ciudadanos[nif][1])
        print("Si pertenece a la Union Europea")
        return

