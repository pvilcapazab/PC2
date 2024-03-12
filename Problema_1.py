#Recorremos el rango definido
for i in range(1500, 2701):
    #Si el residuo de "i" entre 7 y 5 es 0, entonces imprimirá el número "i"
    if i % 7 == 0 and i % 5 == 0:
        print(f'El número "{i}" es divisible por 7 y múltiplo de 5')