from .const import *
def configurar_nivel(nivel: str) -> dict:
    """
    Configura los parámetros del juego según el nivel seleccionado.

    Args:
        nivel (str): Nivel de dificultad ("Easy", "Medium" o "Hard").

    Returns:
        dict: Diccionario con las claves "FILAS", "COLUMNAS", "TAM_CELDA" y "barcos".
    """
    if nivel == "Easy":
        FILAS = 10
        COLUMNAS = 10
        TAM_CELDA = 40
        barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    elif nivel == "Medium":
        FILAS = 20
        COLUMNAS = 20
        TAM_CELDA = 25  # Ajusta el tamaño para que quepa en pantalla
        barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]*2
    elif nivel == "Hard":
        FILAS = 40
        COLUMNAS = 40
        TAM_CELDA = 12
        barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]*3
    return{
        "FILAS": FILAS,
        "COLUMNAS": COLUMNAS,
        "TAM_CELDA": TAM_CELDA,
        "barcos": barcos
    }