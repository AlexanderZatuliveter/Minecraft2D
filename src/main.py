import pygame
import sys
from game_field import GameField
from player import Player
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#camera = Camera(screen_width // 2, screen_height // 2)

game_field = GameField(50, 33)

player = Player(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, game_field)


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update()
    game_field.update()
    #camera.update(player.player_view)

    screen.fill((135, 206, 235))
    game_field.draw(screen, player)
    screen.blit(player.player_view.image, player.player_view.image.get_rect())

    # for entity in game_field.enumerate():
    #     screen.blit(entity.image, camera.apply(entity))

    pygame.display.flip()
    clock.tick(60)
