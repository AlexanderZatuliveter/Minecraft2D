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
        self.jump_force = -6
        self.velocity_y = 0

    def __fall(self):
        if not self.__is_solid():
            self.velocity_y += self.gravity_force
            self.y += self.velocity_y
        else:
            self.velocity_y = 0

    def __is_solid(self):
        return self._game_field.is_solid(self.x+8, self.y+75)
    
    def update(self):
        self.__fall()
        keys = pygame.key.get_pressed()
        is_moving = False
        if keys[pygame.K_d]:
            self.x += self.speed
            is_moving = True
        if keys[pygame.K_a]:
            self.x -= self.speed
            is_moving = True
        if keys[pygame.K_SPACE] and self.__is_solid():
            self.velocity_y = self.jump_force
            self.y -= 3
            is_moving = True
        self.is_moving = is_moving
        #self.player_view.update_image(self.x, self.y, self.is_moving)
        self.player_view.update_image(600, 400, self.is_moving)
