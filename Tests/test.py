import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, move_enabled, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.__move_enabled = move_enabled

    def update(self):
        if not self.__move_enabled: return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(SCREEN_HEIGHT / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - SCREEN_WIDTH), x)
        y = max(-(self.height - SCREEN_HEIGHT), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)

green = (0, 255, 0)
blue = (0, 0, 255)
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, move_enabled=True, color=green)
player2 = Player(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, move_enabled=False, color=blue)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(player2)

world_width = 2000
world_height = 2000
camera = Camera(world_width, world_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()
    camera.update(player)

    screen.fill((135, 206, 235))
    for entity in all_sprites:
        screen.blit(entity.image, camera.apply(entity))

    pygame.display.flip()
    clock.tick(60)
