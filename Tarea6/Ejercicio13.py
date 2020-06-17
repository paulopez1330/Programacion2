cantidad = int(input('Ingresa la cantidad de productos : '))
total = 0
porcentaje = 0.0

if(cantidad > 2000):
    porcentaje = 0.1
elif(cantidad > 1000):
    porcentaje = 0.05

total = cantidad - cantidad * porcentaje

print('porcentaje : ' + str(porcentaje))
print('El total es $' + str(total))
