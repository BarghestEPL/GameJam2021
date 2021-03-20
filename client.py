import sys
import socket
import pygame as pg
from time import time
import threading

from proto import *
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


# MULTIPLAYER

HOST, PORT = "109.88.29.134", 45632
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    srv_sock.connect((HOST, PORT))
except ConnectionRefusedError as error:
    print(error)
    sys.exit()


def handle_srv():
    while True:
        data = recv_msg(srv_sock)
        if data is None:
            break
        print(data)


threading.Thread(target=handle_srv, daemon=True).start()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    inputs = {
        "m_pos": pg.mouse.get_pos()
    }
    send_msg(srv_sock, inputs)


    # draws
    screen.fill((0, 0, 0))
    text = font.render(str(int(clock.get_fps())), True, (255, 255, 25))
    screen.blit(text, (10, 10))

    pg.display.flip()
    dt = clock.tick(fps)
