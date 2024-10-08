import sys
import pygame
from game_field import GameField
from player_view import PlayerView
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, BLOCK_SIZE, HALF_BLOCK_SIZE
from blocks import block


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
        self.is_moving_left = False
        self.hit_force = 5

    def __fall(self):

        # top collision check
        if self.velocity_y < 0 and not self._can_walk_to(self.x, self.y):
            self.velocity_y = 0

        if self._can_walk_to(self.x+4, self.y + BLOCK_SIZE * 3):
            self.velocity_y += self.gravity_force
            self.y += self.velocity_y
        else:
            self.velocity_y = 0

    def _get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, 30, 90)

    def update(self):
        self.__fall()
        left, middle, right = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if left:
            self._game_field.hit_block(mouse_x + self.x - HALF_SCREEN_WIDTH, mouse_y +
                                       self.y - HALF_SCREEN_HEIGHT, self.hit_force)
        if right:
            self._game_field.put_block(mouse_x + self.x - HALF_SCREEN_WIDTH, mouse_y + self.y - HALF_SCREEN_HEIGHT)

        keys = pygame.key.get_pressed()
        is_moving = False

        if keys[pygame.K_d]:
            is_moving = self._move_right()
            self.is_moving_left = False

        if keys[pygame.K_a]:
            is_moving = self._move_left()
            self.is_moving_left = True

        # can jump only if on the ground (velocity_y == 0)
        if keys[pygame.K_SPACE] and self.velocity_y == 0:
            self.velocity_y = self.jump_force
            self.y -= 3
            is_moving = True

        self.is_moving = is_moving
        self.player_view.update_image(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, self.is_moving, self.is_moving_left)

    def _move_right(self) -> bool:

        if not self._can_walk_to(self.x + BLOCK_SIZE, self.y + HALF_BLOCK_SIZE):
            return False

        if not self._can_walk_to(self.x + BLOCK_SIZE, self.y + BLOCK_SIZE + HALF_BLOCK_SIZE):
            return False

        if not self._can_walk_to(self.x + BLOCK_SIZE, self.y + BLOCK_SIZE + BLOCK_SIZE + HALF_BLOCK_SIZE):
            return False

        self.x += self.speed

        return True

    def _move_left(self) -> bool:

        if not self._can_walk_to(self.x - HALF_BLOCK_SIZE / 2, self.y + HALF_BLOCK_SIZE):
            return False

        if not self._can_walk_to(self.x - HALF_BLOCK_SIZE / 2, self.y + BLOCK_SIZE + HALF_BLOCK_SIZE):
            return False

        if not self._can_walk_to(self.x - HALF_BLOCK_SIZE / 2, self.y + BLOCK_SIZE + BLOCK_SIZE + HALF_BLOCK_SIZE):
            return False

        self.x -= self.speed

        return True

    def _can_walk_to(self, x, y):
        block = self._game_field.get_block(x, y)

        if block:
            block_rect = self._game_field.get_block_rect(x, y, self)
            if not block_rect.colliderect(self._get_rect()):
                return False

        return True
