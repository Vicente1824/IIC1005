def dijkstra(N, INI, FIN, precios: list):

    #-------------------------------
    # 1- CREAR LA TABLA DIJKSTRA
    #-------------------------------
    '''
    Lista T de N elementos, uno para cada ciudad. Cada elemento x es una lista [v,d,p]
    indicando si x ya ha sido visitado, el precio mas barato desde INI a x y la ciudad
    previa por la que llegar a x.

    Crear la lista T con todas las ciudades no visitadas, precio infinito y previo vacio (-1).
    '''
    T = [ ]
    for c in range(0, N):
        e = [False, 999999999, -1]
        T.append(e)

    '''
    El precio de INI a INI es 0
    '''
    T[INI][1] = 0


    #-------------------------------
    # 2- ACTUALIZAR LA TABLA HASTA VISITAR TODOS
    #-------------------------------
    faltan_por_visitar = True
    for i in range(N):
        '''
        Buscar la ciudad 'x' con el precio menor que no hayas visitado
        '''
        menor_precio = 9999999999999
        for indice in range(len(T)):
            if (not T[indice][0]) and (T[indice][1] < menor_precio):
                menor_precio = T[indice][1]
                menor_estacion = indice

        '''
        Buscar los vecinos (las ciudades donde se puede viajar desde x) que no hemos visitado
        '''
        precios_vecinos = []
        numero_vecino = 0
        for celda in precios[menor_estacion]:
            if celda != -1:
                if not T[numero_vecino][0]:
                    precios_vecinos.append((celda, numero_vecino))
            numero_vecino += 1
                
        '''
        Actualizar la tabla T. Veamos si el precio de llegar a x, mas lo que cuesta llegar de x a v
        es menor que lo que ya esta en la tabla T. Si es asi, actualizamos el precio y
        '''
        for vecino in precios_vecinos:
            precio_total = T[menor_estacion][1] + vecino[0]
            precio_anterior = T[vecino[1]][1]
            if precio_total < precio_anterior:
                T[vecino[1]][1] = precio_total
                T[vecino[1]][2] = menor_estacion

        '''
        Marcar x como visitado y mirar si aun quedan ciudades por visitar
        '''
        T[menor_estacion][0] = True

    #-------------------------------
    # 3- CALCULAR EL MEJOR PRECIO Y SU RUTA
    #-------------------------------
    '''
    El mejor precio de INI a FIN esta en la tabla
    '''
    mejor_precio = T[FIN][1]

    '''
    Para obtener la mejor ruta hay que ir desde FIN hasta INI siguiendo los previous
    '''
    mejor_ruta = [ ]
    mejor_ruta.append(FIN)
    z = FIN
    while z != INI:
        z = T[z][2]
        mejor_ruta.append(z)
    mejor_ruta.reverse()

    #-------------------------------
    # 4- RETORNAR
    #-------------------------------
    resultado = [mejor_precio,mejor_ruta]
    return resultado
        
  
###############################
#------CODIGO PRINCIPAL ------
###############################
N = int(input())
INI = int(input())
FIN = int(input())

PRECIOS = []
for c in range(0,N):
	ss = input().split(",")
	precio = []
	for s in ss:
		precio.append(int(s))
	PRECIOS.append(precio)
  
res = dijkstra(N, INI, FIN, PRECIOS)

print("Precio:", res[0])
print("Ruta:", res[1])
###############################
###############################

    

    