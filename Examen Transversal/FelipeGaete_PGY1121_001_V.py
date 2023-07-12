import funciones1 as fn

print("Bienvenido/a Inmobiliaria Casa Feliz ")

while True:
    print("\n1.-Comprar departamento")
    print("2.-Mostrar departamentos disponibles")
    print("3.-Ver Listado de Compradores")
    print("4.-Mostar Ganancias Totales")
    print("5.-Salir")

    try:
        opcion1=int(input())

        if opcion1==1:
            fn.comprar() 
        elif opcion1==2:
            fn.mostrarDptos()
        elif opcion1==3:
            fn.compradores()
        elif opcion1==4:
            fn.total_ventas()
        elif opcion1<1 or opcion1>6:
            print("\n Selecciona una opcion valida.")
        elif opcion1==5:
            fn.salir()
            break
    except:
      print("\n Ingresa una opcion valida.")