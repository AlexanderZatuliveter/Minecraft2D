import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установим размеры окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rotate and Move Sprite")

# Загрузка спрайта
sprite_image = pygame.image.load('C:/Users/Alex/Desktop/Python Projects/Games/Minecraft_2D/Data/arm.png')
sprite_rect = sprite_image.get_rect()

# Установим начальные координаты спрайта
sprite_rect.center = (400, 300)

# Установим начальный угол поворота
angle = 0

def rotate(self):
    now = pygame.time.get_ticks()
    if now - self.last_update > 50:
        self.last_update = now
        self.rot = (self.rot + self.rot_speed) % 360
        new_image = pygame.transform.rotate(self.image_orig, self.rot)
        old_center = self.rect.center
        self.image = new_image
        self.rect = self.image.get_rect()
        self.rect.center = old_center

rotated_rect = None

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление координат спрайта (например, перемещение по нажатию клавиш)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        sprite_rect.x += 5
    if keys[pygame.K_UP]:
        sprite_rect.y -= 5
    if keys[pygame.K_DOWN]:
        sprite_rect.y += 5

    # Обновление угла поворота (например, вращение по нажатию клавиш)
    if keys[pygame.K_a]:
        angle += 1
    if keys[pygame.K_d]:
        angle -= 1

    # Очистка экранаddd
    screen.fill((255, 255, 255))

    # Вращение и отрисовка спрайта
    rotated_image = pygame.transform.rotate(sprite_image, angle)
    rotated_rect = rotated_image.get_rect(topleft=[sprite_rect.x, sprite_rect.y])
    screen.blit(rotated_image, rotated_rect.center)

    #new_image = pygame.transform.rotate(self.image_orig, self.rot)
    # old_center = self.rect.center
    # self.image = new_image
    # self.rect = self.image.get_rect()
    # self.rect.center = old_center

    # Для корректного отображения сместим спрайт
    #offset = pygame.math.Vector2(sprite_image.get_size()) / 2
    # offset = pygame.math.Vector2(sprite_image.get_width(), -sprite_image.get_height()) / 2
    # rotated_rect.center += offset

    # Обновление экрана
    pygame.display.flip()

    # Ограничение количества кадров в секунду
    pygame.time.Clock().tick(60)
