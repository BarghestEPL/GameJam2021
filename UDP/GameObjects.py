import json
from const import *
import pygame as pg
from random import randint


players = []
gameObjects = []


def get_state():
    state = []
    for obj in gameObjects:
        obj.update()
        state.append(obj.get_state())
    for player in players:
        state.append(player.get_state())
    return json.dumps(state).encode("utf-8")


class Player:
    def __init__(self):
        players.append(self)
        self.pos = pg.Vector2(400, 300)
        self.color = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

    def update(self, data):
        inputs = json.loads(data.decode("utf-8"))

    def get_state(self):
        return {
            "type": PLAYER,
            "pos": tuple(self.pos),
            "color": self.color
        }
