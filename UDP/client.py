import sys
import json
import socket
import threading
import pygame as pg

from const import *
from protocol import *
from GraphicEngine import GraphicEngine

pg.init()
clock = pg.time.Clock()
pg.display.set_caption("UDP GAME")
font = pg.font.SysFont("comicsansms", 24)
screen = pg.display.set_mode(DIM)

dt = 0
run = 15
ge = GraphicEngine(screen)
srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def handle_srv():
    while True:
        data, addr = srv.recvfrom(DATA_LEN)
        data = json.loads(data.decode("utf-8"))
        if data is not None:
            screen.fill((0, 0, 0))
            ge.render(data)
            text = font.render(str(int(clock.get_fps())), True, (255, 255, 25))
            screen.blit(text, (10, 10))
            pg.display.flip()


threading.Thread(target=handle_srv, daemon=True).start()
while True:
    left, _, right = False, False, False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            srv.close()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            left, _, right = pg.mouse.get_pressed(3)

    inputs = {
        "m_pos": pg.mouse.get_pos(),
        "ml": left,
        "mr": right
    }

    srv.sendto(json.dumps(inputs).encode("utf-8"), ADDRESS)
    dt = clock.tick(60)
