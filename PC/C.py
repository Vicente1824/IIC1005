total_n = int(input())
numeros = input()
numeros = numeros.split(" ")
lista = set()
for n in range(1, total_n + 1):
    lista.add(str(n))
for numero in numeros:
    lista.remove(numero)
for i in lista:
    print(int(i))