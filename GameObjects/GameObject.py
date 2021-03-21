import pygame as pg
from proto import *
from math import floor
from const import *
import numpy as np


bloc = np.array([
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 3, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 1],
[1, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1],
[1, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1],
[1, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1],
[1, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])


class Bullet:
    bullets = []

    def __init__(self, pos, aim, color):
        self.color = color
        self.rad = BULLET_RAD
        self.step = (aim - pos + pg.Vector2(0.001, 0.001)).normalize() * 500
        self.pos = pos + self.step * 0.2
        Bullet.bullets.append(self)

    def collide(self, pos):
        return self.pos.distance_to(pos) < 40

    def update(self, dt):
        tmp = self.pos + self.step * dt
        if bloc[int(tmp.y / 32), int(tmp.x / 32)] != 1:
            self.pos = tmp
        else:
            Bullet.bullets.remove(self)

    def get_state(self):
        return {
            "pos": tuple(self.pos),
            "color": self.color
        }


class Soldier:
    def __init__(self, first, initial_pos: pg.Vector2, respawn_pos: pg.Vector2):
        print(first)
        self.aim = initial_pos + ((SOLDIER_RAD+GUN_WIDTH) * (1 if first else -1), 0)
        self.rad = SOLDIER_RAD
        self.pos = initial_pos
        self.respawn_pos = respawn_pos
        self.angle = 0
        self.speed = SOLDIER_SPEED
        self.m_at = self.pos
        self.selected = False
        self.reload_timer = 666
        self.alive = 666
        self.step = pg.Vector2(0, 0)

    def is_target(self, center):
        return self.pos.distance_to(center) < self.rad

    def move_to(self, data):
        self.m_at = pg.Vector2(data['pos'])
        diff = self.m_at - self.pos + pg.Vector2(0.001, 0.001)
        self.step = diff.normalize() * self.speed

    def can_shoot(self):
        return self.reload_timer > 666

    def update(self, dt, first):
        if self.alive > 666:
            if self.pos.distance_to(self.m_at) > 5:
                tmp = self.pos + self.step * dt
                if bloc[int(tmp.y / 32), int(tmp.x / 32)] != 1:
                    self.pos = tmp
                    self.aim = self.aim + self.step*dt

            for bullet in Bullet.bullets:
                if bullet.collide(self.pos):
                    self.alive = 0
                    self.pos = self.respawn_pos
        self.reload_timer += dt
        self.alive += dt

    def get_state(self):
        return {
            "pos": tuple(self.pos),
            "aim": tuple(self.aim),
            "selected": self.selected
        }


class Player:
    def __init__(self, sock, first):
        self.sock = sock
        self.first = first
        if first:
            self.soldiers = [
                Soldier(first, pg.Vector2(100, 700), pg.Vector2(75, 75)),
                Soldier(first, pg.Vector2(200, 380), pg.Vector2(75, 150)),
                Soldier(first, pg.Vector2(150, 150), pg.Vector2(150, 75)),
            ]
        else:
            self.soldiers = [
                Soldier(first, pg.Vector2(1180, 700), pg.Vector2(1280-75, 75)),
                Soldier(first, pg.Vector2(1000, 380), pg.Vector2(1280-75, 150)),
                Soldier(first, pg.Vector2(1130, 150), pg.Vector2(1280-150, 75))
            ]

        self.target = self.soldiers[1]
        self.target.selected = True

    def update(self, dt):
        data = recv_msg(self.sock)
        if data is not None:
            self.target.aim = data['pos']

            self.target.aim =  tuple(self.target.pos - (self.target.pos - data["pos"]).normalize() * (self.target.rad + GUN_WIDTH))
            for soldier in self.soldiers:
                soldier.update(dt, self.first)

            if data["left"]:
                for soldier in self.soldiers:
                    if soldier.is_target(data["pos"]):
                        self.target.selected = False
                        self.target = soldier
                        soldier.selected = True
                        break
                else:
                    self.target.move_to(data)

            if data["right"] and self.target.can_shoot():
                Bullet(self.target.pos, data["pos"], self.first)

    def get_state(self):
        return {
            "soldiers": [soldier.get_state() for soldier in self.soldiers],
        }
