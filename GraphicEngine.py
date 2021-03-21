import pygame as pg
import numpy as np
from const import *

arena = np.array([
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 3, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 1],
[1, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1],
[1, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1],
[1, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1],
[1, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])


class GraphicEngine:
    def __init__(self, win):
        self.win = win
        self.rad = SOLDIER_RAD
        self.gun_width = GUN_WIDTH

    def render_soldier(self, soldier, color):
        pos= pg.Vector2(soldier["pos"])
        if soldier["selected"]:
            pg.draw.circle(self.win, SELECTED_COLOR, pos, self.rad + 2)
        pg.draw.circle(self.win, color, pos, self.rad)

        aim = pg.Vector2(soldier["aim"])
        if not soldier["counting"]:
            pg.draw.line(self.win, GUN_COLOR, pos, aim, self.gun_width)

    def load_arena(self):
        tile_size = TILE_SIZE
        tile_surface = pg.Surface((tile_size, tile_size))
        for i in range(len(arena)):
            for j in range(len(arena[0])):
                tile_surface.fill(TILES_COLOR[arena[i][j]])
                self.win.blit(tile_surface, (j*tile_size, i*tile_size)) 

    def render(self, data):
        if data["state"][:4] == "game":
            self.win.fill(TILES_COLOR[0])
            self.load_arena()
            font = pg.font.SysFont("comicsansms", 24)
           
            score_counting = font.render(str(int(data["score_counting"])), False, COUNTING_COLOR)
            score_counting = pg.transform.scale(score_counting, (5*TILE_SIZE, 5*TILE_SIZE))
            self.win.blit(score_counting, (7*TILE_SIZE, 13*TILE_SIZE))

            time_remaining = font.render("TIME: " + str(int(data["time_remaining"])), False, TIME_COLOR)
            time_remaining = pg.transform.scale(time_remaining, (3*TILE_SIZE, TILE_SIZE))
            self.win.blit(time_remaining, (35*TILE_SIZE, 0))

            score_blue = font.render(str(data["pr"]["nb_killed"]), False, BLUE_FONT_COLOR)
            score_blue = pg.transform.scale(score_blue, (3*TILE_SIZE, 3*TILE_SIZE))
            self.win.blit(score_blue,(WIDTH - 5*TILE_SIZE, 2*TILE_SIZE))
            
            score_red = font.render(str(data["pb"]["nb_killed"]), False, RED_FONT_COLOR)
            score_red = pg.transform.scale(score_red, (3*TILE_SIZE, 3*TILE_SIZE))
            self.win.blit(score_red,(2*TILE_SIZE, 2*TILE_SIZE))


            for soldier in data['pb']['soldiers']:
                self.render_soldier(soldier, BLUE_COLOR if not soldier['dead'] else DEAD_COLOR)

            for soldier in data['pr']['soldiers']:
                self.render_soldier(soldier, RED_COLOR if not soldier['dead'] else DEAD_COLOR)

            if "bu" in data: 
                for bullet in data['bu']:
                    if bullet['color'] == "red":
                        pg.draw.circle(self.win, RED_COLOR, bullet['pos'], 10)
                    else:
                        pg.draw.circle(self.win, BLUE_COLOR, bullet['pos'], 10)
                
        elif data["state"][:3] == "end":
            self.win.fill(TILES_COLOR[1])
            font = pg.font.SysFont("comicsansms", 52)

            s = font.render("GAME %c FINISHED" % data["state"][3], False, TIME_COLOR)
            self.win.blit(s, (5*TILE_SIZE, int(HEIGHT/2)-2*TILE_SIZE))
            
            s = font.render("DEMOCRATS GOT %d VOTES" % data["score_counting"], False, TIME_COLOR)
            self.win.blit(s, (5*TILE_SIZE, int(HEIGHT/2)+1*TILE_SIZE))

        elif data["state"][:3] == "sta":
            self.win.fill(TILES_COLOR[0])
            font = pg.font.SysFont("comicsansms", 52)
           
            game_nb = data["state"][5] 

            s = font.render("GAME %c STARTING" % game_nb, False, TIME_COLOR)
            self.win.blit(s, (5*TILE_SIZE, int(HEIGHT/2)-2*TILE_SIZE))
            
            s = font.render("GOOD LUCK!", False, TIME_COLOR)
            self.win.blit(s, (5*TILE_SIZE, int(HEIGHT/2)+1*TILE_SIZE))

        elif data["state"] == "final":
            self.win.fill(TILES_COLOR[0])
            font = pg.font.SysFont("comicsansms", 52)

            if data["winner"] != 0:
                s = font.render("PLAYER %d WON THE GAME" % data["winner"], False, TIME_COLOR)
            else:
                s = font.render("IT'S A DRAW!", False, TIME_COLOR)
            self.win.blit(s, (5*TILE_SIZE, int(HEIGHT/2)-2*TILE_SIZE))



