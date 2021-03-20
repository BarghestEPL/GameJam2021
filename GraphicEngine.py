import pygame as pg


class GraphicEngine:
    def __init__(self, win):
        self.win = win

    def render(self, data):
        for x in range(0, 1280, 64):
            pg.draw.line(self.win, (255, 255, 255), (x, 0), (x, 800))
        for y in range(0, 800, 64):
            pg.draw.line(self.win, (255, 255, 255), (0, y), (1280, y))

        pb = data.get('pb')
        if pb is not None:
            for soldier in data['pb']['soldiers']:
                pg.draw.circle(self.win, (0, 0, 255), soldier['pos'], 30)

        pr = data.get('pr')
        if pr is not None:
            for soldier in data['pr']['soldiers']:
                pg.draw.circle(self.win, (255, 0, 0), soldier['pos'], 30)

