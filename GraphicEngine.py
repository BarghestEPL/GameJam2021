import pygame as pg
import numpy as np


class GraphicEngine:
    def __init__(self, win):
        self.win = win
        self.circle_radius = 30
        self.selected_circle_radius = 32
        self.gun_width = 5
        self.gun_length = 40

    def render_soldier(self, soldier, color):
        cx, cy = (self.selected_circle_radius*2, self.selected_circle_radius*2)
        soldier_surface = pg.Surface((self.selected_circle_radius*4+1, self.selected_circle_radius*4+1), pg.SRCALPHA, 32)
        
        x, y = soldier["pos"]
        if soldier["selected"]:
            pg.draw.circle(soldier_surface, (255, 255, 0), (cx, cy), self.selected_circle_radius)
        pg.draw.circle(soldier_surface, color, (cx, cy), self.circle_radius)
        pg.draw.rect(soldier_surface, (0, 0, 0), pg.Rect(cx - self.gun_width/2, cy-self.gun_length, self.gun_width, self.gun_length))

        soldier_surface = pg.transform.rotate(soldier_surface, soldier["ang"])

        self.win.blit(soldier_surface, (x, y))

    def render(self, data):
        background_color = "#7f5539"
        self.win.fill(background_color)

        self.load_arena()


        for soldier in data['pb']['soldiers']:
            self.render_soldier(soldier, (0, 0, 255))

        for soldier in data['pr']['soldiers']:
            self.render_soldier(soldier, (255, 0, 0))

    def load_arena(self):

        color_tiles = [
                    "#7f5539", # Background
                    "#495057", # Walls
                    "#fcf6bd", # Vote counts
                    "#f94144", # Red spawn
                    "#48bfe3", # Blue spawn
                ]
        arena = np.array([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 4, 4, 4, 4, 1, 0, 0, 2, 2, 2, 2, 0, 0, 1, 4, 4, 4, 4, 1],
            [1, 4, 4, 4, 4, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 4, 4, 4, 4, 1],
            [1, 4, 4, 4, 4, 1, 0, 0, 2, 2, 2, 2, 0, 0, 1, 4, 4, 4, 4, 1],
            [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
            [1, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 1],
            [1, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 1],
            [1, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])

        tile_size = 32
        tile_surface = pg.Surface((tile_size, tile_size))
        for i in range(len(arena)):
            for j in range(len(arena[0])):
                tile_surface.fill(color_tiles[arena[i][j]])
                self.win.blit(tile_surface, (j*tile_size, i*tile_size)) 

if __name__ == "__main__":
    fps = 60
    dt = 1 / fps
    width, height = 1280, 800

    pg.init()
    clock = pg.time.Clock()
    pg.display.set_caption('Louvain-li-Nux 2021')
    font = pg.font.SysFont("comicsansms", 24)
    screen = pg.display.set_mode((width, height))


    GE = GraphicEngine(screen)

    data = {'pr': {"soldiers": [{"pos": (100, 100), "selected": True, "ang": 90}]},
            'pb': {"soldiers": [{"pos": (200, 200), "selected": False, "ang": 270}]}}

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        GE.render(data)
        pg.display.flip()
        dt = clock.tick(fps)
