#Número de alumnos a enlistar
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

#Creamos una lista para almacenar a los alumnos
alumnos = []

#Bucle para ingresar a los alumnos y sus notas
for i in range(cantidad_alumnos):
    #Pedimos el nombre del alumno
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")

    #Pedimos las 3 notas del alumno
    nota = []
    for j in range(3):
        nota.append(float(input(f"Ingrese la nota {j + 1} del alumno {nombre}: ")))

    #Guardamos el nombre del alumno y sus 3 notas en un diccionario
    alumno = {'Nombre': nombre,
               'Notas': nota}
    
    #Guardamos el diccionario con los datos del alumno en una lista
    alumnos.append(alumno)

#Imprimimos los datos de cada alumno
for estudiante in alumnos:
    print("-" * 30)
    print(f"Nombre: {estudiante['Nombre']}")
    print(f"Notas: {estudiante['Notas']}")