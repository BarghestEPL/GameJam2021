import sys
import pygame as pg
from time import time
from GameObjects.Loader import Loader

fps = 60
dt = 1 / fps
width, height = 800, 600

# Set up the window.
pg.init()
clock = pg.time.Clock()
pg.display.set_caption('Louvain-li-Nux 2021')
font = pg.font.SysFont("comicsansms", 24)
screen = pg.display.set_mode((width, height))

run = True
ts = time()
loader = Loader(150.0, 400.0, 300.0)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                run = False

    screen.fill((0, 0, 0))
    loader.render(screen)

    text = font.render(str(int(clock.get_fps())), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pg.display.flip()
    dt = clock.tick(fps)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()

    # draws
    screen.fill((0, 0, 0))
    text = font.render(str(int(clock.get_fps())), True, (255, 255, 25))
    screen.blit(text, (10, 10))

    pg.display.flip()
    dt = clock.tick(fps)
