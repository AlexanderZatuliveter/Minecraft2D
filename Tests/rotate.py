import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

leg_x = (screen_width // 2)+8
leg_y = (screen_height // 2)+130

leg2_x = (screen_width // 2)-8
leg2_y = (screen_height // 2)+130

leg_image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/leg.png')

leg_rect = leg_image.get_rect()
leg_rect.center = (leg_x, leg_y)

leg2_rect = leg_image.get_rect()
leg2_rect.center = (leg2_x, leg2_y)

leg_angle = 25

leg_rotate = leg_angle
leg2_rotate = -leg_angle

leg_rotate_direction = 1

body_x = screen_width // 2
body_y = (screen_height // 2)-150

body_image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/body.png')
body_rect = body_image.get_rect()
body_rect.center = (body_x, body_y)

arm_x = screen_width // 2
arm_y = (screen_height // 2)-150

arm2_x = screen_width // 2
arm2_y = (screen_height // 2)-150

arm_image = pygame.image.load('C:/Users/Dev/Desktop/Python Projects/Minecraft_2D/Data/arm.png')

arm_rect = arm_image.get_rect()
arm_rect.center = (arm_x, arm_y)

arm2_rect = arm_image.get_rect()
arm2_rect.center = (arm2_x, arm2_y)

arm_angle = 20

arm_rotate = arm_angle
arm2_rotate = -arm_angle

arm_rotate_direction = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    rotated_leg = pygame.transform.rotate(leg_image, leg_rotate)
    rotated_leg_rect = rotated_leg.get_rect(center=leg_rect.center)

    rotated_leg2 = pygame.transform.rotate(leg_image, leg2_rotate)
    rotated_leg2_rect = rotated_leg2.get_rect(center=leg2_rect.center)

    rotated_arm = pygame.transform.rotate(arm_image, arm_rotate)
    rotated_arm_rect = rotated_arm.get_rect(center=arm_rect.center)

    rotated_arm2 = pygame.transform.rotate(arm_image, arm2_rotate)
    rotated_arm2_rect = rotated_arm2.get_rect(center=arm2_rect.center)

    # Отрисовка повернутого спрайта на экране
    screen.blit(rotated_leg, rotated_leg_rect)
    screen.blit(rotated_leg2, rotated_leg2_rect)

    screen.blit(rotated_arm2, rotated_arm2_rect)
    
    screen.blit(body_image, body_rect)

    screen.blit(rotated_arm, rotated_arm_rect)

    pygame.display.flip()
    clock.tick(60)

    if abs(leg_rotate) >= leg_angle:
        leg_rotate_direction = -leg_rotate_direction
    elif abs(leg2_rotate) <= -leg_angle:
        leg_rotate_direction = leg_rotate_direction

    leg_rotate += arm_rotate_direction    
    leg2_rotate -= arm_rotate_direction

    if abs(arm_rotate) <= arm_angle:
        arm_rotate_direction = arm_rotate_direction
    elif abs(arm2_rotate) >= -arm_angle:
        arm_rotate_direction = -arm_rotate_direction

    arm_rotate += arm_rotate_direction    
    arm2_rotate -= arm_rotate_direction
    
pygame.quit()
sys.exit()