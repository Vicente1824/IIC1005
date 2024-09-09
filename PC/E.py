repeticiones = int(input())

for rep in range(repeticiones):
    datos = input()
    datos = datos.split()
    fila = int(datos[0])
    columna = int(datos[1])
    if (columna % 2) != 0 and fila < columna:
        resultado = (columna ** 2) - fila + 1

    elif (columna % 2) == 0 and fila <= columna:
        resultado = ((columna-1) ** 2) + fila

    elif (fila % 2) == 0 and columna < fila:
        resultado = (fila ** 2) - columna + 1

    elif (fila % 2) != 0 and columna <= fila:
        resultado = ((fila-1) ** 2) + columna

    print(resultado)