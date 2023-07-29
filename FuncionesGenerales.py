from FuncionPDF import *
from DatosEstaticos import *
from nivelUrgencia import *
from Urgencia import *

listaNombre = []
listaSexo = []
listaDomi = []
listaTelefono = []
listaSangre = []
listaCURP = []
listaFecha = []
listaNSS = []

def menu():
    opcion = 1
    while opcion != 0:
        print("1. Dar de alta.")
        print("2. Ingresar documentación")
        print("3. Expediente.")
        print("4. Especialidades.")
        print("5. Nivel de urgencia.")
        print("6. Tipo de urgencia.")
        print("7. Generar PDF")
        print("8. Generar QR")
        print("9. Imprimir datos personales.")
        print("10. Imprimir documentación.")
        print("0. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            pedirDatos()
        elif opcion == 2:
            documentacion()
        elif opcion == 3:
            generarPDF(listaNombre, listaSexo)
        elif opcion == 4:
            nivelUrgencia()
        elif opcion == 5:
            listarEspecialidades()
        elif opcion == 6:
            tipoUrgencia()
        elif opcion == 9:
            imprimirDatosPersonales()
        elif opcion == 10:
            imprimirDocumentacion()

def pedirDatos():
    listaNombre.append(input("Ingresa el nombre del paciente: "))
    listaSexo.append(input("Ingresa el sexo del paciente: "))
    listaDomi.append(input("Ingresa el domicilio del paciente: "))
    listaTelefono.append(input("Ingresa el telefono del paciente: "))
    print("----------------Guardado---------------")

def documentacion():
    listaCURP.append(input("Ingresa el CURP del paciente: "))
    listaFecha.append(input("Ingrese la fecha de nacimiento del paciente: "))
    listaNSS.append(input("Ingrese el NSS del paciente: "))
    listaSangre.append(input("Ingrese el tipo de sangre del paciente: "))
    print("----------------Guardado---------------")

def imprimirDatosPersonales():
    for i in range(len(listaNombre)):
        print(f"Nombre: {listaNombre[i]} Sexo: {listaSexo[i]} Domicilio: {listaDomi[i]} Telefono: {listaTelefono[i]}")

def imprimirDocumentacion():
    for i in range(len(listaCURP)):
        print(f"CURP: {listaCURP[i]} Fecha de nacimiento: {listaFecha[i]} NSS: {listaNSS[i]} Tipo de sangre: {listaSangre[i]}")
