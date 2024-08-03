import os
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()        
        self.speed = 5
        base_path = os.path.dirname(__file__)         
        self._body_image = pygame.image.load(os.path.join(base_path, 'sprites/body.png'))
        self._leg_image = pygame.image.load(os.path.join(base_path, 'sprites/leg.png')) 
        self._leg_image_rect = self._leg_image.get_rect()
        self._x = x
        self._y = y
        self.leg_rotate = 0
        self._max_rotate_angle = 25
        self._leg_rotate_direction = 1

    def _update_image(self):
        self.image = pygame.Surface((self._x + 250, self._y + 900), pygame.SRCALPHA)
        self.rect = self.image.get_rect()        
        self.image.blit(self._body_image, (self._x, self._y))
        self._update_legs()

    def _update_legs(self):
        if abs(self.leg_rotate) >= self._max_rotate_angle:
            self._leg_rotate_direction = -self._leg_rotate_direction
        self.leg_rotate += self._leg_rotate_direction
        self._blit_leg(self._leg_image, self.leg_rotate)
        self._blit_leg(self._leg_image, -self.leg_rotate)
    
    def _blit_leg(self, leg_image, angle):
        leg = pygame.transform.rotate(leg_image, angle)
        leg_center = leg.get_rect(center=leg_image.get_rect().center)
        self.image.blit(leg, (leg_center.x + self._x + 30, leg_center.y + self._y + 240))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self._x < 1010:
            self._x += self.speed
        if keys[pygame.K_a] and self._x > 0:
            self._x -= self.speed
        if keys[pygame.K_s] and self._y < 100:
            self._y += self.speed
        if keys[pygame.K_w] and self._y > 0:
            self._y -= self.speed
        self._update_image()