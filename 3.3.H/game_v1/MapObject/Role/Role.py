from ..MapObject import MapObject


class Role(MapObject):
    def __init__(self):
        super().__init__()
        self.hp: int = 0

    def set_hp(self):
        return NotImplementedError
