import pygame as pg
import sys

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

# Fuente
fuente = pg.font.Font("C:/Users/Maite Conde/Desktop/Python/2° CUATRIMESTRE/segundo parcial/ka1.ttf", 30)

# Música de fondo
pg.mixer.music.load("C:/Users/Maite Conde/Desktop/Python/2° CUATRIMESTRE/segundo parcial/Piratas del  caribe  cancion completa - android juegos.mp3")
pg.mixer.music.play(-1)  # -1 = repetir infinitamente
pg.mixer.music.set_volume(0.4)

# Cargar imagen de fondo
fondo = pg.image.load("C:/Users/Maite Conde/Desktop/Python/2° CUATRIMESTRE/segundo parcial/SEA_BATTLE.PNG")
fondo = pg.transform.scale(fondo, (ANCHO, ALTO))

# Botones: texto, rectángulo
botones = {
    "Level": pg.Rect(300, 150, 200, 50),
    "Play": pg.Rect(300, 230, 200, 50),
    "Scores": pg.Rect(300, 310, 200, 50),
    "Exit": pg.Rect(300, 390, 200, 50)
}

def dibujar_botones():
    for texto, rect in botones.items():
        pg.draw.rect(pantalla, GRIS, rect)
        texto_render = fuente.render(texto, True, NEGRO)
        texto_rect = texto_render.get_rect(center = rect.center)
        pantalla.blit(texto_render, texto_rect)

def detectar_click(pos):
    for texto, rect in botones.items():
        if rect.collidepoint(pos):
            return texto
    return None

# Bucle principal
corriendo = True
while corriendo:
    pantalla.blit(fondo, (0, 0))
    dibujar_botones()
    pg.display.flip()

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
        elif evento.type == pg.MOUSEBUTTONDOWN:
            clic = detectar_click(evento.pos)
            if clic == "Exit":
                corriendo = False
            elif clic == "Play":
                print("Starting game...")
            elif clic == "Level":
                print("Selecting level...")
            elif clic == "Scores":
                print("Showing scores...")

pg.quit()
sys.exit()
