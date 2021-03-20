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
        self.target.selected = True

    def update(self):
        data = recv_msg(self.sock)
        if data is not None:
            if data["left"]:
                for soldier in self.soldiers:
                    if soldier.is_target(data["pos"]):
                        self.target.selected = False
                        self.target = soldier
                        soldier.selected = True
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
        self.rad = 30
        self.pos = pos
        self.angle = 0
        self.health = 100
        self.speed = 0.5
        self.m_at = self.pos
        self.selected = False
        self.step = pg.Vector2(0, 0)

    def is_target(self, center):
        return self.pos.distance_to(center) < self.rad

    def aim(self, center):
        self.angle = self.pos.angle_to(center)

    def move_to(self, data):
        self.m_at = pg.Vector2(data['pos'])
        self.step = pg.Vector2((self.m_at.x - self.pos.x) / 60, (self.m_at.y - self.pos.y) / 60)

    def update(self):
        # moving
        if self.pos.distance_to(self.m_at) > 1:
            self.pos += self.step

    def get_state(self):
        return {
            "pos": tuple(self.pos),
            "ang": self.angle,
            "health": self.health,
            "selected": self.selected
        }
