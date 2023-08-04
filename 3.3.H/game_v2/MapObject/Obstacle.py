from .MapObject import MapObject


class Obstacle(MapObject):
    def __init__(self, x, y, game_map) -> None:
        super().__init__(x, y, game_map)
    
    def _set_symbol(self):
        self.symbol = '□'
