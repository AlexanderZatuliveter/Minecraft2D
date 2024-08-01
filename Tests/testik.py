import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 367, 769
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Steve Walking Animation")

# Загрузка изображения Стива
steve_image = pygame.image.load('steve.png')
steve_rect = steve_image.get_rect()

# Настройка начальных координат ног
left_leg_up = True

# Функция для отрисовки Стива с анимацией ног
def draw_steve(x, y, frame):
    screen.blit(steve_image, (x, y))

    # Определение положения ног
    if frame < 10:
        offset = frame  # Движение ног вверх
    else:
        offset = 20 - frame  # Движение ног вниз
    
    # Изменение положения ног
    screen.blit(steve_image, (x, y - offset))
    screen.blit(steve_image, (x, y + offset))

# Основной игровой цикл
clock = pygame.time.Clock()
x, y = 0, 0
frame = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление экрана
    screen.fill((255, 255, 255))

    # Обновление положения ног
    draw_steve(x, y, frame)
    frame = (frame + 1) % 20

    # Обновление дисплея и задержка
    pygame.display.flip()
    clock.tick(10)