def validateData( dataTyp, message ):
    try:
        value = input(message)

        if dataTyp is int:
            return int(value)
        elif dataTyp is str:
            return str(value).upper()
        else:
            raise NameError("Dato invalido")
    except ValueError:
        raise NameError("Dato invalido")

def sumCases( prov, month, cases, mat ):
    dummy = None
    try:    
        if cases < 0:
            raise NameError("valor de casos incorrecto")

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if str(mat[i][0]).upper() == prov.upper():
                    if str(mat[0][j]).upper() == month.upper():
                        mat[i][j] = int(mat[i][j]) + int(cases)
                        dummy = mat[i][j]

        if dummy == None:
            raise NameError("Origen desconocido")
        
        return dummy

    except NameError:
        raise NameError("Datos invalidos")

def sumTotal(mat, matT):
    dummy = 0

    for i in range(1, len(mat)):
        for j in range(1, len(mat[i])):
            matT[i][0] = int(matT[i][0]) + int(mat[i][j])
            dummy = int(matT[i][0])

    return dummy

def printM(mat):
    dummy = ""    
    
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            dummy += str(mat[i][j])+'\t'
        print(dummy)
        dummy = ""

def process():
    corte = True
    while corte:
        try:
            prov = validateData( str, "Ingrese provincia: ")
            if prov == 'FIN':
                corte = False
                break
            
            month = validateData( str, "Ingrese mes: ")
            if month == 'FIN':
                corte = False
                break
        
            causes = validateData( int, "Casos a agregar: ")

            sumCases(prov, month, causes, m)
        except NameError as err:
            print(err.args[0])

m = [
    [ 'PROVINCIA', 'ENERO', 'FEBRERO', 'MARZO', 'ABRIL' ],
    ['BUENOS AIRES', 300, 400, 300, 200],
    ['CABA', 300, 500, 400, 200],
    ['SANTA CRUZ', 200, 300, 200, 100],
    ['CORDOBA', 100, 200, 300, 100],
]

mT = [ ['TOTAL'], [0], [0], [0], [0] , ]

process()
sumTotal( m, mT )
print('\r')
printM( m )
print('\r')
printM( mT )
