import pygame
import sys
from camera import Camera
from player import Player

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

world_width = 10000
world_height = 10000
camera = Camera(world_width, world_height)

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 500, 500)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    all_sprites.update()
    camera.update(player)

    screen.fill((135, 206, 235))
    all_sprites.draw(screen)
    pygame.display.flip()


    clock.tick(60)