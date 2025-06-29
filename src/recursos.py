import pygame as pg
from src.const import ANCHO, ALTO


def cargar_imagenes()-> pg.Surface:
    """
    Carga y escala la imagen de fondo del juego.

    Returns:
        pg.Surface: Imagen de fondo escalada al tamaño de la ventana.
    """
    fondo = pg.image.load("static/img/SEA_BATTLE.PNG")
    fondo = pg.transform.scale(fondo, (ANCHO, ALTO))
    return fondo

def cargar_fuentes()-> tuple:
    """
    Carga las fuentes utilizadas en el juego.

    Returns:
        tuple: Fuente normal y fuente grande.
    """
    fuente_normal = pg.font.Font("static/font/ka1.ttf", 18)
    fuente_grande = pg.font.Font("static/font/ka1.ttf", 25)
    return fuente_normal, fuente_grande

def cargar_sonidos()-> tuple:
    """
    Carga los sonidos utilizados en el juego.

    Returns:
        tuple: Sonido de impacto en barco, sonido de agua y sonido de barco hundido.
    """
    pg.mixer.music.load("static/sound/Piratas del  caribe  cancion completa - android juegos.mp3")
    pg.mixer.music.set_volume(0.1)
    sonido_barco = pg.mixer.Sound("static/sound/impacto_barco.mp3")
    sonido_barco.set_volume(0.3)
    sonido_agua = pg.mixer.Sound("static/sound/impacto_agua.mp3")
    sonido_agua.set_volume(0.5)
    sonido_hundido = pg.mixer.Sound("static/sound/barco_hundido.mp3")
    sonido_hundido.set_volume(1.0)
    return sonido_barco, sonido_agua, sonido_hundido