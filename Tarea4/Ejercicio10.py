def calculoNotas(escrito, practico, participacion):    
    final = escrito * 5 / 10
    final += practico * 3 / 10  
    final += participacion * 2 / 10
    return final


name = input('Ingrese Nombre del Alumno: ')

nota = calculoNotas(
        float(input('Ingrese Nota examen escrito: ')),
        float(input('Ingrese Nota examen practico: ')),
        float(input('Ingrese Nota participacion en clase: '))
      )


print('La nota final del alumno ' + name + ' es ' + str(nota))
