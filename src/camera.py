import pygame


class Camera:
    def __init__(self, screen_width, screen_height):
        self.camera = pygame.Rect(0, 0, screen_width, screen_height)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = target.rect.centerx + int(self.screen_width / 2)
        y = target.rect.centery + int(self.screen_height / 2)

        # x = min(0, x)
        # y = min(0, y)
        # x = max(-(self.world_width - self.screen_width), x)
        # y = max(-(self.world_height - self.screen_height), y)

        self.camera = pygame.Rect(x, y, self.screen_width, self.screen_height)