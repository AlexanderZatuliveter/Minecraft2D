import time
import pygame
from utils import Utils


class Block(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self._utils = Utils()
        self.rect = None
        self.is_solid = False
        self.health = 1
        self.sound = None
        self.max_health = 1
        self.crack_images = [self._utils.load_image(f"sprites/block_cracks/crack{num}.png") for num in range(1, 5)]
        self.__crack_images_len = len(self.crack_images)

    def _load_block_image(self, path):
        self.image = self._utils.load_image(path)
        self.rect = self.image.get_rect()

    def draw(self, screen, pos):
        if self.image:
            screen.blit(self.image, pos)
            self.draw_cracks(screen, pos)

    def draw_cracks(self, screen, pos):
        fl = (self.health / self.max_health) * self.__crack_images_len
        number = self.__crack_images_len - int(fl)
        # print(f"{number=}, {self.health=}")
        if number > 0:
            screen.blit(self.crack_images[number-1], pos)
