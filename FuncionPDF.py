from reportlab.pdfgen import canvas
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
    c=canvas.Canvas(nombreArchivo)
    xInicial=200
    yInicial=700
    c.setFont('Helvetica', 20)
    c.drawString(xInicial, yInicial, "Nombre")
    c.drawString(xInicial + 120, yInicial, "Sexo")
    c.drawString(xInicial + 240, yInicial, "Domicilio")
    c.drawString(xInicial + 400, yInicial, "Telefono")
    for i in range(len(listaNombre)):
        c.setFont('Helvetica', 18)
        yInicial = yInicial - 20
        c.drawString(xInicial, yInicial, listaNombre[i])
        c.drawString(xInicial + 120, yInicial, listaSexo[i])
        c.drawString(xInicial + 240, yInicial, listaDomi[i])
        c.drawString(xInicial + 400, yInicial, listaTelefono[i])

        c.drawImage(nombreQR, 200, 400, 100, 100)
        c.drawImage(logo,50, 850, 90,90)

    c.save()
    print("---------------Reporte global generado------")