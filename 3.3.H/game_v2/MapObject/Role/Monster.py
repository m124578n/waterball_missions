from typing import TYPE_CHECKING
from .Role import Role
if TYPE_CHECKING:
    from .Character import Character
    from game_v2.Map import Map


class Monster(Role):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
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
    