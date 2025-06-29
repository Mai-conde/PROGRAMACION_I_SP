from .const import BLANCO, GRIS, NEGRO, CELESTE, ANCHO, ALTO
import pygame as pg

def detectar_hover(pos: tuple, botones: dict) -> str | None:
    """
    Detecta qué botón está bajo el cursor del mouse.

    Args:
        pos (tuple): Posición (x, y) del mouse.
        botones (dict): Diccionario con el texto del botón como clave y su rectángulo como valor.

    Returns:
        str or None: El texto del botón sobre el que está el mouse, o None si no está sobre ningún botón.
    """
    resultado = None
    for texto, rect in botones.items():
        if rect.collidepoint(pos):
            resultado = texto
            break
    return resultado

def detectar_click(pos: tuple, botones: dict) -> str | None:
    """
    Detecta si el usuario hizo clic sobre algún botón.

    Args:
        pos (tuple): Posición (x, y) del mouse al hacer clic.
        botones (dict): Diccionario con el texto del botón como clave y su rectángulo como valor.

    Returns:
        str or None: El texto del botón sobre el que se hizo clic, o None si no se hizo clic sobre ningún botón.
    """
    resultado = None
    for texto, rect in botones.items():
        if rect.collidepoint(pos):
            resultado = texto
            break
    return resultado

def obtener_celda_clic(
    x: int, y: int, ANCHO: int, ALTO: int, COLUMNAS: int, FILAS: int, TAM_CELDA: int) -> list:
    """
    Convierte la posición del mouse en la celda correspondiente del tablero.

    Args:
        x (int): Coordenada x del mouse.
        y (int): Coordenada y del mouse.
        ANCHO (int): Ancho de la ventana.
        ALTO (int): Alto de la ventana.
        COLUMNAS (int): Cantidad de columnas del tablero.
        FILAS (int): Cantidad de filas del tablero.
        TAM_CELDA (int): Tamaño de cada celda.

    Returns:
        list: [fila, columna] si el clic está dentro del tablero, lista vacía si está fuera.
    """
    margen_x = (ANCHO - (COLUMNAS * TAM_CELDA)) // 2
    margen_y = (ALTO - (FILAS * TAM_CELDA)) // 2
    resultado = []
    if margen_x <= x < margen_x + COLUMNAS * TAM_CELDA and margen_y <= y < margen_y + FILAS * TAM_CELDA:
        col = (x - margen_x) // TAM_CELDA
        fila = (y - margen_y) // TAM_CELDA
        resultado = [int(fila), int(col)]
    return resultado