import pygame as pg
from .const import BLANCO,GRIS,NEGRO,CELESTE,ANCHO,ALTO

def dibujar_botones(pantalla: pg.Surface, botones: dict, fuente_normal: pg.font.Font, fuente_grande: pg.font.Font, boton_hover: str = None, muteado: bool = False) -> None:
    """
    Dibuja los botones rectangulares con texto que crece y cambia si está muteado.

    Args:
        pantalla: Superficie de pygame donde se dibujan los botones.
        botones (dict): Diccionario con el texto del botón como clave y su rectángulo como valor.
        fuente_normal: Fuente para el texto normal.
        fuente_grande: Fuente para el texto cuando hay hover.
        boton_hover (str, opcional): Texto del botón actualmente bajo el mouse.
        muteado (bool, opcional): Indica si el sonido está muteado.
    """
    for texto, rect in botones.items():

        # Dibujar rectángulo
        color_del_boton= GRIS
        if texto == "Mute":
            if muteado:
                mostrar_texto = "Unmute"
                color_del_boton= (220,50,50)
            else:
                mostrar_texto = "Mute"
        else:
            mostrar_texto = texto
        if texto == boton_hover:
            fuente = fuente_grande
        else:
            fuente = fuente_normal
        pg.draw.rect(pantalla, color_del_boton, rect, border_radius= 25)
        if texto == "Mute" and muteado:
            pg.draw.line(
                pantalla, NEGRO,
                (rect.right - 10, rect.top + 10),
                (rect.left + 10, rect.bottom - 10),
                3
            )
        # Seleccionar fuente según hover
        texto_render = fuente.render(mostrar_texto, True, NEGRO)
        texto_rect = texto_render.get_rect(center=rect.center)
        pantalla.blit(texto_render, texto_rect)
        
def dibujar_botones_juego(pantalla: pg.Surface, botones_juego: dict, fuente_normal: pg.font.Font, fuente_grande: pg.font.Font, boton_hover: str = None) -> None:
    """
    Dibuja los botones del juego con efecto de hover.

    Args:
        pantalla: Superficie de pygame donde se dibujan los botones.
        botones_juego (dict): Diccionario de botones del juego.
        fuente_normal: Fuente para el texto normal.
        fuente_grande: Fuente para el texto cuando hay hover.
        boton_hover (str, opcional): Texto del botón actualmente bajo el mouse.
    """
    for texto, rect in botones_juego.items():
        color_del_boton= GRIS
        pg.draw.rect(pantalla, color_del_boton, rect, border_radius= 25)
        fuente = fuente_grande if texto == boton_hover else fuente_normal
        texto_render = fuente.render(texto, True, NEGRO)
        texto_rect = texto_render.get_rect(center=rect.center)
        pantalla.blit(texto_render, texto_rect)

def dibujar_botones_niveles(pantalla: pg.Surface, botones_niveles: dict, fuente_normal: pg.font.Font, fuente_grande: pg.font.Font, boton_hover: str = None) -> None:
    """
    Dibuja los botones para seleccionar el nivel de dificultad.

    Args:
        pantalla: Superficie de pygame donde se dibujan los botones.
        botones_niveles (dict): Diccionario de botones de niveles.
        fuente_normal: Fuente para el texto normal.
        fuente_grande: Fuente para el texto cuando hay hover.
        boton_hover (str, opcional): Texto del botón actualmente bajo el mouse.
    """
    for texto, rect in botones_niveles.items():
        pg.draw.rect(pantalla, GRIS, rect, border_radius=25)
        fuente = fuente_grande if texto == boton_hover else fuente_normal
        texto_render = fuente.render(texto, True, NEGRO)
        texto_rect = texto_render.get_rect(center=rect.center)
        pantalla.blit(texto_render, texto_rect)

