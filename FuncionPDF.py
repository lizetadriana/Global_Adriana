from reportlab.pdfgen import canvas
ruta = "C:/Users/adria/OneDrive/Escritorio/Modularidad en Python/Prueba de funciones/"
nombreArchivo=ruta + "reporteGlobal.pdf"

def generarPDF():
    c=canvas.Canvas(nombreArchivo)
    c.drawString(200,600,"Hola desde una función")
    c.save()