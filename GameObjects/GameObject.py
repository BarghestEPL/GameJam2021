import pygame as pg
from proto import *
from math import cos, sin, radians


class Player:
    def __init__(self, sock):
        self.sock = sock
        self.soldiers = [
            Soldier(pg.Vector2(100, 100)),
            Soldier(pg.Vector2(200, 100)),
            Soldier(pg.Vector2(300, 100))
        ]

        self.target = self.soldiers[1]

    def update(self):
        data = recv_msg(self.sock)
        if data is not None:
            if data["left"]:
                for soldier in self.soldiers:
                    if soldier.is_target(data["pos"]):
                        self.target = soldier
                        break
                else:
                    self.target.move_to(data)
            self.target.aim(data['pos'])
            for soldier in self.soldiers:
                soldier.update()

    def get_state(self):
        return {"soldiers": [soldier.get_state() for soldier in self.soldiers]}


class Soldier(pg.sprite.Sprite):
    def __init__(self, pos: pg.Vector2):
        pg.sprite.Sprite.__init__(self)
        self.rad = 20
        self.pos = pos
        self.angle = 0
        self.health = 100
        self.speed = 0.5
        self.move_at = self.pos
        self.vel = 0

    def is_target(self, center):
        return self.pos.distance_to(center) < self.rad

    def aim(self, center):
        self.angle = self.pos.angle_to(center)

    def move_to(self, data):
        self.move_at = data['pos']
        self.vel = pg.Vector2(1, 0).rotate(radians(self.pos.angle_to(data['pos'])))

    def update(self):
        # moving
        if self.pos.distance_to(self.move_at) > 1:
            self.pos += self.vel

    def get_state(self):
        return {
            "pos": tuple(self.pos),
            "ang": self.angle,
            "health": self.health
        }
