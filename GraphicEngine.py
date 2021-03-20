import pygame as pg


class GraphicEngine:
    def __init__(self, win):
        self.win = win

    def render(self, data):
        for soldier in data['blue']['soldiers']:
            pg.draw.circle(self.win, (0, 255, 0), soldier['pos'], 10)
