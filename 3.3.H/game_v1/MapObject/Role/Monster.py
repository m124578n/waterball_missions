from .Role import Role


class Monster(Role):
    def __init__(self):
        super().__init__()
        self.set_symbol()
        self.set_hp()

    def set_symbol(self):
        self.symbol = 'M'

    def set_hp(self):
        self.hp = 1