def dibujar_botones_en_pantalla_juego(pantalla: pg.Surface, botones: dict, boton_restart: pg.Rect) -> None:
    """
    Dibuja el botón de reiniciar en la pantalla de juego.

    Args:
        pantalla: Superficie de pygame donde se dibuja el botón.
        botones (dict): Diccionario de botones.
        boton_restart: Rectángulo del botón de reinicio.
    """
    for texto, rect in botones.items():
        pg.draw.rect(pantalla, (0, 200, 0), boton_restart)
        fuente = pg.font.SysFont(None, 36)
        texto = fuente.render("Reiniciar", True, (255, 255, 255))
        texto_rect = texto.get_rect(center = boton_restart.center)
        pantalla.blit(texto, texto_rect)

def dibujar_matriz(pantalla: pg.Surface, filas: int, columnas: int, TAM_CELDA: int, Ancho: int, Alto: int) -> None:
    """
    Dibuja la cuadrícula del tablero de juego.

    Args:
        pantalla: Superficie de pygame donde se dibuja la matriz.
        filas (int): Cantidad de filas.
        columnas (int): Cantidad de columnas.
        TAM_CELDA (int): Tamaño de cada celda.
        Ancho (int): Ancho de la ventana.
        Alto (int): Alto de la ventana.
    """
    margen_x = (Ancho - (columnas * TAM_CELDA)) // 2
    margen_y = (Alto - (filas * TAM_CELDA)) // 2
    for x in range(columnas + 1):
        pg.draw.line(pantalla, NEGRO, (margen_x + x * TAM_CELDA, margen_y), (margen_x + x * TAM_CELDA, margen_y + filas * TAM_CELDA))
    for y in range(filas + 1):
        pg.draw.line(pantalla, NEGRO, (margen_x, margen_y + y * TAM_CELDA), (margen_x + columnas * TAM_CELDA, margen_y + y * TAM_CELDA))

