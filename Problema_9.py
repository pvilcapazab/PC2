#Definimos una función para quitar vocales a cualquier texto   
def sin_vocales(oracion):
    #Definimos las vocales minúsculas y mayúsculas
    vocales = 'aeiouAEIOU'

    #Creamos una lista donde almacenaremos letra por letra
    lista = []

    #Comenzamos un bucle "For" para cada letra que aparece en el texto dado
    for letra in oracion:
        if letra not in vocales:
            #Si la letra no está en las vocales, entonces la añadimos a la lista
            lista.append(letra)

    #Usamos .join para unir los elementos de la lista en un nuevo str
    return "".join(lista) 

#Solicitamos al usuario un texto
oracion = input("Input: ")

#Imprimos el texto sin vocales
print(f"Output: {sin_vocales(oracion)}")