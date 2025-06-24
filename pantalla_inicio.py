import pygame as pg
import sys
import punto_a

# Inicializar Pygame
pg.init()

# Configuración de pantalla
ANCHO = 800
ALTO = 600
pantalla = pg.display.set_mode((ANCHO, ALTO))
pg.display.set_caption("Pantalla de Inicio")

# Colores
BLANCO = (255, 255, 255) 
GRIS = (200, 200, 200)
NEGRO = (0, 0, 0)
CELESTE= (135, 206, 235)
# Fuentes
tamano_fuente_normal = 18
tamano_fuente_grande = 25  # Texto más grande para el hover
fuente_normal = pg.font.Font("ka1.ttf", tamano_fuente_normal)
fuente_grande = pg.font.Font("ka1.ttf", tamano_fuente_grande)

# Música de fondo
pg.mixer.music.load("Piratas del  caribe  cancion completa - android juegos.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.1)
#impactos barcos
sonido_barco= pg.mixer.Sound("impacto_barco.mp3")
sonido_barco.set_volume(0.3)
sonido_agua= pg.mixer.Sound("impacto_agua.mp3")
sonido_agua.set_volume(0.5)
sonido_hundido= pg.mixer.Sound("barco_hundido.mp3")
sonido_hundido.set_volume(1.0)
# Cargar imagen de fondo
fondo = pg.image.load("SEA_BATTLE.PNG")
fondo = pg.transform.scale(fondo, (ANCHO, ALTO))

# Tamaños de botones (rectangulares)
TAMANO_NORMAL = (200, 50)
TAMANO_GRANDE = (250, 70)  # Tamaño aumentado
FILAS=10
COLUMNAS=10
TAM_CELDA=40
nivel_actual = "Easy"

# Posiciones originales de los botones
posiciones_botones = {
    "Level": (300, 150),
    "Play": (300, 230),
    "Scores": (300, 310),
    "Exit": (300, 390),
    "Mute" : (50, 30),
}
posiciones_botones_niveles = {
    "Easy": (300, 150),
    "Medium": (300, 230),
    "Hard": (300, 310),
    "Back": (50, 30)
}
botones_niveles = {}

posiciones_botones_juego = {
    "Restart" : (15,10) ,
    "Back" : (670, 10),
}

# Diccionario para guardar los rectángulos actuales
botones = {}
botones_juego = {}

def dibujar_matriz(filas, columnas, TAM_CELDA,Ancho, Alto):
    margen_x = (Ancho - (columnas * TAM_CELDA)) // 2
    margen_y = (Alto - (filas * TAM_CELDA)) // 2
    for x in range(columnas + 1):
        pg.draw.line(pantalla, NEGRO, (margen_x + x * TAM_CELDA, margen_y), (margen_x + x * TAM_CELDA, margen_y + filas * TAM_CELDA))
    for y in range(filas + 1):
        pg.draw.line(pantalla, NEGRO, (margen_x, margen_y + y * TAM_CELDA), (margen_x + columnas * TAM_CELDA, margen_y + y * TAM_CELDA))

def actualizar_botones(boton_hover=None):
    """objetivo: Actualizar el tamaño de los botones según el hover
    
    parametros:
        botom_hover (opcional)
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

def actualizar_botones_juego(boton_hover=None):
    """Actualiza el tamaño de los botones según el hover"""
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

def actualizar_botones_niveles(boton_hover=None):
    for texto, (x, y) in posiciones_botones_niveles.items():
        if texto == boton_hover:
            botones_niveles[texto] = pg.Rect(
                x - (TAMANO_GRANDE[0] - TAMANO_NORMAL[0]) // 2,
                y - (TAMANO_GRANDE[1] - TAMANO_NORMAL[1]) // 2,
                TAMANO_GRANDE[0], TAMANO_GRANDE[1])
        else:
            botones_niveles[texto] = pg.Rect(x, y, TAMANO_NORMAL[0], TAMANO_NORMAL[1])

def dibujar_botones(boton_hover=None):
    """Dibuja los botones rectangulares con texto que crece"""
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

def dibujar_botones_juego(boton_hover=None):
    """Dibuja los botones rectangulares con texto que crece"""
    for texto, rect in botones_juego.items():
        color_del_boton= GRIS
        pg.draw.rect(pantalla, color_del_boton, rect, border_radius= 25)
        fuente = fuente_grande if texto == boton_hover else fuente_normal
        texto_render = fuente.render(texto, True, NEGRO)
        texto_rect = texto_render.get_rect(center=rect.center)
        pantalla.blit(texto_render, texto_rect)

def dibujar_botones_niveles(boton_hover=None):
    for texto, rect in botones_niveles.items():
        pg.draw.rect(pantalla, GRIS, rect, border_radius=25)
        fuente = fuente_grande if texto == boton_hover else fuente_normal
        texto_render = fuente.render(texto, True, NEGRO)
        texto_rect = texto_render.get_rect(center=rect.center)
        pantalla.blit(texto_render, texto_rect)

def es_barco_hundido(barcos_info, disparos, fila, col):
    hundido = False
    for barco in barcos_info:
        if (fila, col) in barco["posiciones"]:
            hundido = True
            for f, c in barco["posiciones"]:
                if disparos[f][c] != 2:
                    hundido = False
                    break
    return hundido

def detectar_hover(pos):
    """Detecta qué botón está bajo el cursor"""
    resultado = None
    for texto, rect in botones.items():
        if rect.collidepoint(pos):
            resultado = texto
            break
    return resultado

def detectar_click(pos):
    resultado = None
    for texto, rect in botones.items():
        if rect.collidepoint(pos):
            resultado = texto
            break
    return resultado

def detectar_hover_juego(pos):
    """Detecta qué botón está bajo el cursor"""
    resultado = None
    for texto, rect in botones_juego.items():
        if rect.collidepoint(pos):
            resultado = texto
            break
    return resultado

def detectar_click_juego(pos):
    resultado = None
    for texto, rect in botones_juego.items():
        if rect.collidepoint(pos):
            resultado = texto
            break
    return resultado

def detectar_hover_niveles(pos):
    resultado = None
    for texto, rect in botones_niveles.items():
        if rect.collidepoint(pos):
            resultado= texto
            break
    return resultado

def detectar_click_niveles(pos):
    resultado = None
    for texto, rect in botones_niveles.items():
        if rect.collidepoint(pos):
            resultado = texto
            break
    return resultado

def obtener_celda_clic(x, y):
    margen_x = (ANCHO - (COLUMNAS * TAM_CELDA)) // 2
    margen_y = (ALTO - (FILAS * TAM_CELDA)) // 2
    resultado = []
    if margen_x <= x < margen_x + COLUMNAS * TAM_CELDA and margen_y <= y < margen_y + FILAS * TAM_CELDA:
        col = (x - margen_x) // TAM_CELDA
        fila = (y - margen_y) // TAM_CELDA
        resultado = [int(fila), int(col)]
    return resultado

def dibujar_cuadricula():
    margen_x = (ANCHO - (COLUMNAS * TAM_CELDA)) // 2
    margen_y = (ALTO - (FILAS * TAM_CELDA)) // 2
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if disparos[i][j] == 2:  # Tocado
                pg.draw.circle(pantalla, (255,0,0), (margen_x + j*TAM_CELDA + TAM_CELDA//2, margen_y + i*TAM_CELDA + TAM_CELDA//2), 10)
            elif disparos[i][j] == 3:  # Agua
                pg.draw.circle(pantalla, (0,0,255), (margen_x + j*TAM_CELDA + TAM_CELDA//2, margen_y + i*TAM_CELDA + TAM_CELDA//2), 10)


def dibujar_botones_en_pantalla_juego(boton_restart, boton_back):
    for texto, rect in botones.items():
        pg.draw.rect(pantalla, (0, 200, 0), boton_restart)
        fuente = pg.font.SysFont(None, 36)
        texto = fuente.render("Reiniciar", True, (255, 255, 255))
        texto_rect = texto.get_rect(center = boton_restart.center)
        pantalla.blit(texto, texto_rect)

def todos_barcos_hundidos(barcos_info, disparos):
    hundidos = True
    for barco in barcos_info:
        for f, c in barco["posiciones"]:
            if disparos[f][c] != 2:
                hundidos = False
    return hundidos

# Inicializar botones con tamaño normal
actualizar_botones()
muteado = False
# Bucle principal
corriendo = True
estado="menu"
puntaje = 0
boton_restart = pg.Rect(500, 800, 150, 50)  

while corriendo:
    pos_mouse = pg.mouse.get_pos()
    boton_hover = detectar_hover(pos_mouse)
    boton_hover_juego = detectar_hover_juego(pos_mouse)
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
        elif evento.type == pg.MOUSEBUTTONDOWN and estado == "menu":
            clic = detectar_click(evento.pos)
            if clic == "Exit":
                corriendo = False
            elif clic == "Play":
                estado= "levels"
                estado= "game"
            elif clic == "Level": 
                estado = "levels"
            elif clic == "Scores":
                print("Showing scores...")  
            elif clic == "Mute" or clic == "Unmute":
                muteado = not muteado
                if muteado:
                    pg.mixer.music.pause()
                    print("Music muted")
                else:
                    pg.mixer.music.unpause()
                    print("Music unmuted")
        elif evento.type == pg.MOUSEBUTTONDOWN and estado == "levels":
            clic = detectar_click_niveles(evento.pos)
            if clic == "Back":
                estado = "menu"
            elif clic == "Easy":
                nivel_actual = "Easy"
                FILAS = 10
                COLUMNAS = 10
                TAM_CELDA = 40
                tablero = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                disparos = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                barcos = [1]*4 + [2]*3 + [3]*2 + [4]
                barcos_info = []        
                punto_a.colocar_barcos(tablero, barcos, barcos_info)
                estado = "game"
                print("Selected Easy level")
            elif clic == "Medium":
                nivel_actual = "Medium"
                FILAS = 20
                COLUMNAS = 20
                TAM_CELDA = 25  # Ajusta el tamaño para que quepa en pantalla
                tablero = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                disparos = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                barcos = [1]*8 + [2]*6 + [3]*4 + [4]*2 
                barcos_info = []
                punto_a.colocar_barcos(tablero, barcos, barcos_info)
                estado = "game"
                print("Selected Medium level")
            elif clic == "Hard":
                nivel_actual = "Hard"
                FILAS = 40
                COLUMNAS = 40
                TAM_CELDA = 12 
                tablero = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                disparos = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                barcos = [1]*12 + [2]*9 + [3]*6 + [4]*3 
                barcos_info = []
                punto_a.colocar_barcos(tablero, barcos, barcos_info)
                estado = "game"
                print("Selected Hard level")
                print("Starting game...")
            elif clic == "Level":
                estado= "levels"
                print("Selecting level...")
            elif clic == "Scores":
                print("Showing scores...")
        elif evento.type == pg.MOUSEBUTTONDOWN and estado == "game":
            clic = detectar_click_juego(evento.pos)
            if clic == "Restart":
                if clic == "Restart":
                    if nivel_actual == "Easy":
                        FILAS = 10
                        COLUMNAS = 10
                        TAM_CELDA = 40
                        barcos = [1]*4 + [2]*3 + [3]*2 + [4]
                    elif nivel_actual == "Medium":
                        FILAS = 20
                        COLUMNAS = 20
                        TAM_CELDA = 25
                        barcos = [1]*8 + [2]*6 + [3]*4 + [4]*2
                    elif nivel_actual == "Hard":
                        FILAS = 40
                        COLUMNAS = 40
                        TAM_CELDA = 12
                        barcos = [1]*12 + [2]*9 + [3]*6 + [4]*3

                    tablero = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                    disparos = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                    barcos_info = []
                    punto_a.colocar_barcos(tablero, barcos, barcos_info)
                    puntaje = 0
                    print("Game restarted")
            elif clic == "Back":
                estado = "menu"
                puntaje = 0
                print("Volver al menú")
            fila_col = obtener_celda_clic(*evento.pos)
            if fila_col:
                if fila_col[0] is not None and fila_col[1] is not None:
                    if tablero[fila_col[0]][fila_col[1]] == 1 and disparos[fila_col[0]][fila_col[1]] == 0:
                        sonido_barco.play()
                        disparos[fila_col[0]][fila_col[1]] = 2
                        if es_barco_hundido(barcos_info, disparos, fila_col[0], fila_col[1]):
                            for barco in barcos_info:
                                if (fila_col[0], fila_col[1]) in barco["posiciones"]:
                                    tamaño_barco = len(barco["posiciones"])
                                    puntaje += tamaño_barco * 10
                                    print(f"Barco hundido de tamaño {tamaño_barco}! +{tamaño_barco*10} puntos")
                                    sonido_hundido.play()
                                    break
                        else:
                            print("Tocado! +5 puntos")

                        puntaje += 5 

                    elif tablero[fila_col[0]][fila_col[1]] == 0 and disparos[fila_col[0]][fila_col[1]] == 0:
                        sonido_agua.play()
                        print("Agua")
                        puntaje -= 1
                        disparos[fila_col[0]][fila_col[1]] = 3
                if todos_barcos_hundidos(barcos_info, disparos):
                    estado = "fin"
                    print("¡Ganaste! Todos los barcos han sido hundidos.")
        elif evento.type == pg.MOUSEBUTTONDOWN and estado == "fin":
            # Puedes agregar aquí lógica para volver al menú o reiniciar
            clic = detectar_click_juego(evento.pos)
            if clic == "Back":
                estado = "menu"
                puntaje = 0
            elif clic == "Restart":
                if nivel_actual == "Easy":
                    FILAS = 10
                    COLUMNAS = 10
                    TAM_CELDA = 40
                    barcos = [1]*4 + [2]*3 + [3]*2 + [4]
                elif nivel_actual == "Medium":
                    FILAS = 20
                    COLUMNAS = 20
                    TAM_CELDA = 25
                    barcos = [1]*8 + [2]*6 + [3]*4 + [4]*2
                elif nivel_actual == "Hard":
                    FILAS = 40
                    COLUMNAS = 40
                    TAM_CELDA = 12
                    barcos = [1]*12 + [2]*9 + [3]*6 + [4]*3

                tablero = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                disparos = punto_a.inicializar_matriz(FILAS, COLUMNAS, 0)
                barcos_info = []
                punto_a.colocar_barcos(tablero, barcos, barcos_info)
                puntaje = 0
                estado = "game"
                print("Game restarted")           
    if estado=="menu":     
        TAMANO_NORMAL = (200, 50)
        TAMANO_GRANDE = (250, 70)
        pantalla.blit(fondo, (0, 0))
        actualizar_botones(boton_hover)
        dibujar_botones(boton_hover)
    elif estado == "game":
        pantalla.fill(CELESTE)
        dibujar_matriz(FILAS, COLUMNAS,TAM_CELDA, ANCHO, ALTO)
        dibujar_cuadricula() 
        #botones_game = ["Restart", "Back"]
        rect_score = pg.Rect(300, 555, 250, 40)
        pg.draw.rect(pantalla, GRIS, rect_score)
        fuente_score = pg.font.Font("ka1.ttf", 30)
        texto_score = fuente_score.render(f"Score: {puntaje}", True, NEGRO)
        texto_rect = texto_score.get_rect(center=rect_score.center)
        pantalla.blit(texto_score, texto_rect)
        TAMANO_NORMAL = (120, 40)
        TAMANO_GRANDE = (150, 55)
        
        actualizar_botones_juego(boton_hover_juego)
        dibujar_botones_juego(boton_hover_juego)
        YELLOW = (0,255,255)
        '''if todos_barcos_hundidos(barcos_info, disparos):
            rect_win = pg.Rect(250, 30, 350, 50)
            pg.draw.rect(pantalla, YELLOW , rect_win)
            fuente_win = pg.font.Font("ka1.ttf", 30)
            texto_win = fuente_win.render(f"You Win! Score: {puntaje}", True, NEGRO)
            pantalla.blit(texto_win, texto_rect)
            pg.display.flip()'''
    elif estado == "levels":
        pantalla.fill(CELESTE)
        boton_hover_niveles = detectar_hover_niveles(pos_mouse)
        actualizar_botones_niveles(boton_hover_niveles)
        dibujar_botones_niveles(boton_hover_niveles)
        
    
    
    
    elif estado == "fin":
        pantalla.fill(CELESTE)
        rect_win = pg.Rect(150, 200, 600, 100)
        pg.draw.rect(pantalla, (255, 255, 0), rect_win, border_radius=20)
        fuente_win = pg.font.Font("ka1.ttf", 35)
        texto_win = fuente_win.render(f"You Win! Score: {puntaje}", True, NEGRO)
        texto_rect = texto_win.get_rect(center=rect_win.center)
        pantalla.blit(texto_win, texto_rect)
        # Dibuja los botones de juego para permitir volver o reiniciar
        actualizar_botones_juego(boton_hover_juego)
        dibujar_botones_juego(boton_hover_juego)
        
    pg.display.flip()
pg.quit()
sys.exit()