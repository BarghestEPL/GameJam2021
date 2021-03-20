import pygame as pg


class GraphicEngine:
    def __init__(self, win):
        self.win = win

    def render(self, data):
        for b_sol in data['pb']['soldiers']:
            if b_sol['selected']:
                pg.draw.circle(self.win, (255, 255, 0), b_sol['pos'], 32)
                pg.draw.circle(self.win, (0, 0, 255), b_sol['pos'], 30)
            else:
                pg.draw.circle(self.win, (0, 0, 255), b_sol['pos'], 30)
        for r_sol in data['pr']['soldiers']:
            if r_sol['selected']:
                pg.draw.circle(self.win, (255, 255, 0), r_sol['pos'], 32)
                pg.draw.circle(self.win, (255, 0, 0), r_sol['pos'], 30)
            else:
                pg.draw.circle(self.win, (255, 0, 0), r_sol['pos'], 30)
