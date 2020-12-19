
# function to test, gives the persistence of a number.

def Persistence(numero):
    numeroEnFormato=numero
    resultado=0

    while not(len(str(numero)) == 1):
        acumulado = 0

        for i in str(numero):
            acumulado = acumulado + int(i)
        resultado = resultado + 1
        numero = acumulado
    print('El numero ingresado, que fue {0} tiene {1} persistencias aditivas.'.format(numeroEnFormato, resultado))
    return resultado

