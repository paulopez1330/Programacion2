import os
import os.path

def printName():
    print('-----------------------------------------------------------\r')
    print('Paulo Jesus Lopez\r')
    print('-----------------------------------------------------------\r')

def printListado(lista):
    dummy = ""    
    totSalario = 0
    print('legajo'.rjust(3,' ') + '\t' + 'nombre'.rjust(20,' ') + 'salario'.rjust(10,' '))
    
    for l in lista:
        dummy += l[0:3] + '\t'
        dummy += l[4:23] + '\t'        
        s = l[24:33].replace('0','')
        dummy += s + '\t'        
        totSalario = int(totSalario) + int(s)
        print(dummy)
        dummy = ""
        
    print('\r')
    print('\r')
    print('Cantidad de Empleados:         ', len(lista))
    print('Total Salario:                 ', str(totSalario))
    
    if(len(lista) == 0):
        print('Promedio Salarial:             ', '0')
    else:        
        print('Promedio Salarial:             ', str(totSalario / len(lista)))

def store(operacion, registro):
    
    fileOper = None
    fileOperW = None
    
    if (os.path.isfile('./dataBase.txt') == False):
        fileOper = open(os.getcwd() + '\\dataBase.txt', 'w')
        fileOper.close()

    fileOper = open(os.getcwd() + '\\dataBase.txt', 'r')
    try:
        lines = fileOper.readlines()
                
        if(lines.count == 0):
            if(operacion == 'l'):
                print('No se encontraron registros')
                return False
            if (operacion != 'a'):
                print('No se encontro el legajo')
                return False
        
        if(operacion == 'l'):
            return True, lines

        temp = ''
        cambio = False
        for line in lines:
            if(line[0:3] == registro[0:3]):
                if(operacion == 'b'):
                    cambio = True
                    continue
                elif(operacion == 'm'):
                    temp = temp + registro + '\r'
                    cambio = True
                    continue
                elif(operacion == 'a'):
                    print('no se puede crear ya que el legajo es existente')
                    return False
            
            temp = temp + line

        fileOper.close()
        
        if(operacion == 'a'):
            fileOperW = open(os.getcwd() + '\\dataBase.txt', 'a')
            fileOperW.write(registro + '\r')
            return True

        if(cambio):
            fileOperW = open(os.getcwd() + '\\dataBase.txt', 'w')
            fileOperW.write(temp)
            fileOperW.close()
            return True
        else:
            print('No se encontro el legajo')
            return False
    except:
        print('Hubo un error al grabar en base de datos.')
        return False
    finally:
        if (fileOper != None):
            fileOper.close()
        if (fileOperW != None):
            fileOperW.close()

def ParseadoRegistro(legajo: str, nombre: str, salario: str):
    return legajo.rjust(3,' ') + nombre.rjust(20,' ') + salario.rjust(10,'0')

def modificacion():
    
    print('\r')
    print('Imgrese datos de Empleado para modificacion:')
    print('\r')

    mensaje, legajo, nombre, salario = ingresoDatos()

    if (len(mensaje) > 0):
        print(mensaje)
        return
    else:
        result = store('m', ParseadoRegistro(legajo, nombre, salario))
        if(result):
            print('Modificado satisfactoriamente')

def alta():
    print('\r')
    print('Imgrese datos de Empleado para creacion:')
    print('\r')
    mensaje, legajo, nombre, salario = ingresoDatos()

    if (len(mensaje) > 0):
        print(mensaje)
        return
    else:
        result = store('a', ParseadoRegistro(legajo, nombre, salario))
        if(result):
            print('Agregado satisfactoriamente')

def baja():

    print('\r')
    print('Imgrese legajo del Empleado para dar de baja:')
    print('\r')

    message, legajo = ingresoLegajo()

    if(len(message) > 0):
        return message
    
    result = store('b', legajo.rjust(3,' '))
    
    if(result):
        print('Eliminado satisfactoriamente')

def ingresoLegajo():
    legajo = str(input('Ingrese Legajo:'))
    
    if (len(legajo) == 0):
        return 'El legajo no puede ser vacio', None
    elif(len(legajo) > 3):
        return 'El legajo no puede tener mas de 3 caracteres', None

    return '', legajo

def ingresoDatos():
    try:    
        message, legajo = ingresoLegajo()

        if(len(message) > 0):
            return message, None, None, None

        nombre = str(input('Ingrese Nombre:'))
        
        if (len(nombre) == 0):
            return 'El nombre no puede estar vacio', None, None, None
        elif(len(nombre) > 20):
            return 'El nombre no puede tener mas de 20 caracteres', None, None, None

        
        salario = str(input('Ingrese Salario:'))

        if (len(salario) == 0):
            return 'El salario no puede estar vacio', None, None, None
        elif(len(salario) > 10):
            return 'El salario no puede tener mas de 10 digitos', None, None, None

        if(salario.isnumeric() == False):
            return 'El salario debe ser numerico', None, None, None

        return '', legajo, nombre, salario
    except:
        return'Hubo un error al cargar datos de empleado', None, None, None

def listado():
    
    printName()
    
    print('\r')
    print('Listado de Empleados:')
    print('\r')

    result, lista = store('l','')
    
    if(result):
        printListado(lista)

def menu():
    print('     \r')
    print('Menu de Opciones:')
    print('     A - Alta')
    print('     B - Baja')
    print('     M - Modificación')
    print('     L - Listado')
    print('     S - Salida')
    print('     \r')

def process():

    print('     \r')
    print('Bienvenido al sistema CRUD Paisan')
    
    menu()
    
    while True:
        opcion = input('Seleccione opcion de menu:').upper()
        
        if(opcion == 'A'):
            alta()
        elif (opcion == 'B'):
            baja()
        elif (opcion == 'M'):
            modificacion()
        elif (opcion == 'L'):
            listado()
        elif (opcion == 'S'):
            print('saliendo del sistema')
            exit()
        else:
            print('opcion invalida')
        
        while True:
            
            print('\r')
            print('     V - Volver')
            print('     S - Salir')
            print('\r')
            opcion = input('Seleccione opcion de menu:').upper()
            
            if(opcion == 'V'):
                menu()
                break
            elif(opcion == 'S'):
                print('saliendo del sistema')
                exit()
            else :
                print('opcion invalida')

process()
