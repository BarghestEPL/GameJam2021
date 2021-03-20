import pygame as pg
from proto import *


class Player:
    def __init__(self, socket):
        self.sock = socket

        self.soldiers = [
            Soldier(pg.Vector2(100, 100)),
            Soldier(pg.Vector2(200, 100)),
            Soldier(pg.Vector2(300, 100))
        ]
        pg.Vector2()

    def update(self):
        data = recv_msg(self.sock)
        for sold in self.soldiers:
            sold.move_to()

    def get_state(self):
        return {"soldiers": [soldier.get_state() for soldier in self.soldiers]}


class Soldier(pg.sprite.Sprite):
    def __init__(self, pos: pg.Vector2):
        pg.sprite.Sprite.__init__(self)
        # self.image, self.rect = pg.load_image('')
        self.pos = pos
        self.health = 100

    def update(self):
        pass

    def move_to(self):
        self.pos.update(self.pos.x + 0.1, self.pos.y)

    def get_state(self):
        return {"pos": tuple(self.pos), "health": self.health}


class Republican(Soldier):
    def __init__(self):
        super().__init__()
        self.counting = False


class Democrat(Soldier):
    def __init__(self):
        super().__init__()
