largo_matriz = int(input())
matriz = input()
matriz = matriz.split()
elemento_anterior = int(matriz[0])
movs = 0
for rep in range(1, largo_matriz):
    suma = elemento_anterior - int(matriz[rep])
    if suma > 0:
        movs += suma
        elemento_anterior = int(matriz[rep]) + suma
    else:
        elemento_anterior = int(matriz[rep])

print(movs)
