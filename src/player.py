import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/body.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5    

        self.leg_image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/leg.png')
        self.leg_rect = self.leg_image.get_rect()
        self.leg_rect.center = (x, y)
        self.leg_rotate = 0
        self.leg_rotate_direction = 1
        self.max_rotate_angle = 25

    def update(self):      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.x > 0:
            self.rect.x += self.speed
            self.leg_rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.leg_rect.x -= self.speed
        if keys[pygame.K_s] and self.rect.y > 0:
            self.rect.y += self.speed
            self.leg_rect.y += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.leg_rect.y -= self.speed

        self.rotated_leg = pygame.transform.rotate(self.leg_image, self.leg_rotate)
        self.rotated_leg_rect = self.rotated_leg.get_rect(center=self.leg_rect.center)

        if abs(self.leg_rotate) >= self.max_rotate_angle:
            self.leg_rotate_direction = -self.leg_rotate_direction

        self.leg_rotate += self.leg_rotate_direction


    def draw(self, surface):
        surface.blit(self.body_image, self.rect)
        surface.blit(self.rotated_leg, self.rotated_leg_rect)
