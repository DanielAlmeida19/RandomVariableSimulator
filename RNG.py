import copy
 
def Generator(seed, n):
    y = [0]*2
    x = [0]*(n+2)
    y[0] = seed
    m = (pow(2,31)-1)
    for i in range(1,n+2):
        y[1] = (16807 * y[0]) % m  # Usar o operador % para calcular o módulo
        x[i] = y[1] / m
            
        y[0] = y[1]
    return(x)