
import enum

class Billetes(enum.Enum):
    b500 = 500
    b200 = 200
    b100 = 100
    b50 = 50
    b20 = 20
    b10 = 10
    b5 = 5
    b2 = 2

def calculo(sueldo, billete):
    cantidad = int(sueldo //  billete)
    
    if (cantidad > 0 ):
        print(str(cantidad) + " billete/moneda de $" + str(billete))
        sueldo = sueldo % billete

    return sueldo

sueldo = float(input('Ingrese el Monto a Pagar: '))

print('Monto a Pagar: ' + str(sueldo))
print('Detalle de Pago:')
sueldo = calculo(sueldo, Billetes.b500.value)
sueldo = calculo(sueldo, Billetes.b200.value)
sueldo = calculo(sueldo, Billetes.b100.value)
sueldo = calculo(sueldo, Billetes.b50.value)
sueldo = calculo(sueldo, Billetes.b20.value)
sueldo = calculo(sueldo, Billetes.b10.value)
sueldo = calculo(sueldo, Billetes.b5.value)
sueldo = calculo(sueldo, Billetes.b2.value)
