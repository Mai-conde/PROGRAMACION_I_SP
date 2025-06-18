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
tamano_fuente_normal = 30
tamano_fuente_grande = 40  # Texto más grande para el hover
fuente_normal = pg.font.Font("ka1.ttf", tamano_fuente_normal)
fuente_grande = pg.font.Font("ka1.ttf", tamano_fuente_grande)

# Música de fondo
pg.mixer.music.load("Piratas del  caribe  cancion completa - android juegos.mp3")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.4)

# Cargar imagen de fondo
fondo = pg.image.load("SEA_BATTLE.PNG")
fondo = pg.transform.scale(fondo, (ANCHO, ALTO))

# Tamaños de botones (rectangulares)
TAMANO_NORMAL = (200, 50)
TAMANO_GRANDE = (250, 70)  # Tamaño aumentado
FILAS=10
COLUMNAS=10
TAM_CELDA=40

# Posiciones originales de los botones
posiciones_botones = {
    "Level": (300, 150),
    "Play": (300, 230),
    "Scores": (300, 310),
    "Exit": (300, 390)
}


# Diccionario para guardar los rectángulos actuales
botones = {}
def dibujar_matriz(filas, columnas, TAM_CELDA,Ancho, Alto):
    margen_x = (Ancho - (columnas * TAM_CELDA)) // 2
    margen_y = (Alto - (filas * TAM_CELDA)) // 2
    for x in range(columnas + 1):
        pg.draw.line(pantalla, NEGRO, (margen_x + x * TAM_CELDA, margen_y), (margen_x + x * TAM_CELDA, margen_y + filas * TAM_CELDA))
    for y in range(filas + 1):
        pg.draw.line(pantalla, NEGRO, (margen_x, margen_y + y * TAM_CELDA), (margen_x + columnas * TAM_CELDA, margen_y + y * TAM_CELDA))

def actualizar_botones(boton_hover=None):
    """Actualiza el tamaño de los botones según el hover"""
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

def dibujar_botones(boton_hover=None):
    """Dibuja los botones rectangulares con texto que crece"""
    for texto, rect in botones.items():
        # Dibujar rectángulo
        pg.draw.rect(pantalla, GRIS, rect)
        
        # Seleccionar fuente según hover
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

def obtener_celda_clic(x, y):
    FILAS, COLUMNAS = 10, 10
    TAM_CELDA = 40
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
    for i in range(10):
        for j in range(10):
            if disparos[i][j] == 2:  # Tocado
                pg.draw.circle(pantalla, (255,0,0), (margen_x + j*TAM_CELDA + TAM_CELDA//2, margen_y + i*TAM_CELDA + TAM_CELDA//2), 10)
            elif disparos[i][j] == 3:  # Agua
                pg.draw.circle(pantalla, (0,0,255), (margen_x + j*TAM_CELDA + TAM_CELDA//2, margen_y + i*TAM_CELDA + TAM_CELDA//2), 10)

# Inicializar botones con tamaño normal
actualizar_botones()

# Bucle principal
corriendo = True
estado="menu"
puntaje = 0
while corriendo:
    pos_mouse = pg.mouse.get_pos()
    boton_hover = detectar_hover(pos_mouse)
    
         
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
        elif evento.type == pg.MOUSEBUTTONDOWN and estado == "menu":
            clic = detectar_click(evento.pos)
            if clic == "Exit":
                corriendo = False
            elif clic == "Play":
                tablero = punto_a.inicializar_matriz(10, 10, 0)
                disparos = punto_a.inicializar_matriz(10, 10, 0)
                barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
                barcos_info = []
                punto_a.colocar_barcos(tablero, barcos, barcos_info)
                estado= "game"
                print("Starting game...")
            elif clic == "Level":
                print("Selecting level...")
            elif clic == "Scores":
                print("Showing scores...")
        elif evento.type == pg.MOUSEBUTTONDOWN and estado == "game":
            fila_col = obtener_celda_clic(*evento.pos)
            if fila_col:
                if fila_col[0] is not None and fila_col[1] is not None:
                    if tablero[fila_col[0]][fila_col[1]] == 1 and disparos[fila_col[0]][fila_col[1]] == 0:
                        disparos[fila_col[0]][fila_col[1]] = 2
                        if es_barco_hundido(barcos_info, disparos, fila_col[0], fila_col[1]):
                            print("barco Hundido!")
                            puntaje += 10
                        else:
                            print("Tocado")
                        
                        puntaje+= 5 
                    elif tablero[fila_col[0]][fila_col[1]] == 0 and disparos[fila_col[0]][fila_col[1]] == 0:
                        print("Agua")
                        puntaje-= 1
                        disparos[fila_col[0]][fila_col[1]] = 3
    if estado=="menu":     
        pantalla.blit(fondo, (0, 0))
        actualizar_botones(boton_hover)
        dibujar_botones(boton_hover)
    elif estado == "game":
        pantalla.fill(CELESTE)
        dibujar_matriz(FILAS, COLUMNAS,TAM_CELDA, ANCHO, ALTO)
        dibujar_cuadricula() 
    pg.display.flip()
pg.quit()
sys.exit()