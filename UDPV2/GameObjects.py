from const import *
import pygame as pg
from random import randint


gameObjects = []


class Player:
    def __init__(self, inputs):
        gameObjects.append(self)
        self.inputs = inputs
        self.pos = pg.Vector2(400, 300)
        self.color = pg.color.Color(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        )

        self.speed = 1
        self.move_at = self.pos
        self.step = pg.Vector2(0, 0)

    def update(self, dt):
        if self.inputs["ml"]:
            self.move_at = pg.Vector2(self.inputs["pos"])
            self.step = (self.move_at - self.pos + pg.Vector2(0.01, 0.01)).normalize() * self.speed

        if self.pos.distance_to(self.move_at) > 10:
            self.pos += self.step * dt

    def get_state(self):
        return {
            "type": PLAYER,
            "pos": tuple(self.pos),
            "color": tuple(self.color)
        }
