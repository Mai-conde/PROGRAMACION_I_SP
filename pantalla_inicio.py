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
pg.mixer.music.set_volume(0.2)

# Cargar imagen de fondo
fondo = pg.image.load("SEA_BATTLE.PNG")
fondo = pg.transform.scale(fondo, (ANCHO, ALTO))

# Tamaños de botones (rectangulares)
TAMANO_NORMAL = (200, 50)
TAMANO_GRANDE = (250, 70)  # Tamaño aumentado

# Posiciones originales de los botones
posiciones_botones = {
    "Level": (300, 150),
    "Play": (300, 230),
    "Scores": (300, 310),
    "Exit": (300, 390),
    "Mute" : (50, 30),
}
# Diccionario para guardar los rectángulos actuales
botones = {}
def dibujar_cuadricula():
    FILAS, COLUMNAS = 10, 10
    TAM_CELDA = 40
    margen_x = (ANCHO - (COLUMNAS * TAM_CELDA)) // 2
    margen_y = (ALTO - (FILAS * TAM_CELDA)) // 2
    for x in range(COLUMNAS + 1):
        pg.draw.line(pantalla, NEGRO, (margen_x + x * TAM_CELDA, margen_y), (margen_x + x * TAM_CELDA, margen_y + FILAS * TAM_CELDA))
    for y in range(FILAS + 1):
        pg.draw.line(pantalla, NEGRO, (margen_x, margen_y + y * TAM_CELDA), (margen_x + COLUMNAS * TAM_CELDA, margen_y + y * TAM_CELDA))
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
            """pg.draw.line(
                pantalla, NEGRO,
                (rect.right - 10, rect.bottom - 10),
                (rect.left + 10, rect.top + 10),
                3
            )
            """
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

def detectar_hover(pos):
    """Detecta qué botón está bajo el cursor"""
    for texto, rect in botones.items():
        if rect.collidepoint(pos):
            return texto
    return None

def detectar_click(pos):
    for texto, rect in botones.items():
        if rect.collidepoint(pos):
            return texto
    return None

# Inicializar botones con tamaño normal
actualizar_botones()

muteado= False
# Bucle principal
corriendo = True
estado="menu"
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
                estado= "game"
                print("Starting game...")
            elif clic == "Level":
                print("Selecting level...")
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
    if estado=="menu":     
        pantalla.blit(fondo, (0, 0))
        actualizar_botones(boton_hover)
        dibujar_botones(boton_hover)
    elif estado == "game":
        pantalla.fill(CELESTE)
        dibujar_cuadricula()
    pg.display.flip()
pg.quit()
sys.exit()