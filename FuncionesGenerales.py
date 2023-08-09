from FuncionPDF import *
from DatosEstaticos import *
from nivelUrgencia import *
from Urgencia import *
from PacientePDF import *


listaNombre = []
listaSexo = []
listaDomi = []
listaTelefono = []
listaSangre = []
listaCURP = []
listaFecha = []
listaNSS = []
nombre=[]
edad=[]
nivel_urgencia=[]

def menu():
    opcion = 1
    while opcion != 0:
        print("1. Dar de alta.")
        print("2. Ingresar documentación")
        print("3. Imprimir Pacientes.")
        print("4. PDF de todos los pacientes.")
        print("5. Expediente de cada paciente.")
        print("6. Especialidades.")
        print("7. Nivel de urgencias.")
        print("8. Urgencia.")
        print("9. Imprimir pacientes en urgencias.")
        print("10. .")
        print("0. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            pedirDatos()
        elif opcion == 2:
            documentacion()
        elif opcion == 3:
            imprimirInformacionPaciente()
        elif opcion == 4:
            generarPDF(listaNombre, listaSexo, listaDomi, listaTelefono)
        elif opcion == 5:
            generarPDFPacienteIndividual()
        elif opcion == 6:
            tipoUrgencia()
        elif opcion == 7:
            nivelUrgencia()
        elif opcion == 8:
            tipoUrgencia()
        elif opcion == 9:
            imprimirPacientesEnUrgencias()
        elif opcion==10:
            imprimirPacientesEnUrgencias()

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

def imprimirInformacionPaciente():
    print("Pacientes disponibles:")
    for i in range(len(listaNombre)):
        print(f"{i + 1}. {listaNombre[i]}")

    if not listaNombre:
        print("No hay pacientes dados de alta.")
        return

    while True:
        try:
            opcion = int(input("Ingresa el número del paciente para ver su información (0 para salir): "))
            if opcion == 0:
                break
            elif 1 <= opcion <= len(listaNombre):
                paciente_index = opcion - 1
                print("Información del paciente:")
                print(f"Nombre: {listaNombre[paciente_index]} Sexo: {listaSexo[paciente_index]} Domicilio: {listaDomi[paciente_index]} Telefono: {listaTelefono[paciente_index]}")
                print(f"CURP: {listaCURP[paciente_index]} Fecha de nacimiento: {listaFecha[paciente_index]} NSS: {listaNSS[paciente_index]} Tipo de sangre: {listaSangre[paciente_index]}")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")

def generarPDFPacienteIndividual():
    print("Pacientes disponibles:")
    for i in range(len(listaNombre)):
        print(f"{i + 1}. {listaNombre[i]}")

    if not listaNombre:
        print("No hay pacientes dados de alta.")
        return

    while True:
        try:
            opcion = int(input("Ingresa el número del paciente para generar su PDF individual (0 para salir): "))
            if opcion == 0:
                break
            elif 1 <= opcion <= len(listaNombre):
                paciente_index = opcion - 1
                nombrePaciente = listaNombre[paciente_index]
                sexoPaciente = listaSexo[paciente_index]
                domiPaciente = listaDomi[paciente_index]
                telefonoPaciente = listaTelefono[paciente_index]
                curpPaciente = listaCURP[paciente_index]
                fechaPaciente = listaFecha[paciente_index]
                nssPaciente = listaNSS[paciente_index]
                sangrePaciente = listaSangre[paciente_index]

                generarPDFIndividual(nombrePaciente, sexoPaciente, domiPaciente, telefonoPaciente, curpPaciente, fechaPaciente, nssPaciente, sangrePaciente)
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")

def imprimirPacientesEnUrgencias():
    if not nombre:
        print("No hay pacientes en urgencias.")
        return

    print("Pacientes en urgencias:")
    for i in range(len(nombre)):
        print(f"{i + 1}. Nombre: {nombre[i]} Edad: {edad[i]} Número de Seguro Social: {seguro[i]} Nivel de urgencia: {nivel_urgencia[i]}")

    while True:
        try:
            opcion = int(input("Ingresa el número del paciente para ver su información detallada (0 para salir): "))
            if opcion == 0:
                break
            elif 1 <= opcion <= len(nombre):
                paciente_index = opcion - 1
                print("Información detallada del paciente en urgencias:")
                print(f"Nombre: {nombre[paciente_index]} Edad: {edad[paciente_index]} Número de Seguro Social: {seguro[paciente_index]} Nivel de urgencia: {nivel_urgencia[paciente_index]}")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")