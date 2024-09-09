puntos = input()
puntos = puntos.split(" ")
puntos_alice = int(puntos[0])
puntos_bob = int(puntos[1])
if puntos_alice >= puntos_bob * 2:
    print("Yes")
else:
    print("No")
