import numpy as np
import pygame

class GameField:
    def __init__(self, x, y):
        #self.sprites = pygame.sprite.Group()
        self.field = np.zeros((x, y), dtype=pygame.sprite.Sprite)

    def update(self):
        pass
        #self.sprites.update()
        
    def draw(self, screen):
        pass
        #self.sprites.draw(screen)
        