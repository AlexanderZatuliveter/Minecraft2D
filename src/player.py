import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()        
        self.speed = 5          
        self._body_image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/body.png')
        self._leg_image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/leg.png')  
        self._leg_image_rect = self._leg_image.get_rect()
        self._images = [self._body_image, self._leg_image]
        self._x = x
        self._y = y
        self.leg_rotate = 0
        self._max_rotate_angle = 25
        self._leg_rotate_direction = 1
        self.leg_rotate2 = 0
        self._leg_rotate_direction2 = -1
        self._update_image()

    def _update_image(self):
        rotated_leg = pygame.transform.rotate(self._leg_image, self.leg_rotate)
        rotated_leg_rect = rotated_leg.get_rect(center=self._leg_image_rect.center)
        rotated_leg2 = pygame.transform.rotate(self._leg_image, self.leg_rotate2)
        rotated_leg_rect2 = rotated_leg2.get_rect(center=self._leg_image_rect.center)

        if abs(self.leg_rotate) >= self._max_rotate_angle:
            self._leg_rotate_direction = -self._leg_rotate_direction
        if abs(self.leg_rotate2) <= -self._max_rotate_angle:
            self._leg_rotate_direction = self._leg_rotate_direction

        self.leg_rotate += self._leg_rotate_direction
        self.leg_rotate2 -= self._leg_rotate_direction
    
        self.image = pygame.Surface((self._x + 250, self._y + 900), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self._body_image, (self._x, self._y))
        self.image.blit(rotated_leg, (rotated_leg_rect[0] + self._x + 35, rotated_leg_rect[1] + self._y +240))
        self.image.blit(rotated_leg2, (rotated_leg_rect2[0] + self._x + 25, rotated_leg_rect2[1] + self._y +240))

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