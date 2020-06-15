ancho = float(input('Ingrese el ancho del parque en metros: '))
largo = float(input('Ingrese el largo del parque en metros: '))

bloqueLargo = 1.2
bloqueAncho = 0.8
costoBloque = 450.0

superficieParque = ancho * largo
superficieBloque = bloqueAncho * bloqueLargo
cantidadBloques = int((superficieParque / superficieBloque) + 1.0)
costo = costoBloque * cantidadBloques

print( 'Cantidad de bloques requeridos: ' + str(cantidadBloques))
print( 'Costo total: ' + str(costo))
