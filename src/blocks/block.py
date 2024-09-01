import pygame
from utils import Utils


class Block(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = None
        self.rect = None
        self.is_solid = False

    def _load_image(self, path):
        utils = Utils()
        self.image = utils.load_image(path)
        self.rect = self.image.get_rect()