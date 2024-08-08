import pygame
import sys
from camera import Camera
from game_field import GameField
from player import Player

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

camera = Camera(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

all_sprites = pygame.sprite.Group()

game_field = GameField(50, 40)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update()
    game_field.update()
    camera.update(player.x, player.y)

    screen.fill((135, 206, 235))
    game_field.draw(screen)
    screen.blit(player.player_view.image, player.player_view.image.get_rect())

    pygame.display.flip()

    clock.tick(60)
