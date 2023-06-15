import pygame as pg
import sys
from random import randint

WIN_SIZE = 900

pg.init()

class Game(): 
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
    
    #Check Exit from Application
    def check_events(self): 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    
    def run(self): #Run game
        while True:
            self.check_events()
            pg.display.update()
            self.clock.tick(60)
    
if __name__ == "__main__":
    game = Game()
    game.run()