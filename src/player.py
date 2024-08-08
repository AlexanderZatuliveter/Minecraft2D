import pygame
from player_view import PlayerView


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.speed = 3
        self.is_moving = False
        self.x = x
        self.y = y
        self.player_view = PlayerView()

    def update(self):
        keys = pygame.key.get_pressed()
        is_moving = False
        if keys[pygame.K_d] and self.x < 1175:
            self.x += self.speed
            is_moving = True
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed
            is_moving = True
        if keys[pygame.K_s] and self.y < 500:
            self.y += self.speed
            is_moving = True
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed
            is_moving = True
        self.is_moving = is_moving
        self.player_view._update_image(self.x, self.y, self.is_moving)