def dibujar_cuadricula(pantalla: pg.Surface, Disparos: list, FILAS: int, COLUMNAS: int, TAM_CELDA: int, ANCHO: int, ALTO: int) -> None:
    """
    Dibuja los disparos realizados en el tablero (aciertos y agua).

    Args:
        pantalla: Superficie de pygame donde se dibujan los disparos.
        Disparos (list): Matriz con el estado de cada celda (0, 2, 3).
        FILAS (int): Cantidad de filas.
        COLUMNAS (int): Cantidad de columnas.
        TAM_CELDA (int): Tamaño de cada celda.
        ANCHO (int): Ancho de la ventana.
        ALTO (int): Alto de la ventana.
    """
    margen_x = (ANCHO - (COLUMNAS * TAM_CELDA)) // 2
    margen_y = (ALTO - (FILAS * TAM_CELDA)) // 2
    radio = max(2, TAM_CELDA // 2 - 2)  # Radio proporcional, mínimo 2
    for i in range(FILAS):
        for j in range(COLUMNAS):
            centro = (margen_x + j*TAM_CELDA + TAM_CELDA//2, margen_y + i*TAM_CELDA + TAM_CELDA//2)
            if Disparos[i][j] == 2:  # Tocado
                pg.draw.circle(pantalla, (255,0,0), centro, radio)
            elif Disparos[i][j] == 3:  # Agua
                pg.draw.circle(pantalla, (0,0,255), centro, radio)

def actualizar_botones(botones: dict, posiciones_botones: dict, TAMANO_NORMAL: tuple, TAMANO_GRANDE: tuple, boton_hover: str = None) -> None:
    """
    Actualiza el tamaño de los botones según si están en hover o no.

    Args:
        botones (dict): Diccionario de botones.
        posiciones_botones (dict): Posiciones de los botones.
        TAMANO_NORMAL (tuple): Tamaño normal del botón.
        TAMANO_GRANDE (tuple): Tamaño del botón en hover.
        boton_hover (str, opcional): Texto del botón actualmente bajo el mouse.
    """
    for texto, (x, y) in posiciones_botones.items():
        if texto == boton_hover:
            # Tamaño aumentado (centrado)
            botones[texto] = pg.Rect(
                x - (TAMANO_GRANDE[0] - TAMANO_NORMAL[0]) // 2,
                y - (TAMANO_GRANDE[1] - TAMANO_NORMAL[1]) // 2,
                TAMANO_GRANDE[0], TAMANO_GRANDE[1])
        else:
            # Tamaño normal
            botones[texto] = pg.Rect(x, y, TAMANO_NORMAL[0], TAMANO_NORMAL[1])
            
def actualizar_botones_juego(botones_juego: dict, posiciones_botones_juego: dict, TAMANO_NORMAL: tuple, TAMANO_GRANDE: tuple, boton_hover: str = None) -> None:
    """
    Actualiza el tamaño de los botones del juego según el hover.

    Args:
        botones_juego (dict): Diccionario de botones del juego.
        posiciones_botones_juego (dict): Posiciones de los botones del juego.
        TAMANO_NORMAL (tuple): Tamaño normal del botón.
        TAMANO_GRANDE (tuple): Tamaño del botón en hover.
        boton_hover (str, opcional): Texto del botón actualmente bajo el mouse.
    """
    for texto, pos in posiciones_botones_juego.items():
        x, y = pos
        if texto == boton_hover:
            # Tamaño aumentado (centrado)
            botones_juego[texto] = pg.Rect(
                x - (TAMANO_GRANDE[0] - TAMANO_NORMAL[0]) // 2,
                y - (TAMANO_GRANDE[1] - TAMANO_NORMAL[1]) // 2,
                TAMANO_GRANDE[0], TAMANO_GRANDE[1])
        else:
            # Tamaño normal
            botones_juego[texto] = pg.Rect(x, y, TAMANO_NORMAL[0], TAMANO_NORMAL[1])    

def actualizar_botones_niveles(botones_niveles: dict, posiciones_botones_niveles: dict, TAMANO_NORMAL: tuple, TAMANO_GRANDE: tuple, boton_hover: str = None) -> None:
    """
    Actualiza el tamaño de los botones de niveles según el hover.

    Args:
        botones_niveles (dict): Diccionario de botones de niveles.
        posiciones_botones_niveles (dict): Posiciones de los botones de niveles.
        TAMANO_NORMAL (tuple): Tamaño normal del botón.
        TAMANO_GRANDE (tuple): Tamaño del botón en hover.
        boton_hover (str, opcional): Texto del botón actualmente bajo el mouse.
    """
    for texto, (x, y) in posiciones_botones_niveles.items():
        if texto == boton_hover:
            botones_niveles[texto] = pg.Rect(
                x - (TAMANO_GRANDE[0] - TAMANO_NORMAL[0]) // 2,
                y - (TAMANO_GRANDE[1] - TAMANO_NORMAL[1]) // 2,
                TAMANO_GRANDE[0], TAMANO_GRANDE[1])
        else:
            botones_niveles[texto] = pg.Rect(x, y, TAMANO_NORMAL[0], TAMANO_NORMAL[1])
            
def pantalla_menu(pantalla: pg.Surface, fondo: pg.Surface, botones: dict, fuente_normal: pg.font.Font, fuente_grande: pg.font.Font, boton_hover: str, muteado: bool, posiciones_botones: dict, TAMANO_NORMAL: tuple, TAMANO_GRANDE: tuple) -> None:
    """
    Dibuja la pantalla del menú principal.

    Args:
        pantalla: Superficie de pygame donde se dibuja el menú.
        fondo: Imagen de fondo.
        botones (dict): Diccionario de botones.
        fuente_normal: Fuente para el texto normal.
        fuente_grande: Fuente para el texto en hover.
        boton_hover (str): Texto del botón actualmente bajo el mouse.
        muteado (bool): Indica si el sonido está muteado.
        posiciones_botones (dict): Posiciones de los botones.
        TAMANO_NORMAL (tuple): Tamaño normal del botón.
        TAMANO_GRANDE (tuple): Tamaño del botón en hover.
    """
    pantalla.blit(fondo, (0, 0))
    actualizar_botones(botones, posiciones_botones, TAMANO_NORMAL, TAMANO_GRANDE, boton_hover)
    dibujar_botones(pantalla, botones, fuente_normal, fuente_grande, boton_hover, muteado)

def pantalla_game(pantalla: pg.Surface, FILAS: int, COLUMNAS: int, TAM_CELDA: int, ANCHO: int, ALTO: int, disparos: list, puntaje: int, botones_juego: dict, posiciones_botones_juego: dict, fuente_normal: pg.font.Font, fuente_grande: pg.font.Font, boton_hover_juego: str) -> None:
    """
    Dibuja la pantalla principal del juego (tablero, disparos, puntaje y botones).

    Args:
        pantalla: Superficie de pygame donde se dibuja el juego.
        FILAS (int): Cantidad de filas.
        COLUMNAS (int): Cantidad de columnas.
        TAM_CELDA (int): Tamaño de cada celda.
        ANCHO (int): Ancho de la ventana.
        ALTO (int): Alto de la ventana.
        disparos (list): Matriz de disparos.
        puntaje (int): Puntaje actual.
        botones_juego (dict): Diccionario de botones del juego.
        posiciones_botones_juego (dict): Posiciones de los botones del juego.
        fuente_normal: Fuente para el texto normal.
        fuente_grande: Fuente para el texto en hover.
        boton_hover_juego (str): Texto del botón actualmente bajo el mouse.
    """
    pantalla.fill(CELESTE)
    dibujar_matriz(pantalla, FILAS, COLUMNAS, TAM_CELDA, ANCHO, ALTO)
    dibujar_cuadricula(pantalla, disparos, FILAS, COLUMNAS, TAM_CELDA, ANCHO, ALTO)
    rect_score = pg.Rect(300, 555, 250, 40)
    pg.draw.rect(pantalla, GRIS, rect_score)
    fuente_score = pg.font.Font("static/font/ka1.ttf", 30)
    texto_score = fuente_score.render(f"Score: {puntaje}", True, NEGRO)
    texto_rect = texto_score.get_rect(center=rect_score.center)
    pantalla.blit(texto_score, texto_rect)
    TAMANO_NORMAL = (120, 40)
    TAMANO_GRANDE = (150, 55)
    actualizar_botones_juego(botones_juego, posiciones_botones_juego, TAMANO_NORMAL, TAMANO_GRANDE, boton_hover_juego)
    dibujar_botones_juego(pantalla, botones_juego, fuente_normal, fuente_grande, boton_hover_juego)

def pantalla_levels(pantalla: pg.Surface, botones_niveles: dict, posiciones_botones_niveles: dict, fuente_normal: pg.font.Font, fuente_grande: pg.font.Font, boton_hover_niveles: str, TAMANO_NORMAL: tuple, TAMANO_GRANDE: tuple) -> None:
    """
    Dibuja la pantalla de selección de nivel.

    Args:
        pantalla: Superficie de pygame donde se dibuja la pantalla de niveles.
        botones_niveles (dict): Diccionario de botones para cada nivel.
        posiciones_botones_niveles (dict): Posiciones de los botones de niveles.
        fuente_normal: Fuente para el texto normal.
        fuente_grande: Fuente para el texto cuando hay hover.
        boton_hover_niveles (str, opcional): Texto del botón actualmente bajo el mouse.
        TAMANO_NORMAL (tuple): Tamaño normal del botón.
        TAMANO_GRANDE (tuple): Tamaño del botón en hover.
    """
    pantalla.fill(CELESTE)
    actualizar_botones_niveles(botones_niveles, posiciones_botones_niveles, TAMANO_NORMAL, TAMANO_GRANDE, boton_hover_niveles)
    dibujar_botones_niveles(pantalla, botones_niveles, fuente_normal, fuente_grande, boton_hover_niveles)

def pantalla_nombre(pantalla: pg.Surface, nombre_jugador: str) -> None:
    """
    Dibuja la pantalla para ingresar el nombre del jugador.

    Args:
        pantalla: Superficie de pygame donde se dibuja la pantalla.
        nombre_jugador (str): Nombre ingresado por el usuario (se muestra en el campo de texto).
    """
    pantalla.fill(CELESTE)
    fuente = pg.font.Font("static/font/ka1.ttf", 32)
    texto = fuente.render("Ingresa tu nombre:", True, NEGRO)
    pantalla.blit(texto, (220, 200))
    rect_input = pg.Rect(220, 260, 360, 50)
    pg.draw.rect(pantalla, BLANCO, rect_input, border_radius=10)
    fuente_input = pg.font.Font("static/font/ka1.ttf", 28)
    texto_input = fuente_input.render(nombre_jugador, True, NEGRO)
    pantalla.blit(texto_input, (rect_input.x + 10, rect_input.y + 10))
    fuente_inst = pg.font.Font("static/font/ka1.ttf", 20)
    texto_inst = fuente_inst.render("Presiona Enter para continuar", True, NEGRO)
    pantalla.blit(texto_inst, (rect_input.x, rect_input.y + 60))

def pantalla_fin(pantalla: pg.Surface, puntaje: int, botones_juego: dict, posiciones_botones_juego: dict, fuente_normal: pg.font.Font, fuente_grande: pg.font.Font, boton_hover_juego: str, TAMANO_NORMAL: tuple, TAMANO_GRANDE: tuple) -> None:
    """
    Dibuja la pantalla de fin de partida, mostrando el puntaje final y los botones de acción.

    Args:
        pantalla (pg.Surface): Superficie de pygame donde se dibuja la pantalla.
        puntaje (int): Puntaje final del jugador.
        botones_juego (dict): Diccionario de botones del juego.
        posiciones_botones_juego (dict): Posiciones de los botones del juego.
        fuente_normal (pg.font.Font): Fuente para el texto normal.
        fuente_grande (pg.font.Font): Fuente para el texto en hover.
        boton_hover_juego (str): Texto del botón actualmente bajo el mouse.
        TAMANO_NORMAL (tuple): Tamaño normal del botón.
        TAMANO_GRANDE (tuple): Tamaño del botón en hover.
    """
    pantalla.fill(CELESTE)
    rect_win = pg.Rect(150, 200, 600, 100)
    pg.draw.rect(pantalla, (255, 255, 0), rect_win, border_radius=20)
    fuente_win = pg.font.Font("static/font/ka1.ttf", 35)
    texto_win = fuente_win.render(f"You Win! Score: {puntaje}", True, NEGRO)
    texto_rect = texto_win.get_rect(center=rect_win.center)
    pantalla.blit(texto_win, texto_rect)
    actualizar_botones_juego(botones_juego, posiciones_botones_juego, TAMANO_NORMAL, TAMANO_GRANDE, boton_hover_juego)
    dibujar_botones_juego(pantalla, botones_juego, fuente_normal, fuente_grande, boton_hover_juego)

def pantalla_scores(pantalla: pg.Surface, puntajes_guardados: list) -> None:
    """
    Dibuja la pantalla de puntajes guardados.

    Args:
        pantalla: Superficie de pygame donde se dibuja la pantalla.
        puntajes_guardados (list): Lista de diccionarios con los puntajes y nombres.
    """
    pantalla.fill(CELESTE)
    fuente_titulo = pg.font.Font("static/font/ka1.ttf", 36)
    fuente_score = pg.font.Font("static/font/ka1.ttf", 24)
    texto = fuente_titulo.render("Scores", True, NEGRO)
    pantalla.blit(texto, (320, 50))
    y = 120
    puntajes_ordenados = puntajes_guardados[:]
    n = len(puntajes_ordenados)
    for i in range(n):
        for j in range(i + 1, n):
            if puntajes_ordenados[j]["puntaje"] > puntajes_ordenados[i]["puntaje"]:
                temp = puntajes_ordenados[i]
                puntajes_ordenados[i] = puntajes_ordenados[j]
                puntajes_ordenados[j] = temp
    for entry in puntajes_ordenados[:10]:
        texto_score = fuente_score.render(f'{entry["nombre"]}: {entry["puntaje"]}', True, NEGRO)
        pantalla.blit(texto_score, (300, y))
        y += 35
    rect_back = pg.Rect(50, 30, 120, 40)
    pg.draw.rect(pantalla, GRIS, rect_back, border_radius=15)
    fuente_back = pg.font.Font("static/font/ka1.ttf", 22)
    texto_back = fuente_back.render("Back", True, NEGRO)
    pantalla.blit(texto_back, (rect_back.x + 30, rect_back.y + 8))