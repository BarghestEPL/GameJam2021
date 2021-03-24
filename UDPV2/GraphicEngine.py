import pygame as pg
from const import *


class GraphicEngine:
    def __init__(self, win, font):
        self.font = font
        self.win = win
        self.data = []

    def render_player(self, data):
        pg.draw.circle(self.win, data["color"], data["pos"], 25)

    def render(self, fps):
        self.win.fill((0, 0, 0))
        for obj in self.data:
            if obj["type"] == PLAYER:
                self.render_player(obj)

        text = self.font.render(str(fps), True, (255, 255, 25))
        self.win.blit(text, (10, 10))
        pg.display.flip()
