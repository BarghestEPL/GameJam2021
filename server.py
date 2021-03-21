import time
import socket
from proto import *
import pygame as pg
from GameObjects.GameObject import *
import threading

HP = HOST, PORT = "", 45800
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


playerBlue = Player(blue_sock, True)
playerRed = Player(red_sock, False)


def run():
    while True:
        playerBlue.update(dt)


test_blue = 3
test_red = 3
threading.Thread(target=run, daemon=True).start()
while True:
    playerRed.update(dt)
    data = {
        "pb": playerBlue.get_state(),
        "pr": playerRed.get_state()
    }

    test_blue = 3 if send_msg(playerRed.sock, data) else test_blue - 1
    if test_blue == 0:
        break
    send_msg(playerBlue.sock, data)
    test_red = 3 if send_msg(playerRed.sock, data) else test_red - 1
    if test_red == 0:
        break
    clock.tick(fps)

srv.close()
