

def calcularImpuesto(sueldo):
    d80000 = 80000
    d40000 = 40000
    
    if sueldo > d80000:
        return (sueldo - d80000) * 0.2
    elif sueldo > d40000:
        return (sueldo - d40000) * 0.1
    else:
        return 0    

def printM(mat):
    dummy = ""    
    
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            dummy += str(mat[i][j])+'\t'
        print(dummy)
        dummy = ""

def process(mat):
    print('-----------------------------------\r')
    print('Paulo Jesus Lopez\r')
    print('-----------------------------------\r')
    
    for i in range(len(mat)):
        mat[i][2] = calcularImpuesto(mat[i][1])

    printM( mat )
    
    print('-----------------------------------\r')
    print('Paulo Jesus Lopez\r')
    print('-----------------------------------\r')



m = [["Bernasconi",50000,0],
            ["Gutierrez ",35000,0],
            ["Michalina ",75000,0],
            ["Parodi   ",110000,0]]

process(m)
