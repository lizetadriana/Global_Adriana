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
atendido_en_urgencias = [False] * len(nombre)


def menu():
    opcion = 1
    while opcion != 0:
        print("1. Dar de alta.")
        print("2. Ingresar documentación")
        print("3. Imprimir Pacientes.")
        print("4. Expediente de cada paciente.")
        print("5. Especialidades.")
        print("6. Nivel de urgencias.")
        print("7. Urgencia.")
        print("8. Imprimir pacientes en urgencias.")
        print("9. Doctores.")
        print("10. Enfermeras.")
        print("0. Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            pedirDatos()
        elif opcion == 2:
            documentacion()
        elif opcion == 3:
            imprimirInformacionPaciente()
        elif opcion == 4:
            generarPDFPacienteIndividual()
        elif opcion == 5:
            tipoUrgencia()
        elif opcion == 6:
            nivelUrgencia()
        elif opcion == 7:
            tipoUrgencia()
        elif opcion == 8:
            imprimirPacientesEnUrgencias()
        elif opcion == 9:
            mostrarDoctores()
        elif opcion == 10:
            mostrarEnfermeras()
        
            

def pedirDatos():
    listaNombre.append(input("Ingresa el nombre del paciente: "))
    listaSexo.append(input("Ingresa el sexo del paciente: "))
    listaDomi.append(input("Ingresa el domicilio del paciente: "))
    listaTelefono.append(input("Ingresa el telefono del paciente: "))
    print("----------------Guardado---------------")


def mostrarPacientesRegistrados():
    if not listaNombre:
        print("No hay pacientes registrados.")
    else:
        print("Pacientes registrados:")
        for i, nombre in enumerate(listaNombre):
            print(f"{i + 1}. {nombre}")

def documentacion():
    mostrarPacientesRegistrados()

    if not listaNombre:
        return

    seleccion = int(input("Seleccione el número del paciente para ingresar documentación: ")) - 1

    if seleccion < 0 or seleccion >= len(listaNombre):
        print("Selección inválida.")
        return

    while seleccion >= len(listaCURP):
        listaCURP.append("                                                 ")
        listaFecha.append("                                                ")
        listaNSS.append("                                                  ")
        listaSangre.append("                                               ")

    listaCURP[seleccion] = input("Ingresa el CURP del paciente: ")
    listaFecha[seleccion] = input("Ingrese la fecha de nacimiento del paciente: ")
    listaNSS[seleccion] = input("Ingrese el NSS del paciente: ")
    listaSangre[seleccion] = input("Ingrese el tipo de sangre del paciente: ")
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
    for i, nombre in enumerate(listaNombre):
        print(f"{i + 1}. {nombre}")

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
                if paciente_index < len(atendido_en_urgencias) and paciente_index < len(nivel_urgencia):
                    atendido = atendido_en_urgencias[paciente_index]
                    nivel_urgencia_paciente = nivel_urgencia[paciente_index]
                else:
                    print("Error: Datos incompletos para el paciente en urgencias.")
                    continue
                
                nombrePaciente = listaNombre[paciente_index]
                sexoPaciente = listaSexo[paciente_index]
                domiPaciente = listaDomi[paciente_index]
                telefonoPaciente = listaTelefono[paciente_index]
                curpPaciente = listaCURP[paciente_index]
                fechaPaciente = listaFecha[paciente_index]
                nssPaciente = listaNSS[paciente_index]
                sangrePaciente = listaSangre[paciente_index]

                generarPDFIndividual(nombrePaciente, sexoPaciente, domiPaciente, telefonoPaciente, curpPaciente, fechaPaciente, nssPaciente, sangrePaciente, atendido, nivel_urgencia_paciente)
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")

def imprimirPacientesEnUrgencias():
    if not listaNombre:
        print("No hay pacientes en urgencias.")
        return

    print("Pacientes en urgencias:")
    for i, nombre_paciente in enumerate(listaNombre):
        if i < len(edad) and i < len(seguro) and i < len(nivel_urgencia):
            print(f"{i + 1}. Nombre: {nombre_paciente}")
        else:
            print(f"Error: Datos incompletos para el paciente {nombre_paciente}")

    while True:
        try:
            opcion = int(input("Ingresa el número del paciente para ver su información detallada (0 para salir): "))
            if opcion == 0:
                break
            elif 1 <= opcion <= len(listaNombre):
                paciente_index = opcion - 1
                if paciente_index < len(atendido_en_urgencias) and paciente_index < len(nivel_urgencia):
                    atendido = atendido_en_urgencias[paciente_index]
                    nivel_urgencia_paciente = nivel_urgencia[paciente_index]
                else:
                    print("Error: Datos incompletos para el paciente en urgencias.")
                    continue
                
                print("Información detallada del paciente en urgencias:")
                print(f"Nombre: {listaNombre[paciente_index]} Edad: {edad[paciente_index]} Número de Seguro Social: {seguro[paciente_index]} Nivel de urgencia: {nivel_urgencia[paciente_index]}")
                
                generarPDFIndividual(listaNombre[paciente_index], listaSexo[paciente_index], listaDomi[paciente_index], listaTelefono[paciente_index], listaCURP[paciente_index], listaFecha[paciente_index], listaNSS[paciente_index], listaSangre[paciente_index], atendido, nivel_urgencia_paciente)

            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")


doctores = ["Dr. Angel Leon.", "Dr. Enrique Lopez", "Dr. Alejandro Ceron"]
enfermeras = ["Enf. Ana Lopez", "Enf. Teresa Sanchez", "Enf. Guadalupe Lopez"]

def mostrarDoctores():
    print("Doctores registrados:")
    for i, nombre in enumerate(doctores):
        print(f"{i + 1}. {nombre}")


def mostrarEnfermeras():
    print("Enfermeras registradas:")
    for i, nombre in enumerate(enfermeras):
        print(f"{i + 1}. {nombre}")