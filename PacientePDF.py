from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
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
    c = canvas.Canvas(nombreArchivo, pagesize=A4)

    c.setFont('Helvetica-Bold',24)
    c.drawString(180, 750, "Expediente Individual.")

    c.setFont('Helvetica', 20)
    c.drawString(60, 680, "Nombre:")
    c.drawString(60, 640, "Sexo:")
    c.drawString(60, 600, "Domicilio:")
    c.drawString(60, 560, "Telefono:")

    c.setFont('Helvetica', 18)
    c.drawString(280, 680, nombrePaciente)
    c.drawString(280, 640, sexoPaciente)
    c.drawString(280, 600, domiPaciente)
    c.drawString(280, 560, telefonoPaciente)

    c.setFont('Helvetica', 20)
    c.drawString(60, 520, "CURP:")
    c.drawString(60, 480, "Fecha de nacimiento:")
    c.drawString(60, 440, "NSS:")
    c.drawString(60, 400, "Tipo de sangre:")

    c.setFont('Helvetica', 18)
    c.drawString(280, 520, curpPaciente)
    c.drawString(280, 480, fechaPaciente)
    c.drawString(280, 440, nssPaciente)
    c.drawString(280, 400, sangrePaciente)

    c.drawImage(nombreQR, 450, 50, 100, 100)
    c.drawImage(logo,50, 750, 100, 80)

    c.save()
    print(f"--------Reporte de {nombrePaciente} generado------")
