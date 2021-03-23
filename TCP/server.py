import socket
from proto import *
import pygame as pg
from GameObjects.GameObject import *
import threading
from math import ceil

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

player1 = Player(red_sock, "red")
player2 = Player(blue_sock, "blue")


def run():
    while True:
        player2.update(dt)


test_blue = 3
test_red = 3
score_counting = 0

player1_score = 0
player2_score = 0

time = 0
threading.Thread(target=run, daemon=True).start()
while time < START_DURATION:
    time += dt
    
    player1.update(dt)
    for bullet in Bullet.bullets:
        bullet.update(dt)

    if player1.color == "blue":
        playerBlue = player1
        playerRed = player2
    else:
        playerBlue = player2
        playerRed = player1
    
    data = {
        "pb": playerBlue.get_state(),
        "pr": playerRed.get_state(),
        "bu": [bullet.get_state() for bullet in Bullet.bullets],
        "score_counting": score_counting,
        "time_remaining": ceil(START_DURATION-time),
        "state": "start1",
        "color": "RED"
    }

    test_blue = 3 if send_msg(player1.sock, data) else test_blue - 1
    if test_blue == 0:
        break
    data["color"]: "BLUE"
    send_msg(player2.sock, data)
    data["color"]: "RED"
    test_red = 3 if send_msg(player1.sock, data) else test_red - 1
    if test_red == 0:
        break

time = 0

player1_score = score_counting

time = 0
threading.Thread(target=run, daemon=True).start()
while time < GAME_DURATION:
    time += dt
    
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
        "time_remaining": ceil(GAME_DURATION-time),
        "state": "game1"
    }

    test_blue = 3 if send_msg(player1.sock, data) else test_blue - 1
    if test_blue == 0:
        break
    send_msg(player2.sock, data)
    test_red = 3 if send_msg(player1.sock, data) else test_red - 1
    if test_red == 0:
        break
    clock.tick(fps)


time = 0
while time < END_DURATION:
    time += dt
    

    player1.update(dt)
    for bullet in Bullet.bullets:
        bullet.update(dt)

    if player1.color == "blue":
        playerBlue = player1
        playerRed = player2
    else:
        playerBlue = player2
        playerRed = player1
    

    data = {
        "pb": playerBlue.get_state(),
        "pr": playerRed.get_state(),
        "bu": [bullet.get_state() for bullet in Bullet.bullets],
        "score_counting": score_counting,
        "time_remaining": floor(END_DURATION-time),
        "state": "end1",
        "color": "RED"
    }

    test_blue = 3 if send_msg(player1.sock, data) else test_blue - 1
    if test_blue == 0:
        break

    data["color"] = "BLUE"
    send_msg(player2.sock, data)
    data["color"] = "RED"
    test_red = 3 if send_msg(player1.sock, data) else test_red - 1
    if test_red == 0:
        break
    clock.tick(fps)

player1.reset("blue")
player2.reset("red")

time = 0
while time < START_DURATION:
    time += dt
    

    player1.update(dt)
    for bullet in Bullet.bullets:
        bullet.update(dt)

    if player1.color == "blue":
        playerBlue = player1
        playerRed = player2
    else:
        playerBlue = player2
        playerRed = player1
    

    data = {
        "pb": playerBlue.get_state(),
        "pr": playerRed.get_state(),
        "bu": [bullet.get_state() for bullet in Bullet.bullets],
        "score_counting": score_counting,
        "time_remaining": floor(START_DURATION-time),
        "state": "start2",
        "color": "BLUE"
    }

    test_blue = 3 if send_msg(player1.sock, data) else test_blue - 1
    if test_blue == 0:
        break
    data["color"]: "RED"
    send_msg(player2.sock, data)
    data["color"]: "BLUE"
    test_red = 3 if send_msg(player1.sock, data) else test_red - 1
    if test_red == 0:
        break
    clock.tick(fps)

time = 0
score_counting = 0
while time < GAME_DURATION:
    time += dt
    
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
        "time_remaining": ceil(GAME_DURATION-time),
        "state": "game1"
    }

    test_blue = 3 if send_msg(player1.sock, data) else test_blue - 1
    if test_blue == 0:
        break
    send_msg(player2.sock, data)
    test_red = 3 if send_msg(player1.sock, data) else test_red - 1

    if test_red == 0:
        break

    clock.tick(fps)

player2_score = score_counting

time = 0
while time < END_DURATION:
    time += dt
    

    player1.update(dt)
    for bullet in Bullet.bullets:
        bullet.update(dt)

    if player1.color == "blue":
        playerBlue = player1
        playerRed = player2
    else:
        playerBlue = player2
        playerRed = player1
    

    data = {
        "pb": playerBlue.get_state(),
        "pr": playerRed.get_state(),
        "bu": [bullet.get_state() for bullet in Bullet.bullets],
        "score_counting": score_counting,
        "time_remaining": floor(END_DURATION-time),
        "state": "end2",
        "color": "BLUE"
    }

    test_blue = 3 if send_msg(player1.sock, data) else test_blue - 1
    if test_blue == 0:
        break
    data["color"]: "RED"
    send_msg(player2.sock, data)
    test_red = 3 if send_msg(player1.sock, data) else test_red - 1
    if test_red == 0:
        break
    clock.tick(fps)
time = 0

if player1_score > player2_score:
    winner = 1
elif player2_score > player1_score:
    winner = 2
else:
    winner = 0

while True:
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
        "time_remaining": floor(GAME_DURATION-time),
        "state": "final",
        "winner": winner,
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
