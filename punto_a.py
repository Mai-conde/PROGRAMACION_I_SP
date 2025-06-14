import random


'''A. Para el estado inicial: desarrollar una función que realice la creación dinámica de una matriz de 10 filas
por 10 columnas. En la misma se deberá incluir ceros para el agua y unos consecutivos para las naves.
Las naves pueden ser horizontales y/o verticales. Las naves deben ser generadas de la siguiente manera:
 Cuatro (4) submarinos de un (1) casillero
 Tres (3) destructores de dos (2) casilleros
 Dos (2) cruceros de tres (3) casilleros
 Un (1) acorazado de cuatro (4) casilleros'''

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial=0) -> list:
    '''  Documentación:
    Objetivo: Inicializar una matriz de n filas por m columnas.

    Parámetros:
        cant_filas (int): Cantidad de filas de la nueva matriz
        cant_columnas (int): Cantidad de columnas de la nueva matriz
    Retorno:
        list: retorna la matriz inicializada'''
    
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]

    return matriz

def mostrar_matriz(matriz:list) -> None:
    '''  Documentación:
    Objetivo: mostrar una matriz

    Parámetros:
        matriz (list): Matriz que quiere mostrarse'''
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = "  ")
        print("")

def verifica_posicion_barco(tablero, fila, columna, eleccion, orientacion):
    valido = True
    if orientacion == "horizontal":
        if columna > len(tablero[0]) - eleccion:
            valido = False
        for i in range(eleccion):
            if tablero[fila][columna + i] != 0:
                valido = False
    else:
        if fila > len(tablero) - eleccion:
            valido = False
        for i in range(eleccion):
            if tablero[fila + i][columna] != 0:
                valido = False
    return valido


def verifica_posicion_barco(tablero, fila, columna, tamaño, orientacion):
    if orientacion == "horizontal":
        if columna + tamaño > len(tablero[0]):
            return False
        for i in range(tamaño):
            if tablero[fila][columna + i] != 0:
                return False
    else:  # vertical
        if fila + tamaño > len(tablero):
            return False
        for i in range(tamaño):
            if tablero[fila + i][columna] != 0:
                return False
    return True

tablero = inicializar_matriz(10,10,0)
barcos = [1,1,1,1,2,2,2,3,3,4]

for j in range(len(barcos)):
    eleccion = random.choice(barcos) 
    barcos.remove(eleccion)
    orientacion = random.choice(["horizontal","vertical"])
    fila = random.randint(0,(len(tablero) - 1))
    columna = random.randint(0, len(tablero[0]) - 1)

    while verifica_posicion_barco(tablero,fila,columna,eleccion,orientacion) == False:
        fila = random.randint(0,(len(tablero) - 1))
        columna = random.randint(0, len(tablero[0]) - 1)   

    if orientacion == "horizontal":
        if columna > len(tablero[0]) - eleccion:
            columna = len(tablero[0]) - eleccion
        for i in range(eleccion):
            tablero[fila][columna + i] = 1
    else:
        if fila > len(tablero) - eleccion:
            fila = len(tablero) - eleccion
        for i in range(eleccion):
            tablero[fila + i][columna] = 1

    for choice in range(eleccion):
        for i in range(eleccion):
            if orientacion == "horizontal":
                tablero[fila][columna + i] = 1
            else:
                tablero[fila + i][columna] = 1
  
    

mostrar_matriz(tablero)
    


