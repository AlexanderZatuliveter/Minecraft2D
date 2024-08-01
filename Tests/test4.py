import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Анимация шагающего человека")

# Устанавливаем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Загружаем изображение человека
person_image = pygame.image.load("chel.png")

# Создаем поверхность для ног
legs_surface = pygame.Surface((person_image.get_width(), person_image.get_height()), pygame.SRCALPHA)

# Устанавливаем параметры анимации
frame_count = 4
frame_delay = 200  # Задержка между кадрами в миллисекундах
last_update = pygame.time.get_ticks()
current_frame = 0

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время
    now = pygame.time.get_ticks()

    # Проверяем, прошло ли достаточно времени для переключения кадра
    if now - last_update > frame_delay:
        current_frame = (current_frame + 1) % frame_count
        last_update = now

    # Заполнение экрана белым цветом
    screen.fill(WHITE)

    # Копируем исходное изображение на экран
    screen.blit(person_image, (screen_width // 2 - person_image.get_width() // 2, screen_height // 2 - person_image.get_height() // 2))

    # Рисуем ноги в зависимости от текущего кадра
    legs_surface.fill((0, 0, 0, 0))  # Очищаем поверхность для ног
    if current_frame == 0:
        pygame.draw.line(legs_surface, BLACK, (30, 100), (20, 140), 5)  # Левая нога
        pygame.draw.line(legs_surface, BLACK, (50, 100), (60, 140), 5)  # Правая нога
    elif current_frame == 1:
        pygame.draw.line(legs_surface, BLACK, (30, 100), (40, 140), 5)
        pygame.draw.line(legs_surface, BLACK, (50, 100), (40, 140), 5)
    elif current_frame == 2:
        pygame.draw.line(legs_surface, BLACK, (30, 100), (40, 140), 5)
        pygame.draw.line(legs_surface, BLACK, (50, 100), (60, 140), 5)
    elif current_frame == 3:
        pygame.draw.line(legs_surface, BLACK, (30, 100), (20, 140), 5)
        pygame.draw.line(legs_surface, BLACK, (50, 100), (40, 140), 5)

    # Накладываем поверхность с ногами на экран
    screen.blit(legs_surface, (screen_width // 2 - person_image.get_width() // 2, screen_height // 2 - person_image.get_height() // 2))

    # Обновление экрана
    pygame.display.flip()

    # Задержка для ограничения скорости кадров
    pygame.time.delay(30)

# Завершение работы Pygame
pygame.quit()
sys.exit()