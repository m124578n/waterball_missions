from .MapObject import MapObject


class Space(MapObject):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def _set_symbol(self):
        self.symbol = '-'
