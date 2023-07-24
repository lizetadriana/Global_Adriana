listaNombres=[]
listaEdades=[]

def menu():
    opcion=1
    while(opcion!=0):
        print("1. Pedir Datos")
        print("2. Imprimir datos")
        print("3. Generar PDF")
        print("4. Generar QR")
        print("0. Salir")
        opcion=int(input("Elige una opcion "))
        if(opcion==1):
            pedirDatos()
        elif(opcion==2):
         imprimirDatos()


def pedirDatos():
    listaNombres.append(input("Ingresa un nombre"))
    listaEdades.append(input("Ingresa una edad "))
    print("Guardado")

def imprimirDatos():
    for i in range(len(listaNombres)):
        print(f"Nombre: {listaNombres[i]} Edad: {listaEdades[i]}")