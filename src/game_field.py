import random
import pygame
import numpy as np
from blocks import Stone, Dirt, Bedrock
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, BLOCK_SIZE


class GameField:
    def __init__(self, x, y):
        self.field = np.zeros(shape=(x, y), dtype=object)
        self.field.fill(None)

        for i in range(x):
            self.field[i][0] = Bedrock()
            self.field[i][y-1] = Bedrock()

        for j in range(y):
            self.field[0][j] = Bedrock()
            self.field[x-1][j] = Bedrock()

        for n in range(200):
            rand_x = random.randint(1, x-2)
            rand_y = random.randint(1, y-2)
            self.field[rand_x][rand_y] = random.choice((Dirt(), Stone()))

        self.__block_size = 24

    def update(self):
        for (x, y), block in np.ndenumerate(self.field):
            if block is not None:
                block.update()

    def draw(self, screen, player):
        for (bx, by), block in np.ndenumerate(self.field):
            if block is not None:
                pos = self._get_block_position(player, bx, by)
                block.draw(screen, pos)

    def _get_block_position(self, player, bx, by):
        return (
            bx * self.__block_size - player.x + HALF_SCREEN_WIDTH,
            by * self.__block_size - player.y + HALF_SCREEN_HEIGHT
        )

    def get_block_rect(self, x, y, player) -> pygame.Rect:
        pos = self.get_block_field_position(x, y)
        screen_pos = self._get_block_position(player, pos[0], pos[1])
        return pygame.Rect(screen_pos[0], screen_pos[1], BLOCK_SIZE, BLOCK_SIZE)

    def get_block_field_position(self, x, y):
        return (
            int(x // self.__block_size),
            int(y // self.__block_size)
        )

    def drop_block(self, x, y):
        pos = self.get_block_field_position(x, y)
        block = self.field[pos[0]][pos[1]]
        if block:
            block.health -= 1
            if block.health <= 0:
                self.field[pos[0]][pos[1]] = None
                if block.sound:
                    self._mp3_play(block.sound)

    def put_block(self, x, y):
        pos = self.get_block_field_position(x, y)
        block = self.field[pos[0]][pos[1]]
        if block == None:
            self.field[pos[0]][pos[1]] = random.choice((Stone(), Dirt()))
            self._mp3_play(self.field[pos[0]][pos[1]].sound)

    def get_block(self, x, y):
        pos = self.get_block_field_position(x, y)
        block = self.field[pos[0]][pos[1]]
        return block

    def is_solid(self, x, y):
        block = self.get_block(x, y)
        if block is None:
            return False
        if block.strength >= 1:
            return False
        return block.is_solid

    def enumerate(self):
        return [value for index, value in np.ndenumerate(self.field) if value is not None]

    def _mp3_play(self, path):
        self.sound = pygame.mixer.Sound(path)
        self.sound.play()
