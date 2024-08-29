import pygame
from blocks.block import Block
from utils import Utils


class Dirt(Block):
    def __init__(self) -> None:
        utils = Utils()
        self.image = utils.load_image('sprites/blocks/dirt.png')
        self.is_solid = True