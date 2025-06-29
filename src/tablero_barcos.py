import random

def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_inicial=0) -> list:
    """
    Inicializa una matriz de n filas por m columnas con un valor inicial.

    Args:
        cant_filas (int): Cantidad de filas de la nueva matriz.
        cant_columnas (int): Cantidad de columnas de la nueva matriz.
        valor_inicial (opcional): Valor con el que se inicializa cada celda (por defecto 0).

    Returns:
        list: Matriz inicializada.
    """
    
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]

    return matriz

def mostrar_matriz(matriz: list) -> None:
    """
    Muestra una matriz por consola.

    Args:
        matriz (list): Matriz que se quiere mostrar.
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = "  ")
        print("")

def verifica_posicion_barco(tablero: list, fila: int, columna: int, tamaño: int, orientacion: str) -> bool:
    """
    Verifica si se puede colocar un barco en la posición y orientación dadas.

    Args:
        tablero (list): Matriz del tablero.
        fila (int): Fila inicial.
        columna (int): Columna inicial.
        tamaño (int): Tamaño del barco.
        orientacion (str): "horizontal" o "vertical".

    Returns:
        bool: True si la posición es válida, False en caso contrario.
    """
    total_filas = len(tablero)
    total_columnas = len(tablero[0])
    posiciones_barco = []
    es_valido = True

    for i in range(tamaño):
        if orientacion == "horizontal":
            fila_actual, columna_actual = fila, columna + i
        else:
            fila_actual, columna_actual = fila + i, columna
        # Si está fuera del tablero, marca como inválido
        if fila_actual < 0 or fila_actual >= total_filas or columna_actual < 0 or columna_actual >= total_columnas:
            es_valido = False
        else:
            posiciones_barco.append((fila_actual, columna_actual))

    for fila_barco, columna_barco in posiciones_barco:
        for delta_fila in [-1, 0, 1]:
            for delta_columna in [-1, 0, 1]:
                fila_vecina, columna_vecina = fila_barco + delta_fila, columna_barco + delta_columna
                if 0 <= fila_vecina < total_filas and 0 <= columna_vecina < total_columnas:
                    if tablero[fila_vecina][columna_vecina] != 0 and (fila_vecina, columna_vecina) not in posiciones_barco:
                        es_valido = False
        if tablero[fila_barco][columna_barco] != 0:
            es_valido = False

    return es_valido

def colocar_barcos(tablero: list, lista_tamaños: list, barcos_info: list) -> list:
    """
    Coloca barcos aleatoriamente en el tablero según los tamaños dados.

    Args:
        tablero (list): Matriz del tablero.
        lista_tamaños (list): Lista con los tamaños de los barcos.
        barcos_info (list): Lista donde se guardará la información de los barcos.

    Returns:
        list: Lista con la información de los barcos colocados.
    """
    barcos_info.clear()  # Limpia la lista antes de colocar nuevos barcos
    for tamaño in lista_tamaños:
        colocado = False
        while not colocado:
            orientacion = random.choice(["horizontal", "vertical"])
            fila = random.randint(0, len(tablero) - 1)
            columna = random.randint(0, len(tablero[0]) - 1)
            if verifica_posicion_barco(tablero, fila, columna, tamaño, orientacion):
                posiciones = []
                for i in range(tamaño):
                    if orientacion == "horizontal":
                        tablero[fila][columna + i] = 1
                        posiciones.append((fila, columna + i))
                    else:
                        tablero[fila + i][columna] = 1
                        posiciones.append((fila + i, columna))
                barcos_info.append({"tamaño": tamaño, "posiciones": posiciones})
                colocado = True
    return barcos_info

def es_barco_hundido(barcos_info: list, disparos: list, fila: int, col: int) -> bool:
    """
    Verifica si el barco al que pertenece la celda (fila, col) está hundido.

    Args:
        barcos_info (list): Lista con la información de los barcos.
        disparos (list): Matriz de disparos realizados.
        fila (int): Fila del disparo.
        col (int): Columna del disparo.

    Returns:
        bool: True si el barco está hundido, False en caso contrario.
    """
    hundido = False
    for barco in barcos_info:
        if (fila, col) in barco["posiciones"]:
            hundido = True
            for filas, columnas in barco["posiciones"]:
                if disparos[filas][columnas] != 2:
                    hundido = False
                    break
    return hundido

def todos_barcos_hundidos(barcos_info: list, disparos: list) -> bool:
    """
    Verifica si todos los barcos han sido hundidos.

    Args:
        barcos_info (list): Lista con la información de los barcos.
        disparos (list): Matriz de disparos realizados.

    Returns:
        bool: True si todos los barcos están hundidos, False en caso contrario.
    """
    hundidos = True
    for barco in barcos_info:
        for filas, columnas in barco["posiciones"]:
            if disparos[filas][columnas] != 2:
                hundidos = False
    return hundidos



