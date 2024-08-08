import pygame


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, x, y):
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - self.width), x)
        y = max(-(self.width - self.height), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)
