
class MapObject:
    """
    所有地圖物件的媽媽
    """
    def __init__(self):
        self.symbol = '-'
        self.object = None
        self.x: int | None = None
        self.y: int | None = None

    def __repr__(self):
        if self.object is not None:
            return self.object.symbol
        else:
            return self.symbol

    def set_symbol(self):
        raise NotImplementedError

    def set_coord(self, x: int, y: int):
        self.x = x
        self.y = y

