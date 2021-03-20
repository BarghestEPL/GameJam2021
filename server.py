import time
import socket
from proto import *
import pygame as pg
from GameObjects.GameObject import *
import threading

HP = HOST, PORT = "", 45632
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(HP)
srv.listen(5)

fps = 60
dt = 1 / fps
clock = pg.time.Clock()
blue_sock, _ = srv.accept()
print("blue is connected")
red_sock, _ = srv.accept()
print("red is connected")


playerBlue = Player(blue_sock)
playerRed = Player(red_sock)


def run():
    while True:
        playerBlue.update()


threading.Thread(target=run, daemon=True).start()
while True:
    playerRed.update()

    data = {
        "pb": playerBlue.get_state(),
        "pr": playerRed.get_state()
    }

    send_msg(playerRed.sock, data)
    send_msg(playerBlue.sock, data)
    clock.tick(fps)
