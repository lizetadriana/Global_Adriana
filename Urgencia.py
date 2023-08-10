from collections import deque

nombre = []
edad = []
seguro = []
nivel_urgencia=[]
cola_pacientes = deque()

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
    while op != 4:
        print("1. Paro cardiorrespiratorio.")
        print("2. Hemorragias severas.")
        print("3. Pérdida de un órgano.")
        print("4. Labor de parto.")
        print("5. Luxación de alguna parte del cuerpo.")
        print("6. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente("1.1 Paro cardiorrespiratorio")
            break
        elif op == 2:
            pedir_datos_paciente("1.2 Hemorragias severas.")
            break
        elif op == 3:
            pedir_datos_paciente("1.3 Pérdida de un órgano.")
            break
        elif op == 4:
            pedir_datos_paciente("1.4 Labor de parto.")
            break
        elif op == 5:
            pedir_datos_paciente("1.5 Luxación de alguna parte del cuerpo.")
            break

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
            pedir_datos_paciente("2.1 Dolor extremo.")
            break
        elif op == 2:
            pedir_datos_paciente("2.2 Heridas no vitales.")
            break
        elif op == 3:
            pedir_datos_paciente("2.3 Diarrea aguda con dolor abdominal.")
            break
        elif op == 4:
            pedir_datos_paciente("2.4 Vómito sin tolerancia a vía oral.")
            break
        elif op == 5:
            pedir_datos_paciente("2.5 Fiebre aguda.")
            break

def nivel3():
    op = 1
    while op != 6:
        print("1. Dolor por un par de días.")
        print("2. Cuerpo extraño dolor en el oído sin sangrado.")
        print("3. Dolor lumbar.")
        print("4. Lumbalgia súbita.")
        print("5. Infección en cuencas de ojos.")
        print("6. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente("3.1  Dolor por un par de días.")
            break
        elif op == 2:
            pedir_datos_paciente("3.2 Cuerpo extraño dolor en el oído sin sangrado.")
            break
        elif op == 3:
            pedir_datos_paciente("3.3 Dolor lumbar.")
            break
        elif op == 4:
            pedir_datos_paciente("3.4 Lumbalgia súbita.")
            break
        elif op == 5:
            pedir_datos_paciente("3.5 Infección en cuencas de ojos.")
            break

def nivel4():
    op = 1
    while op != 6:
        print("1. Dolor en el estómago.")
        print("2. Sinusitis.")
        print("3. Infección en vías urinarias.")
        print("4. Dolores musculares.")
        print("5. Virus varicela-zoster.")
        print("6. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente("4.1 Dolor en el estómago.")
            break
        elif op == 2:
            pedir_datos_paciente("4.2 Sinusitis.")
            break
        elif op == 3:
            pedir_datos_paciente("4.3 Infección en vías urinarias.")
            break
        elif op == 4:
            pedir_datos_paciente("4.4 Dolores musculares.")
            break
        elif op == 5:
            pedir_datos_paciente("4.5 Virus varicela-zoster.")
            break

def nivel5():
    op = 1
    while op != 6:
        print("1. Dolor de garganta.")
        print("2. Cólico abdominal.")
        print("3. Dolor de cabeza.")
        print("4. Insomnio.")
        print("5. Estres postraumatico.")
        print("6. Volver al menú principal.")
        op = int(input("Elige una opción: "))
        if op == 1:
            pedir_datos_paciente("5.1 Dolor de garganta.")
            break
        elif op == 2:
            pedir_datos_paciente("5.2 Cólico abdominal.")
            break
        elif op == 3:
            pedir_datos_paciente("5.3 Dolor de cabeza.")
            break
        elif op == 4:
            pedir_datos_paciente("5.4 Insomnio.")
            break
        elif op==5:
            pedir_datos_paciente("5.5 Estres postraumatico.")
            break

def pedir_datos_paciente(nivel):
    nombre.append(input("Ingresa el nombre del paciente: "))
    edad.append(input("Ingresa la edad del paciente: "))
    seguro.append(input("Ingresa el número de seguro social del paciente: "))
    nivel_urgencia.append(nivel)
    cola_pacientes.append((nombre, edad, seguro, nivel))
    print("---------------- Información guardada ---------------")
    input("Presiona Enter para continuar...")
