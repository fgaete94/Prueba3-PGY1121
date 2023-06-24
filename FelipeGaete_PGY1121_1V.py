import funciones as fn
print("Bienvenidos al registro de ciudadanos de Andalucia")

while True:
    print("seleccione que desea realizar\n")
    print("1.- Grabar Ciudadano")
    print("2.- Buscar Ciudadano")
    print("3.- Imprimir Certificado")
    print("4.- Salir")

    opcion1=int(input())

    if opcion1==1:
        print("ingrese NIF")
        print("por ejemplo: 99999999-RTX")
        nif=input().upper()
        print("ingrese Nombre")
        nombre=input().upper()
        print("ingrese edad")
        edad=int(input())
        fn.grabar(nif,nombre,edad) 
    elif opcion1==2:
        print("ingrese NIF")
        nif=input().upper()
        fn.buscar(nif)
    elif opcion1==3:
        print()
    elif opcion1==4:
        print("Gracias por usar el programa !")
        print("Felipe Gaete T, Version 1.0")
        break