from blocks.block import Block


class Dirt(Block):
    def __init__(self) -> None:
        super().__init__()
        self._load_image('sprites/blocks/dirt.png')
        self.is_solid = True
        self.sound = "src/sounds/grass1.mp3"
        self.health = 10