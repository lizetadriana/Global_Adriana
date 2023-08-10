from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from FuncionQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, "")
ruta = "C:/Users/adria/OneDrive/Escritorio/Modularidad en Python/Prueba de funciones/"
nombreQR=ruta+"miQR.png"
logo=ruta+"Hospitales.png"

def generarPDF(listaNombre, listaSexo, listaDomi, listaTelefono):
    fecha_actual=datetime.datetime.now()
    nombreArchivo=ruta + "reporteGlobal"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
    generarQR(nombreQR, "Hola desde funcion")
    c=canvas.Canvas(nombreArchivo, pagesize=A4)
    
    c.setFont('Helvetica-Bold',20)
    c.drawString(180, 750, "Pacientes.")

    c.setFont('Helvetica', 18)
    c.drawString(60, 680, "Nombre")
    c.drawString(100, 680, "Sexo")
    c.drawString(150, 680, "Domicilio")
    c.drawString(200, 680, "Telefono")
    for i in range(len(listaNombre)):
        c.setFont('Helvetica', 16)
        
        c.drawString(60, 640, -40, listaNombre[i])
        c.drawString(100, 640, -40, listaSexo[i])
        c.drawString(150, 640, -40, listaDomi[i])
        c.drawString(200, 640, -40, listaTelefono[i])

    c.drawImage(nombreQR, 450, 50, 100, 100)
    c.drawImage(logo,50, 750, 100, 80)

    c.save()
    print("---------------Reporte global generado------")