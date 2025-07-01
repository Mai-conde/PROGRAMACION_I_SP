import pygame as pg
import sys
from src.scores import cargar_puntajes
from src.tablero_barcos import (inicializar_matriz,colocar_barcos,mostrar_matriz)
from src.const import *
from src.utils import (detectar_hover)
from src.seteo_de_juego import configurar_nivel
from src.ui import (pantalla_menu, pantalla_game, pantalla_levels,pantalla_nombre, pantalla_fin, pantalla_scores,actualizar_botones)
from src.recursos import cargar_imagenes, cargar_fuentes, cargar_sonidos
from src.eventos import (eventos_menu, eventos_levels, eventos_scores,eventos_game, eventos_nombre, eventos_fin)
pg.init()

# Configuración de pantalla
pantalla = pg.display.set_mode((ANCHO, ALTO))
pg.display.set_caption("Pantalla de Inicio")

fondo = cargar_imagenes()
fuente_normal, fuente_grande = cargar_fuentes()
sonido_barco, sonido_agua, sonido_hundido = cargar_sonidos()
pg.mixer.music.play(-1)
botones_niveles = {}
boton_hover = None
# Diccionario para guardar los rectángulos actuales
botones = {}
botones_juego = {}
botones_scores = {}
from src.const import posiciones_boton_scores, TAMAÑO_NORMAL, TAMAÑO_GRANDE

# Inicializar botones with tamaño normal
actualizar_botones(botones, posiciones_botones, TAMAÑO_NORMAL, TAMAÑO_GRANDE, boton_hover)
# Variables mutables como listas de un solo elemento
corriendo = [True]
estado = ["menu"]
puntaje = [0]
nombre_jugador = [""]
nivel_actual = ["Easy"]
puntajes_guardados = [None]
muteado = [False]

FILAS = 0
COLUMNAS = 0
TAM_CELDA = 0
barcos = []

while corriendo[0]:
    pos_mouse = pg.mouse.get_pos()
    boton_hover = detectar_hover(pos_mouse, botones)
    boton_hover_juego = detectar_hover(pos_mouse, botones_juego)
    boton_hover_scores = detectar_hover(pos_mouse, botones_scores)  # <-- Agrega esto

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pass

        elif estado[0] == "menu":
            eventos_menu(evento, botones, muteado, corriendo, estado, cargar_puntajes, puntajes_guardados)
            # Si el usuario hace clic en "Play", inicializa el juego aquí:
            if estado[0] == "play":
                config = configurar_nivel(nivel_actual[0])
                FILAS = config["FILAS"]
                COLUMNAS = config["COLUMNAS"]
                TAM_CELDA = config["TAM_CELDA"]
                barcos = config["barcos"]
                tablero = inicializar_matriz(FILAS, COLUMNAS, 0)
                disparos = inicializar_matriz(FILAS, COLUMNAS, 0)
                barcos_info = []
                colocar_barcos(tablero, barcos, barcos_info)
                print("Matriz de barcos:")
                mostrar_matriz(tablero)
                print("Barcos info:", barcos_info)
                puntaje[0] = 0
                nombre_jugador[0] = ""
                estado[0] = "nombre"

        elif estado[0] == "levels":
            eventos_levels(evento, botones_niveles, estado, nivel_actual)
            # Si el usuario elige un nivel, inicializa el juego aquí:
            if estado[0] == "nombre":
                config = configurar_nivel(nivel_actual[0])
                FILAS = config["FILAS"]
                COLUMNAS = config["COLUMNAS"]
                TAM_CELDA = config["TAM_CELDA"]
                barcos = config["barcos"]
                tablero = inicializar_matriz(FILAS, COLUMNAS, 0)
                disparos = inicializar_matriz(FILAS, COLUMNAS, 0)
                barcos_info = []
                colocar_barcos(tablero, barcos, barcos_info)
                print("Matriz de barcos:")
                mostrar_matriz(tablero)
                print("Barcos info:", barcos_info)

        elif estado[0] == "scores":
            eventos_scores(evento, botones_scores, estado)  

        elif estado[0] == "game":
            res = eventos_game(evento, botones_juego, estado, puntaje, nombre_jugador, tablero, disparos, barcos_info, sonido_barco, sonido_agua, sonido_hundido, FILAS, COLUMNAS, TAM_CELDA, ANCHO, ALTO)
            if res == "restart":
                tablero = inicializar_matriz(FILAS, COLUMNAS, 0)
                disparos = inicializar_matriz(FILAS, COLUMNAS, 0)
                barcos_info = []
                colocar_barcos(tablero, barcos, barcos_info)
                puntaje[0] = 0

        elif estado[0] == "nombre":
            eventos_nombre(evento, nombre_jugador, estado)
            
        elif estado[0] == "fin":
            res = eventos_fin(evento, botones_juego, estado, puntaje, nombre_jugador)
            if res == "restart":
                tablero = inicializar_matriz(FILAS, COLUMNAS, 0)
                disparos = inicializar_matriz(FILAS, COLUMNAS, 0)
                barcos_info = []
                colocar_barcos(tablero, barcos, barcos_info)
                puntaje[0] = 0
                estado[0] = "game"


    # Renderizado de pantallas según el estado
    if estado[0] == "menu":
        nivel_actual[0] = "Easy"
        pantalla_menu(
            pantalla, fondo, botones, fuente_normal, fuente_grande,
            boton_hover, muteado[0], posiciones_botones,
            TAMAÑO_NORMAL, TAMAÑO_GRANDE
        )
    elif estado[0] == "game":
        pantalla_game(
            pantalla, FILAS, COLUMNAS, TAM_CELDA, ANCHO, ALTO,
            disparos, puntaje[0], botones_juego, posiciones_botones_juego,
            fuente_normal, fuente_grande, boton_hover_juego
        )
    elif estado[0] == "levels":
        boton_hover_niveles = detectar_hover(pos_mouse, botones_niveles)
        pantalla_levels(
            pantalla, botones_niveles, posiciones_botones_niveles,
            fuente_normal, fuente_grande, boton_hover_niveles,
            TAMAÑO_NORMAL, TAMAÑO_GRANDE
        )
    elif estado[0] == "nombre":
        pantalla_nombre(pantalla, nombre_jugador[0])
    elif estado[0] == "fin":
        pantalla_fin(
        pantalla, puntaje[0], botones_juego, posiciones_botones_juego,
        fuente_normal, fuente_grande, boton_hover_juego,
        TAMAÑO_NORMAL_JUEGO, TAMAÑO_GRANDE_JUEGO
        )
    elif estado[0] == "scores":
        puntajes_guardados[0] = cargar_puntajes()
        # Actualiza y dibuja el botón Back con hover
        actualizar_botones(botones_scores, posiciones_boton_scores, TAMAÑO_NORMAL, TAMAÑO_GRANDE, boton_hover_scores)
        pantalla_scores(
            pantalla, puntajes_guardados[0], botones_scores, posiciones_boton_scores,
            fuente_normal, fuente_grande, boton_hover_scores
        )
        
    
        
    pg.display.flip()
pg.quit()
sys.exit()