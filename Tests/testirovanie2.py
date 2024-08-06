import numpy as np
import pygame
import sys

# Параметры изображения
width, height = 100, 100  # Размеры изображения
num_cells = 200  # Количество случайных клеточек
cell_size = 5  # Размер клетки в пикселях

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((width * cell_size, height * cell_size))
pygame.display.set_caption('Random Cells')

# Создаем пустое изображение (черное)
image = np.zeros((height, width), dtype=np.uint8)

# Генерируем случайные координаты
x_coords = np.random.randint(0, width, num_cells)
y_coords = np.random.randint(0, height, num_cells)

# Устанавливаем пиксели в белый цвет (255)
for x, y in zip(x_coords, y_coords):
    image[y, x] = 255

# Преобразуем массив в поверхность Pygame
surface = pygame.surfarray.make_surface(np.stack([image]*3, axis=-1))

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Отображаем изображение
    screen.blit(pygame.transform.scale(surface, (width * cell_size, height * cell_size)), (0, 0))
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
sys.exit()