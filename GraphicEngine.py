import pygame as pg


class GraphicEngine:
    def __init__(self, win):
        self.win = win

    def render(self, data):
        for b_sol in data['pb']['soldiers']:
            pg.draw.circle(self.win, (0, 0, 255), b_sol['pos'], 20)
        for r_sol in data['pr']['soldiers']:
            pg.draw.circle(self.win, (255, 0, 0), r_sol['pos'], 20)
