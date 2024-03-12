#Definimos una función para calcular los "N" (50 en este caso) primeros números de la serie de Fibonacci
def fibonacci(numero_terminos):
    #Guardamos los dos primeros términos de la serie de Fibonacci: 0 y 1
    t0, t1 = 0, 1

    #Creamos una lista donde almacenaremos los números de la serie de fibonacci
    serie_fibonacci = []

    #Calculamos los términos de la serie de Fibonacci sabiendo que el térmno enésimo es igual a la suma de los dos términos anteriores
    for i in range(numero_terminos):
        serie_fibonacci.append(t0)
        t0, t1 = t1, t0 + t1
    return serie_fibonacci

#Imprimimos los 50 primeros términos de la serie de Fibonacci
print(f"Los 50 primeros términos de la serie de Fibonacci es:\n{fibonacci(50)}")