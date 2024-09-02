from blocks.block import Block


class Stone(Block):
    def __init__(self) -> None:
        super().__init__()
        self._load_image('sprites/blocks/stone.png')
        self.is_solid = True
        self.sound = "src/sounds/stone1.mp3"
        self.health = 50
