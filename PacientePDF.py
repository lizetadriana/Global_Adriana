from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
from FuncionQR import *
import datetime
import locale
from Urgencia import *
from PacientePDF import *

locale.setlocale(locale.LC_ALL, "")
ruta = "C:/Users/adria/OneDrive/Escritorio/Modularidad en Python/Prueba de funciones/"
nombreQR = ruta + "miQR.png"
logo = ruta + "Hospitales.png"

def generarPDFIndividual(nombrePaciente, sexoPaciente, domiPaciente, telefonoPaciente, curpPaciente, fechaPaciente, nssPaciente, sangrePaciente):
    fecha_actual = datetime.datetime.now()
    nombreArchivo = ruta + nombrePaciente + ".pdf"
    generarQR(nombreQR, f"Nombre: {nombrePaciente}, NSS: {nssPaciente}")
    c = canvas.Canvas(nombreArchivo, pagesize=A4)

    c.setFont('Helvetica-Bold',24)
    c.drawString(180, 700, "Expediente Individual.")

    c.setFont('Helvetica-Bold', 20)
    c.drawString(60, 650, "Nombre:")
    c.drawString(60, 600, "Sexo:")
    c.drawString(60, 550, "Domicilio:")
    c.drawString(60, 500, "Telefono:")

    c.setFont('Helvetica', 18)
    c.drawString(280, 650, nombrePaciente)
    c.drawString(280, 600, sexoPaciente)
    c.drawString(280, 550, domiPaciente)
    c.drawString(280, 500, telefonoPaciente)

    c.setFont('Helvetica-Bold', 20)
    c.drawString(60, 450, "CURP:")
    c.drawString(60, 400, "Fecha de nacimiento:")
    c.drawString(60, 350, "NSS:")
    c.drawString(60, 300, "Tipo de sangre:")

    c.setFont('Helvetica', 18)
    c.drawString(280, 450, curpPaciente)
    c.drawString(280, 400, fechaPaciente)
    c.drawString(280, 350, nssPaciente)
    c.drawString(280, 300, sangrePaciente)

    c.drawImage(nombreQR, 450, 50, 100, 100)
    c.drawImage(logo,50, 750, 200, 100)

    c.save()
    print(f"--------Reporte de {nombrePaciente} generado------")
