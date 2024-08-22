import tablero_gato

print("EMPIEZA EL JUEGO")

j = 1 #De que jugador es el turno
continuar = True

while continuar:
    
    #Imprimir el tablero actual
    t = tablero_gato.tablero_imprimible()
    print(t)

    #Pedir Tirada
    print("Turno Jugador",j)
    f = int(input("Fila? "))
    c = int(input("Columna? "))

    #Hacer tirada
    libre = tablero_gato.esta_libre(f,c)
    if libre:
        tablero_gato.poner_ficha(f,c,j)
    else:
        print("Casilla Ocupada! Persiste el turno")

    #Comprobar ganador, empate, o continuar
    g = tablero_gato.ganador()

    if g == 1:
        print("Ganaste Jugador 1")
        continuar = False

    elif g == 2:
        print("Ganaste Jugador 2")
        continuar = False

    else:
        ocupado = tablero_gato.ocupado()

        if ocupado:
            print("Empate")
            continuar = False

        else:
            #Cambiar el turno
            if j == 1:
                j = 2
            else:
                j = 1

t = tablero_gato.tablero_imprimible()
print(t)       
print("ACABA EL JUEGO")

