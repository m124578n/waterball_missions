from .Role import Role



class Monster(Role):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
    
    def _set_symbol(self):
        self.symbol = 'M'

    def _set_hp(self):
        self.hp = 1
    
    def move(self):
        pass

    def attack(self):
        pass

    def touch(self):
        pass
    