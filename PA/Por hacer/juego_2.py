from random import randint, choice
from time import sleep, time

operaciones = ["+", "-", "x"]
tiempo_total = 0
print("¡Bienvenido al juego de cálculos rápidos!\nIniciando el juego...")
sleep(1)
for i in range(10):
    operacion = choice(operaciones)
    numero_1 = randint(0, 15)
    numero_2 = randint(0, 15)
    if operacion == "+":
        resultado = numero_1 + numero_2
    elif operacion == "-":
        resultado = numero_1 - numero_2
    elif operacion == "x":
        resultado = numero_1 * numero_2
    print(f"¡Rápido! ¡Resuelve esta operación!\n{int(numero_1)} {operacion} {int(numero_2)}")
    entrada = 9999999
    tiempo_inicial = time()
    while entrada != resultado:
        entrada = int(input("Tu respuesta: "))
    tiempo_final = time()
    tiempo_intento = tiempo_final - tiempo_inicial
    print(f"¡Correcto! Te demoraste {tiempo_intento} segundos.")
    tiempo_total += tiempo_intento
print(f"¡Has terminado! Te demoraste {tiempo_total} segundos en los 10 intentos.")