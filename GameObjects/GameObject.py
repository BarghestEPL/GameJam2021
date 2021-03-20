import pygame as pg
from proto import *


class Player:
    def __init__(self, sock):
        self.sock = sock
        self.soldiers = [
            Soldier(pg.Vector2(100, 100)),
            Soldier(pg.Vector2(200, 100)),
            Soldier(pg.Vector2(300, 100))
        ]

    def update(self):
        data = recv_msg(self.sock)
        print(data)
        pass

    def get_state(self):
        return {"soldiers": [soldier.get_state() for soldier in self.soldiers]}


class Soldier(pg.sprite.Sprite):
    def __init__(self, pos: pg.Vector2):
        pg.sprite.Sprite.__init__(self)
        self.pos = pos
        self.health = 100

    def update(self):
        pass

    def get_state(self):
        return {"pos": tuple(self.pos), "health": self.health}
