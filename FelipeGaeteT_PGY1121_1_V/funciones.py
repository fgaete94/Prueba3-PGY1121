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
    if edad>=0 and longnom>=8 and longnif>0 and longnif==12: ##si se cumple esto, se graba al ciudadano/a en el diccionario
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
