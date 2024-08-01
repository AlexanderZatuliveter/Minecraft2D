from PIL import Image, ImageDraw
import time

# Загрузите изображение спрайтов
sprite_sheet = Image.open('steve.png')

# Определите координаты ног в спрайт-листе
# Предположим, что у нас есть два спрайта ног: (x, y, width, height)
left_leg1 = sprite_sheet.crop((0, 0, 16, 32))  # координаты для первой ноги
left_leg2 = sprite_sheet.crop((16, 0, 32, 32))  # координаты для второй ноги

right_leg1 = sprite_sheet.crop((32, 0, 48, 32))  # координаты для первой ноги
right_leg2 = sprite_sheet.crop((48, 0, 64, 32))  # координаты для второй ноги

# Создаем новое изображение для анимации
animation = []

# Создаем последовательность кадров
for i in range(10):
    if i % 2 == 0:
        frame = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
        frame.paste(left_leg1, (16, 16))
        frame.paste(right_leg2, (32, 16))
    else:
        frame = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
        frame.paste(left_leg2, (16, 16))
        frame.paste(right_leg1, (32, 16))
    animation.append(frame)

# Сохраните анимацию как gif
animation[0].save('steve_walking.gif', save_all=True, append_images=animation[1:], duration=100, loop=0)

# Отображение анимации
animation[0].show()
