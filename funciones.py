import numpy as np
import random as rd

ciudadanos={}

def crearNIF():
    num="0123456789"
    letras="ABDCEFGHIJKLMNOPQRSTUVWXYZ"
    g="-"
    long=8
    long2=1
    long3=3
    unir=rd.sample(num,long)+rd.sample(g,long2)+rd.sample(letras,long3)
    NIF="".join(unir)
    return NIF

def grabar(nif,nombre,edad):
    longnom=len(nombre)
    if longnom<8:
        print("el nombre ingresado no cumple con longitud.")
        return
    if edad<0:
        print("la edad ingresada no es valida.")
    if edad>=0 and longnom>=8: ##si se cumple esto, se graba al ciudadano/a en el diccionario
        ciudadanos[nif]=nombre,edad
        print("Registro Exitoso\n")
        return

def buscar(nif): ## KeyError
    if nif== KeyError:##si la llave no existe no encuentra al ciudadano/a
        print("El ciudadano/a no pertenece la Union Europea")
        return
    else:
        print("El ciudadano/a de nombre: ",ciudadanos[nif][0])
        print("Edad: ", ciudadanos[nif][1])
        print("Si pertenece a la Union Europea")
        return

def nacimiento(nif,ciudad,pais):
    if nif== KeyError:##si la llave no existe no encuentra al ciudadano
        print("El ciudadano/a no se encuentra en la base de datos")
        return
    else:
        print("----- Estado de Andalucía -----")
        print("El gobierno Español certifica que: ")
        print("Sr/a: ",ciudadanos[nif][0])
        print("Edad: ",ciudadanos[nif][1])
        print("Nacido en la ciudad de:",ciudad,"de: ",pais)
        print("Es Ciudadano Nacido en Union Europea\n")
        return

def conyugal(nif,matrimonio):
    if nif== KeyError:##si la llave no existe no encuentra al ciudadano/a
        print("El ciudadano/a no se encuentra en la base de datos")
        return
    else:
        print("----- Estado de Andalucía -----")
        print("El gobierno Español certifica que: ")
        print("Sr/a: ",ciudadanos[nif][0])
        print("Edad: ",ciudadanos[nif][1])
        print("Ciudadano de la Union Europea")
        print("Se encuentra en la condicion de: ",matrimonio)
        return
def pertenencia(nif):
    if nif== KeyError:##si la llave no existe no encuentra al ciudadano/a
        print("El ciudadano/a no se encuentra en la base de datos")
        return
    else:
        print("----- Estado de Andalucía -----")
        print("El gobierno Español certifica que: ")
        print("Sr/a: ",ciudadanos[nif][0])
        print(" Es Ciudadano/a de la Union Europea") 
        return