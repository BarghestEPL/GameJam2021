import time
import socket
from proto import *
import pygame as pg
from GameObjects.GameObject import *
import threading

HP = HOST, PORT = "", 45759
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


player1 = Player(red_sock, "red")
player2 = Player(blue_sock, "blue")


def run():
    while True:
        player2.update(dt)


test_blue = 3
test_red = 3
score_counting = 0

time = 0

threading.Thread(target=run, daemon=True).start()
while True:
    time += dt

    if time > GAME_DURATION:
        pass

    player1.update(dt)
    for bullet in Bullet.bullets:
        bullet.update(dt)

    if player1.color == "blue":
        playerBlue = player1
        playerRed = player2
    else:
        playerBlue = player2
        playerRed = player1
    
    score_counting += sum([soldier.counting for soldier in playerBlue.soldiers])*dt

    data = {
        "pb": playerBlue.get_state(),
        "pr": playerRed.get_state(),
        "bu": [bullet.get_state() for bullet in Bullet.bullets],
        "score_counting": score_counting,
        "time_remaining": GAME_DURATION-time
    }

    test_blue = 3 if send_msg(player1.sock, data) else test_blue - 1
    if test_blue == 0:
        break
    send_msg(player2.sock, data)
    test_red = 3 if send_msg(player1.sock, data) else test_red - 1
    if test_red == 0:
        break
    clock.tick(fps)

srv.close()
