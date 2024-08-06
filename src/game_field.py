import random
import numpy as np

from blocks import Block, Stone

class GameField:
    def __init__(self, x, y):
        #self.sprites = pygame.sprite.Group()
        self.field = np.zeros((x, y), dtype=Block)
        for n in range(0, 100):
            rand_x = random.randint(1, x-1)
            rand_y = random.randint(1, y-1)
            #print(f"{rand_x=}, {rand_y=}")
            self.field[rand_x][rand_y] = Stone()

    def update(self):
        for block in np.nditer(self.field):
            block.update()
        
    def draw(self, screen):
        for block in np.nditer(self.field):
            block.draw(screen)
        