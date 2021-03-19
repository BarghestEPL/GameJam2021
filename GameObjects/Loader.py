import os
import pygame as pg
from math import cos, sin


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def pos(self):
        return self.x, self.y

    def rot_x(self, o, t):
        c, s = cos(t), sin(t)
        self.y -= o.y
        self.z -= o.z

        rot_y = self.y * c - self.z * s
        rot_z = self.y * s + self.z * c

        self.y = rot_y + o.y
        self.z = rot_z + o.z

    def rot_y(self, o, t):
        c, s = cos(t), sin(t)
        self.x -= o.x
        self.z -= o.z

        rot_x = self.x * c + self.z * s
        rot_z = self.z * c - self.x * s

        self.x = rot_x + o.x
        self.z = rot_z + o.z

    def rot_z(self, o, t):
        c, s = cos(t), sin(t)
        self.x -= o.x
        self.y -= o.y

        rot_x = self.x * c - self.y * s
        rot_y = self.x * s + self.y * c

        self.x = rot_x + o.x
        self.y = rot_y + o.y


class Loader:
    def __init__(self, w, x, y):
        self.pace = 0.01
        self.image = pg.image.load("/home/barghest/Documents/Github/GameJam2021/GameObjects/sprites/tux.png")
        self.color = pg.Color(255, 255, 255)
        self.a = Point3D(x - w, y - w, -w)
        self.b = Point3D(x + w, y - w, -w)
        self.c = Point3D(x + w, y + w, -w)
        self.d = Point3D(x - w, y + w, -w)

        self.e = Point3D(x + w, y + w, w)
        self.f = Point3D(x - w, y + w, w)
        self.g = Point3D(x - w, y - w, w)
        self.h = Point3D(x + w, y - w, w)

        self.p = [self.a, self.b, self.c, self.d,
                  self.e, self.f, self.g, self.h]

        self.w = w
        self.pos = Point3D(x, y, 0)

    def rot_x(self):
        for p in self.p:
            p.rot_x(self.pos, self.pace)

    def rot_y(self):
        for p in self.p:
            p.rot_y(self.pos, self.pace)

    def rot_z(self):
        for p in self.p:
            p.rot_z(self.pos, self.pace)

    def update(self):
        self.rot_x()
        self.rot_y()
        self.rot_z()

    def render(self, win):
        self.update()
        win.blit(self.image, (323, 210))
        pg.draw.line(win, self.color, self.a.pos(), self.b.pos(), 2)
        pg.draw.line(win, self.color, self.b.pos(), self.c.pos(), 2)
        pg.draw.line(win, self.color, self.c.pos(), self.d.pos(), 2)
        pg.draw.line(win, self.color, self.d.pos(), self.a.pos(), 2)

        pg.draw.line(win, self.color, self.e.pos(), self.f.pos(), 2)
        pg.draw.line(win, self.color, self.f.pos(), self.g.pos(), 2)
        pg.draw.line(win, self.color, self.g.pos(), self.h.pos(), 2)
        pg.draw.line(win, self.color, self.h.pos(), self.e.pos(), 2)

        pg.draw.line(win, self.color, self.a.pos(), self.g.pos(), 2)
        pg.draw.line(win, self.color, self.b.pos(), self.h.pos(), 2)
        pg.draw.line(win, self.color, self.c.pos(), self.e.pos(), 2)
        pg.draw.line(win, self.color, self.d.pos(), self.f.pos(), 2)
