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

# Функция для рисования человека в разных фазах шага
def draw_person(screen, phase, x, y):
    # Голова
    pygame.draw.circle(screen, BLACK, (x, y), 20)
    
    # Тело
    pygame.draw.line(screen, BLACK, (x, y + 20), (x, y + 80), 5)
    
    # Руки в зависимости от фазы
    if phase in [0, 2]:
        pygame.draw.line(screen, BLACK, (x, y + 40), (x - 20, y + 60), 5)
        pygame.draw.line(screen, BLACK, (x, y + 40), (x + 20, y + 60), 5)
    else:
        pygame.draw.line(screen, BLACK, (x, y + 40), (x - 30, y + 50), 5)
        pygame.draw.line(screen, BLACK, (x, y + 40), (x + 30, y + 50), 5)

    # Ноги в зависимости от фазы
    if phase == 0:
        pygame.draw.line(screen, BLACK, (x, y + 80), (x - 20, y + 100), 5)
        pygame.draw.line(screen, BLACK, (x, y + 80), (x + 20, y + 100), 5)
    elif phase == 1:
        pygame.draw.line(screen, BLACK, (x, y + 80), (x - 10, y + 100), 5)
        pygame.draw.line(screen, BLACK, (x, y + 80), (x + 30, y + 100), 5)
    elif phase == 2:
        pygame.draw.line(screen, BLACK, (x, y + 80), (x + 20, y + 100), 5)
        pygame.draw.line(screen, BLACK, (x, y + 80), (x - 20, y + 100), 5)
    elif phase == 3:
        pygame.draw.line(screen, BLACK, (x, y + 80), (x + 10, y + 100), 5)
        pygame.draw.line(screen, BLACK, (x, y + 80), (x - 30, y + 100), 5)

# Устанавливаем начальные параметры
current_frame = 0
frame_count = 4
frame_delay = 200  # Задержка между кадрами в миллисекундах
last_update = pygame.time.get_ticks()

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

    # Рисуем текущий кадр анимации
    draw_person(screen, current_frame, screen_width // 2, screen_height // 2)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для ограничения скорости кадров
    pygame.time.delay(30)

# Завершение работы Pygame
pygame.quit()
sys.exit()