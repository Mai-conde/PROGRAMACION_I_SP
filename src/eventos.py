import pygame as pg
from src.utils import detectar_click, obtener_celda_clic
from src.tablero_barcos import es_barco_hundido, todos_barcos_hundidos, obtener_barco_hundido
from src.scores import guardar_puntaje

def eventos_menu(evento: pg.event.Event, botones: dict, muteado: list, corriendo: list, estado: list, cargar_puntajes: callable, puntajes_guardados: list) -> None:
    """
    Maneja los eventos del menú principal.

    Args:
        evento: Evento de pygame.
        botones (dict): Diccionario de botones.
        muteado (list): Estado de muteo [bool].
        corriendo (list): Estado de ejecución [bool].
        estado (list): Estado actual del juego [str].
        cargar_puntajes (func): Función para cargar puntajes.
        puntajes_guardados (list): Lista para almacenar puntajes cargados.
    """
    if evento.type == pg.MOUSEBUTTONDOWN:
        clic = detectar_click(evento.pos, botones)
        if clic == "Exit":
            corriendo[0] = False
        elif clic == "Play":
            estado[0] = "play"
        elif clic == "Level":
            estado[0] = "levels"
        elif clic == "Scores":
            puntajes_guardados[0] = cargar_puntajes()
            estado[0] = "scores"
        elif clic == "Mute" or clic == "Unmute":
            muteado[0] = not muteado[0]
            if muteado[0]:
                pg.mixer.music.pause()
            else:
                pg.mixer.music.unpause()

def eventos_levels(evento: pg.event.Event, botones_niveles: dict, estado: list, nivel_actual: list) -> None:
    """
    Maneja los eventos de la pantalla de selección de nivel.

    Args:
        evento: Evento de pygame.
        botones_niveles (dict): Diccionario de botones de niveles.
        estado (list): Estado actual del juego [str].
        nivel_actual (list): Nivel seleccionado [str].
    """
    if evento.type == pg.MOUSEBUTTONDOWN:
        clic = detectar_click(evento.pos, botones_niveles)
        if clic == "Back":
            estado[0] = "menu"
        elif clic in ["Easy", "Medium", "Hard"]:
            nivel_actual[0] = clic
            estado[0] = "nombre"

def eventos_scores(evento: pg.event.Event, botones_scores: dict, estado: list) -> None:
    """
    Maneja los eventos de la pantalla de puntajes.

    Args:
        evento: Evento de pygame.
        botones_scores (dict): Diccionario de botones de scores.
        estado (list): Estado actual del juego [str].
    """
    if evento.type == pg.MOUSEBUTTONDOWN:
        clic = detectar_click(evento.pos, botones_scores)
        if clic == "Back":
            estado[0] = "menu"

def eventos_game(evento: pg.event.Event, botones_juego: dict, estado: list, puntaje: list, nombre_jugador: list, tablero: list, disparos: list, barcos_info: list, sonido_barco, sonido_agua, sonido_hundido, FILAS: int, COLUMNAS: int, TAM_CELDA: int, ANCHO: int, ALTO: int) -> None:
    """
    Maneja los eventos de la pantalla de juego.

    Args:
        evento: Evento de pygame.
        botones_juego (dict): Diccionario de botones del juego.
        estado (list): Estado actual del juego [str].
        puntaje (list): Puntaje actual [int].
        nombre_jugador (list): Nombre del jugador [str].
        tablero (list): Matriz del tablero.
        disparos (list): Matriz de disparos.
        barcos_info (list): Información de los barcos.
        sonido_barco: Sonido de impacto en barco.
        sonido_agua: Sonido de impacto en agua.
        sonido_hundido: Sonido de barco hundido.
        FILAS (int): Cantidad de filas.
        COLUMNAS (int): Cantidad de columnas.
        TAM_CELDA (int): Tamaño de celda.
        ANCHO (int): Ancho de la ventana.
        ALTO (int): Alto de la ventana.
    """

    if evento.type == pg.MOUSEBUTTONDOWN:
        clic = detectar_click(evento.pos, botones_juego)
        if clic == "Restart":
            estado[0] = "game"          
        elif clic == "Back":
            estado[0] = "menu"
            puntaje[0] = 0
            nombre_jugador[0] = ""
        fila_col = obtener_celda_clic(evento.pos[0], evento.pos[1], ANCHO, ALTO, COLUMNAS, FILAS, TAM_CELDA)
        if fila_col:
            f, c = fila_col
            if f is not None and c is not None:
                if tablero[f][c] == 1 and disparos[f][c] == 0:
                    sonido_barco.play()
                    disparos[f][c] = 2
                    puntaje[0] += 5  # Suma puntos por acertar
                    if es_barco_hundido(barcos_info, disparos, f, c):
                        sonido_hundido.play()
                        puntaje[0] += 10
                        barco = obtener_barco_hundido(barcos_info, f, c)
                        if barco:
                            print("¡Barco hundido!", barco["posiciones"])
                        if todos_barcos_hundidos(barcos_info, disparos):
                            guardar_puntaje(nombre_jugador[0], puntaje[0])
                            estado[0] = "fin"
                elif tablero[f][c] == 0 and disparos[f][c] == 0:
                    sonido_agua.play()
                    puntaje[0] -= 1
                    disparos[f][c] = 3


def eventos_nombre(evento: pg.event.Event, nombre_jugador: list, estado: list) -> None:
    """
    Maneja los eventos de la pantalla de ingreso de nombre.

    Args:
        evento: Evento de pygame.
        nombre_jugador (list): Nombre del jugador [str].
        estado (list): Estado actual del juego [str].
    """
    if evento.type == pg.KEYDOWN:
        if evento.key == pg.K_RETURN:
            if nombre_jugador[0].strip() != "":
                estado[0] = "game"
        elif evento.key == pg.K_BACKSPACE:
            nombre_jugador[0] = nombre_jugador[0][:-1]
        else:
            if len(nombre_jugador[0]) < 15 and evento.unicode.isprintable():
                nombre_jugador[0] += evento.unicode

def eventos_fin(evento: pg.event.Event, botones_juego: dict, estado: list, puntaje: list, nombre_jugador: list) -> None:
    """
    Maneja los eventos de la pantalla de fin de partida.

    Args:
        evento: Evento de pygame.
        botones_juego (dict): Diccionario de botones del juego.
        estado (list): Estado actual del juego [str].
        puntaje (list): Puntaje actual [int].
        nombre_jugador (list): Nombre del jugador [str].
    """
    if evento.type == pg.MOUSEBUTTONDOWN:
        clic = detectar_click(evento.pos, botones_juego)
        if clic == "Back":
            estado[0] = "menu"
            puntaje[0] = 0
            nombre_jugador[0] = ""
        elif clic == "Restart":
            return "restart"

