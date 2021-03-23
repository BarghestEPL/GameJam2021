import pygame as pg
from const import *


class GraphicEngine:
    def __init__(self, win):
        self.win = win

    def render_player(self, data):
        pg.draw.circle(self.win, data["color"], data["pos"], 25)

    def render(self, data):
        for obj in data:
            if obj["type"] == PLAYER:
                self.render_player(obj)
