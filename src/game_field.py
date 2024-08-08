import random
import numpy as np

from blocks import Block, Stone


class GameField:
    def __init__(self, x, y):
        self.field = np.zeros((x, y), dtype=object)
        for i in range(x):
            for j in range(y):
                self.field[i][j] = Block()
        for n in range(0, 100):
            rand_x = random.randint(1, x-1)
            rand_y = random.randint(1, y-1)
            self.field[rand_x][rand_y] = Stone()
        self.__block_size = 24

    def update(self):
        for (x, y), block in np.ndenumerate(self.field):
            block.update()

    def draw(self, screen):
        for (x, y), block in np.ndenumerate(self.field):
            if block.image:
                screen.blit(block.image, (x * self.__block_size, y * self.__block_size))

    def is_solid(self, x, y):
        xpos = int(x / self.__block_size)
        ypos = int(y / self.__block_size)
        return self.field[xpos][ypos].is_solid
