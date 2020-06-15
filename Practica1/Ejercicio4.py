ancho = float(input('Ingrese el ancho del contenedor en metros: '))
largo = float(input('Ingrese el largo del contenedor en metros: '))
alto = float(input('Ingrese el alto del contenedor en metros: '))

cajaVolumen = 0.6 * 0.6 * 0.6

camionVolumen = ancho * largo * alto

cantidadCajas = int(camionVolumen // cajaVolumen)


print( 'Cantidad de cajas total: ' + str(cantidadCajas))
