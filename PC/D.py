pruebas = int(input())
for rep in range(pruebas):
    detalles = input()
    detalles = detalles.split(" ")
    puntos = int(detalles[1]) * 3
    puntos -= int(detalles[0]) - int(detalles[1])
    if puntos >= int(detalles[2]):
        print("PASS")
    else:
        print("FAIL")