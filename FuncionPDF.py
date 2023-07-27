from reportlab.pdfgen import canvas
from FuncionQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, "")
ruta = "C:/Users/adria/OneDrive/Escritorio/Modularidad en Python/Prueba de funciones/"
nombreQR=ruta+"miQR.png"

def generarPDF(listaNombre,listaSexo):
    fecha_actual=datetime.datetime.now()
    nombreArchivo=ruta + "reporteGlobal"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
    generarQR(nombreQR, "Hola desde funcion")
    c=canvas.Canvas(nombreArchivo)
    xInicial=200
    yInicial=700
    c.setFont('Helvetica',20)
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial+120,yInicial,"Nombre")
    for i in range(len(listaNombre)):
        c.setFont('Helvetica',18)
        yInicial=yInicial-20
        c.drawString(xInicial,yInicial,listaSexo[i])
        c.drawString(xInicial+120,yInicial,listaNombre[i])

        c.drawImage(nombreQR,200,400,100,100)

    c.save()
    print("Reporte generado------")