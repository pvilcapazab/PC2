#Definimos una función para averiguar si un número es primo o no
def primo(numero):
    #El número 1 no es primo
    if numero == 1:
        return False
    
    #Calculamos el residuo del número ingresado con valores que van desde 2 hasta la mitad del número ingresado para ahorrar calculos
    #Si algun residuo da 0, quiere decir que hay más de 2 divisores para dicho número. Por lo tanto, no es primo
    for i in range(2, int(numero * (1/2))):
        if numero % i == 0:
            return False
    
    #Regresará True si las sentencias anteriores no se cumplen. Por lo tanto, es primo
    return True
    
#Creamos un bucle para que el número sea positivo
numero = -1
while numero < 0:
    #Solicitamos un número al usuario
    numero = int(input("Ingrese un número entero: "))
    if numero < 0:
        print("Por favor, ingrese un número positivo")

#Según la función "primo": Si es "True" el número es primo, sino será no primo
if primo(numero):
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")