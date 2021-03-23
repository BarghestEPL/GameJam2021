import json
from const import *
import pygame as pg
from random import randint

clients = {}
gameObjects = []


def get_state(dt):
    state = []
    for obj in gameObjects:
        obj.update(dt)
        state.append(obj.get_state())
    return json.dumps(state).encode("utf-8")


class Player:
    def __init__(self, addr, data):
        gameObjects.append(self)
        self.inputs = None
        self.set_inputs(data)
        clients[addr] = self

        self.timeout = TIMEOUT
        self.pos = pg.Vector2(400, 300)
        self.addr = addr
        self.color = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

        self.speed = 0.8
        self.move_at = self.pos
        self.step = pg.Vector2(0, 0)

    def set_inputs(self, data):
        self.timeout = TIMEOUT
        self.inputs = json.loads(data.decode("utf-8"))

    def update(self, dt):
        self.timeout -= 1
        if self.timeout < 0:
            gameObjects.remove(self)
            clients.pop(self.addr)

        if self.inputs["ml"]:
            self.move_at = pg.Vector2(self.inputs["pos"])
            self.step = (self.move_at - self.pos + pg.Vector2(0.01, 0.01)).normalize() * self.speed

        if self.pos.distance_to(self.move_at) > 5:
            self.pos += self.step * dt

    def get_state(self):
        return {
            "type": PLAYER,
            "pos": tuple(self.pos),
            "color": self.color
        }
