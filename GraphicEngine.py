import pygame as pg


class GraphicEngine:
    def __init__(self, win):
        self.win = win
        self.circle_radius = 30
        self.gun_width = 5
        self.gun_length = 30

    def render(self, data):
        for soldier in data['pb']['soldiers']:
            x, y = soldier["pos"]
            pg.draw.circle(self.win, (0, 0, 255), (x, y), self.circle_radius)
            pg.draw.rect(self.win, (0, 255, 0), pg.Rect(x+self.circle_radius - self.gun_width/2, y - self.gun_length, self.gun_width, self.gun_length))

        for soldier in data['pr']['soldiers']:
            x, y = soldier["pos"]
            pg.draw.circle(self.win, (255, 0, 0), (x, y), self.circle_radius)
            pg.draw.rect(self.win, (0, 255, 0), pg.Rect(x+self.circle_radius - self.gun_width/2, y - self.gun_length, self.gun_width, self.gun_length))



if __name__ == "__main__":
    fps = 60
    dt = 1 / fps
    width, height = 800, 600

    pg.init()
    clock = pg.time.Clock()
    pg.display.set_caption('Louvain-li-Nux 2021')
    font = pg.font.SysFont("comicsansms", 24)
    screen = pg.display.set_mode((width, height))

    GE = GraphicEngine(screen)

    data = {'pr': {"soldiers": [{"pos": (100, 100)}]},
            'pb': {"soldiers": [{"pos": (200, 200)}]}}

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        GE.render(data)
        pg.display.flip()
        dt = clock.tick(fps)
