from blocks.block import Block


class Bedrock(Block):
    def __init__(self) -> None:
        super().__init__()
        self._load_image('sprites/blocks/bedrock.png')
        self.is_solid = True
        # self.sound = "src/sounds/stone1.mp3"
