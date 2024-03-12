#Definimos una función para calcular el factorial de un número
def factorial(numero):
    #El factorial de 0 y 1 es 1
    if numero == 0 or numero == 1:
        return 1
    else:
        #Usamos funciones recursivas para hallar el factorial de un número
        return numero * factorial(numero - 1)

#Ponemos en contexto al usuario y creamos la variable de control
print("----Calcular factorial----")
numero = -1

#Creamos un bucle While para obtener un número entero positivo
while numero < 0:
    #Solicitamos un número entero al usuario
    numero = int(input("Ingrese un número entero: "))
    if numero < 0:
        #Si no es positivo, se imprimirá lo siguiente:
        print("Por favor, ingrese un número positivo")

#Imprimimos el factorial
print(f"El factorial de {numero} es {factorial(numero)}")