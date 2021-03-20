import pygame as pg

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
        pg.draw.rect(soldier_surface, (0, 255, 0), pg.Rect(cx - self.gun_width/2, cy-self.gun_length, self.gun_width, self.gun_length))
        soldier_surface = pg.transform.rotate(soldier_surface, soldier["ang"])
        self.win.blit(soldier_surface, (x, y))

    def render(self, data):
        for soldier in data['pb']['soldiers']:
            self.render_soldier(soldier, (0, 0, 255))

        for soldier in data['pr']['soldiers']:
            self.render_soldier(soldier, (255, 0, 0))

if __name__ == "__main__":
    fps = 60
    dt = 1 / fps
    width, height = 800, 600

    pg.init()
    clock = pg.time.Clock()
    pg.display.set_caption('Louvain-li-Nux 2021')
    font = pg.font.SysFont("comicsansms", 24)
    screen = pg.display.set_mode((width, height))

    screen.fill([255, 255, 255])

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

