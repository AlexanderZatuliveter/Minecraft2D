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

# Координаты для ног в исходном изображении
# Предположим, что ноги Стива находятся в нижней части изображения
leg_height = 290 # высота ног
leg_y = steve_rect.height - leg_height  # координата Y для ног

# Настройка начальных координат ног
left_leg_up = True

# Функция для отрисовки Стива с анимацией ног
def draw_steve(x, y, frame):
    # Разделение изображения на верхнюю часть и ноги
    upper_body = steve_image.subsurface((0, 0, steve_rect.width, leg_y))
    left_leg = steve_image.subsurface((0, leg_y, steve_rect.width // 2, leg_height))
    right_leg = steve_image.subsurface((steve_rect.width // 2, leg_y, steve_rect.width // 2, leg_height))

    # Определение положения ног
    if frame < 10:
        left_leg_offset = frame  # Движение левой ноги вверх
        right_leg_offset = 10 - frame  # Движение правой ноги вниз
    else:
        left_leg_offset = 20 - frame  # Движение левой ноги вниз
        right_leg_offset = frame - 10  # Движение правой ноги вверх

    # Отрисовка верхней части тела
    screen.blit(upper_body, (x, y))

    # Отрисовка ног с изменением положения
    screen.blit(left_leg, (x, y + leg_y + left_leg_offset))
    screen.blit(right_leg, (x + steve_rect.width // 2, y + leg_y + right_leg_offset))

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
