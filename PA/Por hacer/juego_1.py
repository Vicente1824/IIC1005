from random import randint
from time import sleep

puntaje = 0
puntaje_computadora = 0
while (puntaje < 30) and (puntaje_computadora < 30):
    input("¡Aprieta ENTER para lanzar el dado!")
    numero = randint(1, 6)
    puntaje += numero
    print(f"¡Obtuviste un {numero}! Ahora tienes {puntaje} puntos.")
    if puntaje < 30:
        print("Ahora le toca a la computadora.")
        sleep(0.5)
        numero = randint(1, 6)
        puntaje_computadora += numero
        print(f"¡La computadora obtuvo un {numero}! Ahora tiene {puntaje_computadora} puntos.")
if puntaje >= 30:
    print("¡Felicidades, has ganado!")
else:
    print("La computadora ha ganado.")