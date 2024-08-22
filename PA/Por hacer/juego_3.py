from random import randint

intento = 1
print("Trata de adivinar el número que va desde el 0 hasta el 9, ¡tienes 3 intentos!")
meta = randint(0, 9)
numero = -1
while numero != meta:
    numero = int(input("Ingresa un número del 0 al 9:\n"))
    if numero < meta:
        print("Uhm, muy bajo, el número buscado es mayor a lo que ingresaste.")
        intento += 1
    elif numero == meta:
        print(f"¡Felicidades adivinaste el número al intento {intento}!")
    elif numero > meta:
        print("Uhm, muy alto, el número buscado es menor a lo que ingresaste.")
        intento += 1