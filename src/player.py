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

        self._arm_image = pygame.image.load(os.path.join(base_path, 'sprites/arm.png')) 
        self._arm_image_rect = self._arm_image.get_rect()

        self._x = x
        self._y = y

        self.leg_rotate = 0
        self.arm_rotate = 0
        self._max_rotate_angle = 25
        self.leg_rotate_direction = 1
        self.arm_rotate_direction = 1

    def _update_image(self):
        self.image = pygame.Surface((self._x + 250, self._y + 900), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self._update_legs()
        self._update_arms()

        self._blit_arm(self._arm_image, -self.arm_rotate)
        self._blit_leg(self._leg_image, self.leg_rotate)

        self.image.blit(self._body_image, (self._x, self._y))
        
        self._blit_leg(self._leg_image, -self.leg_rotate)
        self._blit_arm(self._arm_image, self.arm_rotate)

    def _update_legs(self):
        if abs(self.leg_rotate) >= self._max_rotate_angle:
            self.leg_rotate_direction = -self.leg_rotate_direction
        self.leg_rotate += self.leg_rotate_direction

    def _update_arms(self):
        if abs(self.arm_rotate) >= self._max_rotate_angle:
            self.arm_rotate_direction = -self.arm_rotate_direction
        self.arm_rotate += self.arm_rotate_direction
    
    def _blit_leg(self, leg_image, angle):
        leg = pygame.transform.rotate(leg_image, angle)
        leg_center = leg.get_rect(center=leg_image.get_rect().center)
        self.image.blit(leg, (leg_center.x + self._x + 30, leg_center.y + self._y + 240))

    def _blit_arm(self, arm_image, angle):
        arm = pygame.transform.rotate(arm_image, angle)
        arm_center = arm.get_rect(center=arm_image.get_rect().center)
        self.image.blit(arm, (arm_center.x + self._x + 45, arm_center.y + self._y + 10))

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