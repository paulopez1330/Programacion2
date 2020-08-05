def totalMatriz(matriz, matrizTotal):
    for i in range(1, len(matriz)):
        for j in range(1, len(matriz[i])):
            matrizTotal[i] = int(matrizTotal[i]) + int(matriz[i][j])

def sumarCaso(matriz, provincia, mes, casos):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str(matriz[i][0]).upper() == provincia.upper():
                if str(matriz[0][j]).upper() == mes.upper():
                    matriz[i][j] = matriz[i][j] + int(casos)

def imprimirMatriz(matriz, matrizTotal):
    a=""    
    print('\r')
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a+=str(matriz[i][j])+'\t'
        print(a)
        a=""

    print('\r')

    for i in range(len(matrizTotal)):
        a+=str(matrizTotal[i])+'\t'
        print(a)
        a=""

mOriginal = [
    [ 'Provincia', 'Enero', 'Febrero', 'Marzo', 'Abril' ],
    ['Buenos Aires', 300, 400, 300, 200],
    ['CABA', 300, 500, 400, 200],
    ['Santa Cruz', 200, 300, 200, 100],
    ['Cordoba', 100, 200, 300, 100],    
]

mTotal = [
    'Total', 0, 0, 0, 0
]

corte = True

while corte:
    provincia = str(raw_input("Ingrese provincia: ")).replace("\r", "")
    if provincia.upper() == 'FIN':
        corte = False
        break
    mes = str(raw_input("Ingrese mes: ")).replace("\r", "")
    if mes.upper() == 'FIN':
        corte = False
        break
    casos = input("Casos a agregar: ")
    
    sumarCaso(mOriginal, provincia, mes, casos)

totalMatriz(mOriginal, mTotal)
imprimirMatriz(mOriginal, mTotal)
