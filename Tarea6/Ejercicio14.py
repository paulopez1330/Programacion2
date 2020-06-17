cantidad = int(input('Ingresa la cantidad de productos : '))
total = 0
porcentaje = 0.0
cantidadDesc = 0

def calculo(value):
    total = 0
    if(value > 2000):
        total = value - (value - 2000 * 0.25) - (1000 * 0.125)
    elif(value > 1000):
        total = value - (value - 1000 * 0.125)
    
    return  value - total

print('El total es $' + str(calculo(cantidad)))
