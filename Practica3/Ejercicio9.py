infectadoshoy = int(input('Ingrese la cantidad de infectados al dia de hoy: '))
limiteMax = int(input('Ingrese la cantidad maxima que puede tener el sistema de Salud: '))


dia = 1

while infectadoshoy < limiteMax:
    infectadoshoy = infectadoshoy ** 3
    dia += 4

print("El el dia " + str(dia)  + " superará el límite de atención del sistema de salud")
