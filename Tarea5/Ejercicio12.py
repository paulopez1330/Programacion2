empleados = 1
salario = 1000
produccion = 3000
alfajor = 1.5
rebaja = 0.1

totalVenta = 0
totalSalario = 0
totalProduccion = 0
maxGanancia = 0
maxEmpleadosGanancia = 0
condition = True

while condition:
    totalSalario = salario * empleados
    totalProduccion = produccion * empleados
    totalVenta = totalProduccion * alfajor

    if (totalVenta - totalSalario > maxGanancia):
        maxGanancia = totalVenta - totalSalario
        maxEmpleadosGanancia = empleados

    if (totalVenta < totalSalario):
        condition=False

    alfajor = alfajor - alfajor * rebaja
    empleados += 1

print('la cantidad de empleados que puede contratar como maximo es ' + str(empleados))
print('la mayor ganancia es con  ' + str(maxEmpleadosGanancia) + ' empleados')
