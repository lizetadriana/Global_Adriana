from reportlab.pdfgen import canvas
from FuncionQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, "")
ruta = "C:/Users/adria/OneDrive/Escritorio/Modularidad en Python/Prueba de funciones/"
nombreQR=ruta+"miQR.png"
logo=ruta+"Hospitales.png"

def generarPDFIndividual(nombrePaciente, sexoPaciente, domiPaciente, telefonoPaciente, curpPaciente, fechaPaciente, nssPaciente, sangrePaciente):
    fecha_actual = datetime.datetime.now()
    nombreArchivo = ruta + nombrePaciente + ".pdf"
    generarQR(nombreQR, "Hola desde funcion")
    c = canvas.Canvas(nombreArchivo)
    xInicial = 70
    yInicial = 700
    c.setFont('Helvetica-bold',26)
    c.drawString(300, 750, "Expediente Individual.")
    c.setFont('Helvetica', 20)
    c.drawString(xInicial, yInicial, "Nombre")
    c.drawString(xInicial + 120, yInicial, "Sexo")
    c.drawString(xInicial + 240, yInicial, "Domicilio")
    c.drawString(xInicial + 400, yInicial, "Telefono")
    c.setFont('Helvetica', 18)
    yInicial = yInicial - 20
    c.drawString(xInicial, yInicial, nombrePaciente)
    c.drawString(xInicial + 120, yInicial, sexoPaciente)
    c.drawString(xInicial + 240, yInicial, domiPaciente)
    c.drawString(xInicial + 400, yInicial, telefonoPaciente)

    c.setFont('Helvetica', 20)
    yInicial -= 40
    c.drawString(xInicial, yInicial, "CURP")
    c.drawString(xInicial + 120, yInicial, "Fecha de nacimiento")
    c.drawString(xInicial + 300, yInicial, "NSS")
    c.drawString(xInicial + 400, yInicial, "Tipo de sangre")

    c.setFont('Helvetica', 18)
    yInicial -= 20
    c.drawString(xInicial, yInicial, curpPaciente)
    c.drawString(xInicial + 120, yInicial, fechaPaciente)
    c.drawString(xInicial + 300, yInicial, nssPaciente)
    c.drawString(xInicial + 400, yInicial, sangrePaciente)

    c.drawImage(nombreQR, 200, 400, 100, 100)
    c.drawImage(logo,50, 850, 90,90)

    c.save()
    print(f"--------Reporte de {nombrePaciente} generado------")
