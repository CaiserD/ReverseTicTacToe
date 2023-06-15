import pygame as pg
import sys
from random import randint

WIN_SIZE = 900
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')
vec2 = pg.math.Vector2


class GameLogic:
    def __init__(self, game):
        self.game = game
        self.field_image = self.get_scaled_image(path='Resource/field.png', res=[WIN_SIZE] * 2)
        self.O_image = self.get_scaled_image(path='Resource/o.png', res =[CELL_SIZE] * 2)
        self.X_image = self.get_scaled_image(path='Resource/x.png', res =[CELL_SIZE] * 2)
        
        #1 mean X and 0 means O, otherwise all empty spaces are infinity (INF)
        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]
        self.player = randint(0, 1)
        
    #Launching the Game Main Process    
    def run_game_process(self):
        current_cell = vec2(pg.mouse.get_pos()) // CELL_SIZE
        col, row = map(int, current_cell)
        left_click = pg.mouse.get_pressed()[0]
        
        if left_click and self.game_array[row][col] == INF:
            self.game_array[row][col] = self.player
            self.player = not self.player

    #Display Gameplay
    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                if obj != INF:
                    self.game.screen.blit(self.X_image if obj else self.O_image, vec2(x, y) * CELL_SIZE)
        
    #Display the Pictures
    def draw(self):
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()
        
    #Importing Pictures
    @staticmethod
    def get_scaled_image(path, res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img, res)
    
    #Print Current Player as Caption of the Window
    def print_caption(self):
        pg.display.set_caption(f'Player "{"OX"[self.player]}" turn!')
    
    #General Run Method
    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = GameLogic(self)

    # Check Exit from Application
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):  # Run game
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()