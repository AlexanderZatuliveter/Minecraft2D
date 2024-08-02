import pygame

class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.speed = 5  
        
        body_image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/body.png')
        leg_image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/leg.png')
        
        self._images = [body_image, leg_image]
        self._x = x
        self._y = y

        self._update_image()

    def _get_combined_width(self):
        return max(self._x + img.get_width() for img in self._images)

    def _get_combined_height(self):
        return max(self._y + img.get_height() for img in self._images)

    def _update_image(self):        
        self.image = pygame.Surface((self._get_combined_width(), self._get_combined_height()), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))  # Clear the surface with transparency
        for img in self._images:
            self.image.blit(img, (self._x, self._y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self._x += self.speed
        if keys[pygame.K_a]:
            self._x -= self.speed
        if keys[pygame.K_s]:
            self._y += self.speed
        if keys[pygame.K_w]:
            self._y -= self.speed
        self._update_image()
