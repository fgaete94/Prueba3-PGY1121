import funciones as fn
print("Bienvenidos al registro de ciudadanos de Andalucía")
while True:
    try:
        print("seleccione que desea realizar\n")
        print("1.- Grabar Ciudadano")
        print("2.- Buscar Ciudadano")
        print("3.- Imprimir Certificado")
        print("4.- Salir")
        
        opcion1=int(input())

        if opcion1==1:##menu para ingresar ciudadano
            print("ingrese NIF")
            print("por ejemplo: 99999999-RTX")
            nif=input().upper()
            print("ingrese Nombre: ")
            nombre=input().upper()
            print("ingrese edad: ")
            try:
                edad=int(input())
            except:
                print("Ingresa un Valor Valido \n") 
            fn.grabar(nif,nombre,edad) 
        elif opcion1==2:###menu para buscar ciudadanos
            print("ingrese NIF")
            nif=input().upper()
            try:
                fn.buscar(nif)
            except:
                print("El ciudadano no pertenece la Union Europea")
        elif opcion1==3:##menu para certificados
            print("ingrese NIF")
            nif=input().upper()
            while True:
                print("1.- Imprimir Certificado de Nacimiento")
                print("2.- Imprimir Certificado Conyugal")
                print("3.- Imprimir Certificado de Pertenencia a UE")
                opcion2=int(input())
                try:
                    if opcion2==1:
                        print("ingrese el nombre de ciudad de nacimiento:")
                        ciudad=input().upper()
                        print("ingrece pais de nacimiento: ")
                        pais=input().upper()
                        fn.nacimiento(nif,ciudad,pais)
                    elif opcion2==2:
                        print("Ingrese Esatado Conyugal del Ciudadano/a: ")
                        matrimonio=input().upper()
                        fn.conyugal(nif,matrimonio)
                    elif opcion2==3:
                        fn.pertenencia(nif)
                except:
                    print("Error el ciudadano no se encuentra en los registros")
                try:
                    print("¿Desea Ver Otro Certificado?:   S/N")
                    opcion3=input().upper()
                    if opcion3=="N":
                        break
                except:
                    print("Ingresa un Valor Valido \n") 
        elif opcion1==4:##menu para salir
            print("Gracias por usar el programa !")
            print("Felipe Gaete T, Version 1.0")
            break
        elif opcion1<1 or opcion1>4:
            print("Escoge una opcion entre 1 y 4\n")
    except:
        print("Ingresa un Valor Valido \n")
    