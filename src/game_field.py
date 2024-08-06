import random
import numpy as np

from blocks import Block, Stone

class GameField:
    def __init__(self, x, y):
        #self.sprites = pygame.sprite.Group()
        self.field = np.zeros((x, y), dtype=object)
        for i in range(x):
            for j in range(y):
                self.field[i][j] = Stone()
        # for n in range(0, 100):
        #     rand_x = random.randint(1, x-1)
        #     rand_y = random.randint(1, y-1)
        #     #print(f"{rand_x=}, {rand_y=}")
        #     self.field[rand_x][rand_y] = Stone()

    def update(self):
        for i in np.nditer(self.field, flags=['refs_ok'], op_flags=['readwrite']):
            i.item().update()
        
    def draw(self, screen):
        # for i in np.nditer(self.field, flags=['refs_ok'], op_flags=['readwrite']):
        #     i.item().draw(screen)
        pass