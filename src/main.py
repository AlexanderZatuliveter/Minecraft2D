import pygame
import sys
from camera import Camera
from player import Player
from player2 import Player2

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

world_width = 1200
world_height = 800
camera = Camera(world_width, world_height)

player = Player2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    all_sprites.update()
    camera.update(player)

    screen.fill((135, 206, 235))
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)