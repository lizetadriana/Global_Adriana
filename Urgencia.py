nombre = []
edad = []
seguro = []

def tipoUrgencia():
    op = 1
    while op != 6:
        print("1. Nivel 1: Prioridad absoluta con atención inmediata y sin demora.")
        print("2. Nivel 2: Situaciones muy urgentes, de riesgo vital.")
        print("3. Nivel 3: Urgente pero estable hemodinámicamente con potencial riesgo vital.")
        print("4. Nivel 4: Urgencia menor, potencialmente sin riesgo vital.")
        print("5. Nivel 5: No urgencia. Poca complejidad en la patología.")
        print("6. Salir")
        op = int(input("Elige una opción: "))
        if op == 1:
            nivel1()
        elif op == 2:
            nivel2()
        elif op == 3:
            nivel3()
        elif op == 4:
            nivel4()
        elif op == 5:
            nivel5()



def nivel1():
    op = 1
    while op != 6:
        print("1. Paro cardiorrespiratorio.")
        print("2. Hemorragias severas.")
        print("3. Pérdida de un órgano.")
        print("4. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente()
        elif op == 2:
            pedir_datos_paciente()
        elif op == 3:
            pedir_datos_paciente()

def nivel2():
    op = 1
    while op != 6:
        print("1. Dolor extremo.")
        print("2. Heridas no vitales.")
        print("3. Diarrea aguda con dolor abdominal.")
        print("4. Vómito sin tolerancia a vía oral.")
        print("5. Fiebre aguda.")
        print("6. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente()
        elif op == 2:
            pedir_datos_paciente()
        elif op == 3:
            pedir_datos_paciente()

def nivel3():
    op = 1
    while op != 6:
        print("1. Dolor por un par de días.")
        print("2. Cuerpo extraño en el oído sin sangrado.")
        print("3. Dolor lumbar.")
        print("4. Lumbalgia súbita")
        print("5. ")
        print("6. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente()
        elif op == 2:
            pedir_datos_paciente()
        elif op == 3:
            pedir_datos_paciente()

def nivel4():
    op = 1
    while op != 6:
        print("1. Dolor en el estómago.")
        print("2. Sinusitis.")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente()
        elif op == 2:
            pedir_datos_paciente()

def nivel5():
    op = 1
    while op != 6:
        print("1. Dolor de garganta.")
        print("2. Cólico abdominal.")
        print("3. Dolor de cabeza")
        print("4. ")
        print("5. ")
        print("6. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente()
        elif op == 2:
            pedir_datos_paciente()
        elif op == 3:
            pedir_datos_paciente()

def pedir_datos_paciente():
    nombre.append(input("Ingresa el nombre del paciente: "))
    edad.append(input("Ingresa la edad del paciente: "))
    seguro.append(input("Ingresa el número de seguro social del paciente: "))
    print("---------------- Información guardada ---------------")
    input("Presiona Enter para continuar...")

