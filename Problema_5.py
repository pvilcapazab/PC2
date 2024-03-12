#Definimos una función con dos variables que nos devolverá la cantidad de veces que aparece un dígito en un número
def contador(numero, digito):
    numero = str(numero)
    return numero.count(str(digito))

#Ponemos en contexto al usuario, y solicitamos el número como el digito
print("Hallaremos cuántas veces aparece un dígito en un número")
numero = int(input("Ingrese el número: "))
digito = int(input("Ingrese el digito: "))

#Imprimimos
print(f"Número ingresado: {numero} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número: {contador(numero, digito)}")