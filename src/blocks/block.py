import pygame

#from utils import Utils

class Block(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        #utils = Utils()
        self.image = None
        #self.image = utils.load_image('sprites/blocks/empty_block.png')