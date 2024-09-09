resultados = input()
resultados = resultados.split(" ")
suma = 0
for resultado in resultados:
    suma += 7 - int(resultado)
print(suma)