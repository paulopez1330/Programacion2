mes = 1
salario = 10000
gastos = 8500
adicional = 5000
deuda = 50000


acumulado = 0

while acumulado < deuda:
    acumulado += salario - gastos
    
    if (mes % 6 == 0 ):
        acumulado += adicional

    mes +=1 

print('El usuario tardara ' + str(mes) + ' meses en pagar su deuda ')
