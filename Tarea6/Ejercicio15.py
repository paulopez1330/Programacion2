cantidad = int(input('Ingresa la cantidad de productos : '))
total = 0
porcentaje = 0.0
cantidadDesc = 0


def calculoALFA(total):
    porcentaje = 0.0

    if(cantidad > 2000):
        porcentaje = 0.1
    elif(cantidad > 1000):
        porcentaje = 0.05

    return cantidad - cantidad * porcentaje  
    
def calculoBETA(total):
    desc = 0
    if(total > 2000):
        desc = total - (total - 2000 * 0.25) - (1000 * 0.125)
    elif(total > 1000):
        desc = total - (total - 1000 * 0.125)
    
    return  total - desc


alfa = calculoALFA(cantidad)
beta = calculoBETA(cantidad)

if (alfa < beta):
    print('Conviene comprar con el proveeedor ALFA $' + str(alfa))
else:
    print('Conviene comprar con el proveeedor BETA $' + str(beta))
