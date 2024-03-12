#Con esta variable controlamos el bucle While
respuesta = "si"

#Definimos una lista para almacenar los números
lista = []

#Bucle para ingresar los números
while respuesta != "no":
    #Pregunta de control
    respuesta = input("“Desea ingresar un número? (Si/No): ").lower()

    #Si la respuesta es "si", guardaremos el número en la lista
    if respuesta == "si":
        lista.append(int(input("Ingrese el número: ")))
    #Si la respuesta es "no", romperemos el bucle
    elif respuesta == "no":
        break
    #Si la respuesta no es "si" o "no", entonces comentamos al usuario que su entrada es inválida
    else:
        print("Operación inválida")

#Contamos la cantidad de números pares e impares
cantidad_pares = 0
cantidad_impares = 0
for numero in lista:
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

#Imprimimos la lista de números ingresados, la cantidad de pares e impares
print(f"Números ingresados: {lista}")
print(f"Cantidad de números pares: {cantidad_pares}")
print(f"Cantidad de números impares: {cantidad_impares}")