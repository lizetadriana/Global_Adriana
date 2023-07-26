from reportlab.pdfgen import canvas
from FuncionQR import *
ruta = "C:/Users/adria/OneDrive/Escritorio/Modularidad en Python/Prueba de funciones/"
nombreArchivo=ruta + "reporteGlobal.pdf"
nombreQR=ruta+"miQR.png"

def generarPDF(listaNombres,listaEdades):
    generarQR(nombreQR, "Hola desde funcion")
    c=canvas.Canvas(nombreArchivo)
    xInicial=200
    yInicial=700
    c.setFont('Helvetica',20)
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial+120,yInicial,"Nombre")
    for i in range(len(listaNombres)):
        c.setFont('Helvetica',18)
        yInicial=yInicial-20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial+120,yInicial,listaNombres[i])

        c.drawImage(nombreQR,200,400,100,100)

    c.save()
    print("Reporte generado------")