import pygame
from utils import Utils


class PlayerView(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        utils = Utils()

        self._body_left_image = utils.load_image('sprites/body_left.png')
        self._body_left_image_rect = self._body_left_image.get_rect()

        self._body_right_image = utils.load_image('sprites/body_right.png')
        self._body_right_image_rect = self._body_right_image.get_rect()

        self._leg_image = utils.load_image('sprites/leg.png')
        self._leg_image_rect = self._leg_image.get_rect()

        self.leg_rotate = 0
        self.leg_rotate_direction = 1

        self._arm_image = utils.load_image('sprites/arm.png')
        self._arm_image_rect = self._arm_image.get_rect()

        self.arm_rotate = 0
        self.arm_rotate_direction = 1

        self._max_rotate_angle = 25

    def update_image(self, x, y, is_moving, is_moving_left):
        self.image = pygame.Surface((x + 30, y + 90), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        if is_moving:
            self._update_legs()
            self._update_arms()

        self._blit_arm(self._arm_image, x, y, -self.arm_rotate)
        self._blit_leg(self._leg_image, x, y, self.leg_rotate)

        if is_moving_left:
            self.image.blit(self._body_left_image, (x, y))
        else:
            self.image.blit(self._body_right_image, (x, y))

        self._blit_leg(self._leg_image, x, y, -self.leg_rotate)
        self._blit_arm(self._arm_image, x, y, self.arm_rotate)

    def _update_legs(self):
        if abs(self.leg_rotate) >= self._max_rotate_angle:
            self.leg_rotate_direction = -self.leg_rotate_direction
        self.leg_rotate += self.leg_rotate_direction

    def _update_arms(self):
        if abs(self.arm_rotate) >= self._max_rotate_angle:
            self.arm_rotate_direction = -self.arm_rotate_direction
        self.arm_rotate += self.arm_rotate_direction

    def _blit_leg(self, leg_image, x, y, angle):
        leg = pygame.transform.rotate(leg_image, angle)
        leg_center = leg.get_rect(center=leg_image.get_rect().center)
        self.image.blit(leg, (leg_center.x + x + 3, leg_center.y + y + 24))

    def _blit_arm(self, arm_image, x, y, angle):
        arm = pygame.transform.rotate(arm_image, angle)
        arm_center = arm.get_rect(center=arm_image.get_rect().center)
        self.image.blit(arm, (arm_center.x + x + 4, arm_center.y + y + 1))
