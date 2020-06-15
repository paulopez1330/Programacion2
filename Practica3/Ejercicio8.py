disponible = float(input('Ingrese el Monto Disponible: '))
precio = float(input('Ingrese el precio de la empanada: '))

print(str(int(disponible //  precio)) + ' empanadas puede comprar')

sobrante = disponible % precio

print("$" + str(sobrante) + ' le sobra')

if( sobrante> 0):
    print("$" + str(precio- sobrante) + ' pida prestado para comprar otra empanada')
