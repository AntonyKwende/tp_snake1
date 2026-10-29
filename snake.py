"""
v03 : Le damier
Plateau de 30x30 cases de 20 pixels
"""

import pygame as pg

# Constantes du plateau
NB_COLS = 30
NB_ROWS = 30
TILE_SIZE = 20

# Dimensions de la fenêtre
WIDTH = NB_COLS * TILE_SIZE   # 600 px
HEIGHT = NB_ROWS * TILE_SIZE  # 600 px

# Couleurs du damier (ex. blanc / noir ou deux nuances de vert/gris)
COLOR_1 = (240, 240, 240)
COLOR_2 = (0, 0, 0)

def draw_checkerboard(surface):
    for row in range(NB_ROWS):
        for col in range(NB_COLS):
            # Alternance des cases
            color = COLOR_1 if (row + col) % 2 == 0 else COLOR_2
            
            # Position en pixels
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            
            rect = pg.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pg.draw.rect(surface, color, rect)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

running = True
while running:
    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

    # Affichage du damier
    draw_checkerboard(screen)
    snake = [
    (10, 15),
    (11, 15),
    (12, 15),
]
    pg.display.update()

pg.quit()
