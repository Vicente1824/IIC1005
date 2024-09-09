rep_larga = 0
entrada = input()
ultima_letra = ""
repeticion_actual = 0
letra_ganadora = ""
for letra in entrada:
    if letra != ultima_letra:
        repeticion_actual = 1
        ultima_letra = letra
    elif letra == ultima_letra:
        repeticion_actual += 1
    if repeticion_actual >= rep_larga:
        letra_ganadora = letra
        rep_larga = repeticion_actual
print(rep_larga)
