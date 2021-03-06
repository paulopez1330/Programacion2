def calculoALFA(cantidad):
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


productos = []

cantidadProductos = int(input('Ingresa la cantidad de productos a calcular : '))

for p in range(cantidadProductos):
    productos.append(int(input('Ingresa la cantidad de productos a comprar: ')))

for p in productos:
    alfa = calculoALFA(p)
    beta = calculoBETA(p)
    if (alfa < beta):
        print('Para ' + str(p) + 'conviene comprar con el proveeedor ALFA $' + str(alfa))
    else:
        print('Para ' + str(p) + 'conviene comprar con el proveeedor BETA $' + str(beta))
