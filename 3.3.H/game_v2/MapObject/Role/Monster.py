from .Role import Role



class Monster(Role):
    def __init__(self, x, y, game_map) -> None:
        super().__init__(x, y, game_map)
    
    def _set_symbol(self):
        self.symbol = 'M'

    def _set_hp(self):
        self.hp = 1
    
    def move(self):
        pass

    def attack(self):
        pass

    def be_attacked(self, damage):
        self.hp -= damage
        self.check_is_alive()

    def touch(self):
        pass
    