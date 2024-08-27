import pygame
from game_field import GameField
from player_view import PlayerView


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, game_field: GameField):
        super().__init__()
        self.speed = 3
        self.is_moving = False
        self.x = x
        self.y = y
        self.player_view = PlayerView()
        self._game_field = game_field
        self.gravity_force = 0.2
        self.fall_time = 0

    def gravity(self):
        if not self._game_field.is_solid(self.x, self.y+75):
            self.fall_time += 0.7
            self.y += self.gravity_force * self.fall_time
        else:
            self.fall_time = 0

    def update(self):
        self.gravity()
        keys = pygame.key.get_pressed()
        is_moving = False
        if keys[pygame.K_d] and self.x < 1175:
            self.x += self.speed
            is_moving = True
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed
            is_moving = True
        if keys[pygame.K_SPACE] and self.y > 0:
            self.y -= 15
            self.gravity()
            is_moving = True
        self.is_moving = is_moving
        self.player_view._update_image(self.x, self.y, self.is_moving)
