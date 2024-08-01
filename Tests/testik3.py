import pygame
import sys
from PIL import Image, ImageSequence

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Steve Walking Animation")

# Загрузка GIF-файла и извлечение кадров
gif_image = Image.open(r"C:\Users\Alex\Desktop\Steve.gif")
frames = []

# Цвет фона (в данном случае зеленый)
background_color = (0, 255, 0)

# Извлечение кадров из GIF и удаление фона
for frame in ImageSequence.Iterator(gif_image):
    frame = frame.convert("RGBA")
    datas = frame.getdata()

    new_frame = []
    for item in datas:
        # Измените это условие на цвет фона вашего GIF
        if item[:3] == background_color:
            new_frame.append((255, 255, 255, 0))  # прозрачный цвет
        else:
            new_frame.append(item)

    frame.putdata(new_frame)
    frame_image = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
    frames.append(frame_image)

# Основной игровой цикл
clock = pygame.time.Clock()
x, y = screen_width // 2, screen_height // 2
frame_index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление экрана
    screen.fill((255, 255, 255))

    # Отрисовка текущего кадра
    screen.blit(frames[frame_index], (x, y))
    frame_index = (frame_index + 1) % len(frames)

    # Обновление дисплея и задержка
    pygame.display.flip()
    clock.tick(10)