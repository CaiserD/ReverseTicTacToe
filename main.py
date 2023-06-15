import pygame as pg
import sys
from random import randint

WIN_SIZE = 900

pg.init()


class GameLogic:
    def __init__(self, game):
        self.game = game
        self.field_image = self.get_scaled_image()

    @staticmethod
    def get_scaled_image(path, res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img, res)

    def run(self):
        pass


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