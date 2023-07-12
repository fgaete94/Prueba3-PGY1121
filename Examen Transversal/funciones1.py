import numpy as np

deptos=np.array([[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],
                 [" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]])

piso1=deptos[0].astype(str)
piso2=deptos[1].astype(str)
piso3=deptos[2].astype(str)
piso4=deptos[3].astype(str)
piso5=deptos[4].astype(str)
piso6=deptos[5].astype(str)
piso7=deptos[6].astype(str)
piso8=deptos[7].astype(str)
piso9=deptos[8].astype(str)
piso10=deptos[9].astype(str)

registro={}
clientes=[]
modelos={'A':1,'B':2,'C':3,'D':4,}
modeloA=[]
modeloB=[]
modeloC=[]
modeloD=[]
acuA=0
acuB=0
acuC=0
acuD=0


def salir():
    print("Gracias por Usar el Programa, Felipe Gaete 1/07/2023")

def reservadepto(piso,tipo):
    if piso==1:
        if tipo=="A":
            piso1[0]="X"
        elif tipo=="B":
            piso1[1]="X"
        elif tipo=="C":
            piso1[2]="X"
        elif tipo=="D":
            piso1[3]="X"
    elif piso==2:
        if tipo=="A":
            piso2[0]="X"
        elif tipo=="B":
            piso2[1]="X"
        elif tipo=="C":
            piso2[2]="X"
        elif tipo=="D":
            piso2[3]="X"
    elif piso==3:
        if tipo=="A":
            piso3[0]="X"
        elif tipo=="B":
            piso3[1]="X"
        elif tipo=="C":
            piso3[2]="X"
        elif tipo=="D":
            piso3[3]="X"
    elif piso==4:
        if tipo=="A":
            piso4[0]="X"
        elif tipo=="B":
            piso4[1]="X"
        elif tipo=="C":
            piso4[2]="X"
        elif tipo=="D":
            piso4[3]="X"
    elif piso==5:
        if tipo=="A":
            piso5[0]="X"
        elif tipo=="B":
            piso5[1]="X"
        elif tipo=="C":
            piso5[2]="X"
        elif tipo=="D":
            piso5[3]="X"
    elif piso==6:
        if tipo=="A":
            piso6[0]="X"
        elif tipo=="B":
            piso6[1]="X"
        elif tipo=="C":
            piso6[2]="X"
        elif tipo=="D":
            piso6[3]="X"
    elif piso==7:
        if tipo=="A":
            piso7[0]="X"
        elif tipo=="B":
            piso7[1]="X"
        elif tipo=="C":
            piso7[2]="X"
        elif tipo=="D":
            piso7[3]="X"
    elif piso==8:
        if tipo=="A":
            piso8[0]="X"
        elif tipo=="B":
            piso8[1]="X"
        elif tipo=="C":
            piso8[2]="X"
        elif tipo=="D":
            piso8[3]="X"
    elif piso==9:
        if tipo=="A":
            piso9[0]="X"
        elif tipo=="B":
            piso9[1]="X"
        elif tipo=="C":
            piso9[2]="X"
        elif tipo=="D":
            piso9[3]="X"
    elif piso==10:
        if tipo=="A":
            piso10[0]="X"
        elif tipo=="B":
            piso10[1]="X"
        elif tipo=="C":
            piso10[2]="X"
        elif tipo=="D":
            piso10[3]="X"

def preciodepa(tipo):
    if tipo=="A":
        print("\nEl Departamento Tiene un valor de 3.800 UF")
    elif tipo=="B":
        print("\nEl Departamento Tiene un valor de 3.000 UF")
    elif tipo=="C":
        print("\nEl Departamento Tiene un valor de 2.800 UF")
    elif tipo=="D":
        print("\nEl Departamento Tiene un valor de 3.500 UF")

def comprar():
    print("Ingrese su Run (sin puntos ni digito verificador): ")
    run=int(input())
    print("Departamentos Disponibles: ")
    print("            TIPO")
    print("Piso | A | B | C | D |")
    print("10  ",piso10)
    print("9   ",piso9)
    print("8   ",piso8)
    print("7   ",piso7)
    print("6   ",piso6)
    print("5   ",piso5)
    print("4   ",piso4)
    print("3   ",piso3)
    print("2   ",piso2)
    print("1   ",piso1)
    print("\nSeleccione un piso:")
    piso=int(input())
    if piso<1 or piso>10:
        print("El piso seleccionado NO Existe")
    else:
        print("\nSeleccione un tipo:")
        tipo=input().upper()
        if tipo in modelos:
            departamento=piso,tipo
            if departamento in registro:
                print("\nEl Departaento no puede ser selecionado")
            else:
                preciodepa(tipo)
                registro[departamento]=run
                unir=(run,departamento)
                clientes.append(unir)
                reservadepto(piso,tipo)
                print("\nLa compra de su departamento se ha realizado")
                if tipo=="A":
                    modeloA.append(tipo)
                elif tipo=="B":
                    modeloB.append(tipo)    
                elif tipo=="C":
                    modeloC.append(tipo)    
                elif tipo=="D":
                    modeloD.append(tipo)    

        else:
            print("\nEl Modelo Seleccionado No Existe")

    
def mostrarDptos():
    print("Departamentos Disponibles: ")
    print("            TIPO")
    print("Piso | A | B | C | D |")
    print("10  ",piso10)
    print("9   ",piso9)
    print("8   ",piso8)
    print("7   ",piso7)
    print("6   ",piso6)
    print("5   ",piso5)
    print("4   ",piso4)
    print("3   ",piso3)
    print("2   ",piso2)
    print("1   ",piso1)
    return

def compradores():
    clientes.sort()
    return print(clientes)

def total_ventas():
    acuA=len(modeloA)*3800
    acuB=len(modeloB)*3000
    acuC=len(modeloC)*2800
    acuD=len(modeloD)*3500
    print (f"Del Modelo A de 3.800 UF se vendieron {len(modeloA)} Unidades, acumulando un total de: {acuA} UF")
    print (f"Del Modelo B de 3.000 UF se vendieron {len(modeloB)} Unidades, acumulando un total de: {acuB} UF")
    print (f"Del Modelo C de 2.800 UF se vendieron {len(modeloC)} Unidades, acumulando un total de: {acuC} UF")
    print (f"Del Modelo D de 3.500 UF se vendieron {len(modeloD)} Unidades, acumulando un total de: {acuD} UF")

