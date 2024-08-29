import random
import numpy as np
from blocks import Stone, Dirt
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH

class GameField:
    def __init__(self, x, y):
        self.field = np.zeros(shape=(x, y), dtype=object)
        self.field.fill(None)

        for i in range(x):  
            self.field[i][0] = random.choice((Dirt(), Stone()))
            self.field[i][y-1] = random.choice((Dirt(), Stone()))

        for j in range(y):
            self.field[0][j] = random.choice((Dirt(), Stone()))
            self.field[x-1][j] = random.choice((Dirt(), Stone()))

        for n in range(100):
            rand_x = random.randint(1, x-1)
            rand_y = random.randint(1, y-1)
            self.field[rand_x][rand_y] = random.choice((Dirt(), Stone()))

        self.__block_size = 24

    def update(self):
        for (x, y), block in np.ndenumerate(self.field):
            if block is not None: block.update()

    def draw(self, screen, player):
        for (x, y), block in np.ndenumerate(self.field):
            if block is not None and block.image:
                screen.blit(
                    block.image, 
                    ( 
                        x * self.__block_size - player.x + HALF_SCREEN_WIDTH,
                        y * self.__block_size - player.y + HALF_SCREEN_HEIGHT
                    )
                )

    def is_solid(self, x, y):
        xpos = int(x / self.__block_size)
        ypos = int(y / self.__block_size)
        block = self.field[xpos][ypos]
        if block is None: return False
        return block.is_solid

    def enumerate(self):
        return [value for index, value in np.ndenumerate(self.field) if value is not None]
