import qrcode
ruta= "C:/Users/adria/OneDrive/Escritorio/Modularidad en Python/Prueba de funciones/"
img = qrcode.make("Elaborado por Adriana Mata")
f = open(ruta+"miQR.png", "wb")
img.save(f)
f.close()