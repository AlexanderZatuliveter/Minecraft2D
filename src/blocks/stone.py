from blocks.block import Block
from utils import Utils


class Stone(Block):
    def __init__(self) -> None:
        super().__init__()
        utils = Utils()
        self.image = utils.load_image('sprites/blocks/stone.png')
        self.is_solid = True
