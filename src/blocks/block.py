import pygame

# from utils import Utils


class Block(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = None
        self.is_solid = False
