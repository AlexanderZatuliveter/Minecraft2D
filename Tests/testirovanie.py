import pygame
import sys
import numpy as np

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Array in Pygame")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Размер клетки
tile_size = 5

# Создание двумерного массива (матрицы) игрового уровня
level = np.zeros((50, 100))

# # Добавление строки
new_row = np.zeros((1, 100))
level = np.vstack((level, new_row))

# # Добавление столбца
new_column = np.zeros((51, 100))
array = np.hstack((level, new_column))

# print(array)


# # генерация уровня
# for row in range(0, 50):
#     level.append([0, 1, 0] * 50)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана белым цветом
    screen.fill(WHITE)

    # Отрисовка уровня
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col * tile_size, row * tile_size, tile_size, tile_size))
            else:
                pygame.draw.rect(screen, BLACK, (col * tile_size, row * tile_size, tile_size, tile_size))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()