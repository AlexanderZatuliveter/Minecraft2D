import pygame
import sys
from camera import Camera
from game_field import GameField
from player import Player

pygame.init()

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

camera = Camera(screen_width // 2, screen_height // 2)

game_field = GameField(50, 33)

player = Player(screen_width // 2, screen_height // 2, game_field)

all_sprites = pygame.sprite.Group()

all_sprites.add(player.player_view)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update()
    game_field.update()
    camera.update(player.player_view)
    all_sprites.update()

    screen.fill((135, 206, 235))
    game_field.draw(screen)
    screen.blit(player.player_view.image, player.player_view.image.get_rect())

    for entity in all_sprites:
        screen.blit(entity.image, camera.apply(entity))

    pygame.display.flip()
    clock.tick(60)
