import sys
from blocks.block import Block


class Bedrock(Block):
    def __init__(self) -> None:
        super().__init__()
        self._load_block_image('sprites/blocks/bedrock.png')
        self.is_solid = True
        self.health = self.max_health = sys.maxsize
