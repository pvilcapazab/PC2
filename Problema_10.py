#Definimos una función que corrija fechas
def corregir_fecha(fecha):
    #Guardamos los meses del año en una lista
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    #Ponemos condiciones. Si en la fecha solicitada aparece "/", entonces hará lo siguiente
    if '/' in fecha:
        #Guardará en tres variables los datos separados
        mes, dia, año = fecha.split('/')
        nuevo_formato = f'{año}-{int(mes):02}-{int(dia):02}'
    #Si en la fecha solicitada aparece una coma, entonces hará lo siguiente
    elif ',' in fecha:
        #Separará el mes, día y año respectivos
        mes_dia, año = fecha.split(',')
        mes, dia = mes_dia.split(' ')
        posicion = meses.index(f'{mes}') + 1
        nuevo_formato = f'{año}-{int(posicion):02}-{int(dia):02}'
    #Si el usuario se equivocó de formato, se imprimirá lo siguiente    
    else:
        print("Formato equivocado")
        return
    
    #Regresaremos "nuevo_formato" convirtiendo el mes, dia y la posición en "Int" porque estas se guardaron como str
    return nuevo_formato

#Ponemos en contexto al usuario
print('Ingrese una fecha en el formato: "Mes/Día/Año" o "(Nombre del mes) (Día), (Año)"')

#Solicitamos la fecha en uno de los dos formatos pedidos
fecha = input("Input: ").title()

#Imprimimos el formato corregido
print(f'Output:{corregir_fecha(fecha)}')