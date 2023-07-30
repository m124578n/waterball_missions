from .MapObject import MapObject


class Obstacle(MapObject):
    def __init__(self):
        super().__init__()
        self.set_symbol()

    def set_symbol(self):
        self.symbol = '□'
