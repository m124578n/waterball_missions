from typing import TYPE_CHECKING
import random
from .Role import Role
if TYPE_CHECKING:
    from .Character import Character
    from game_v2.Map import Map
    from game_v2.MapObject import Treasure


class Monster(Role):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
        super().__init__(x, y, game_map)
    
    def _set_symbol(self):
        self.symbol = 'M'

    def _set_hp(self):
        self.hp = 1

    def _set_max_hp(self):
        self.max_hp = 1

    def _set_damage(self):
        self.damage = 50

    def choose(self):
        character = self.get_attack_targets()
        if character:
            return "b"
        else:
            return "a"

    def move_step(self):
        targets = self.map.find_around_objects(self)
        target = targets.get(random.choice(self.can_move_step), None)
        if target is not None:
            self.handler.collision(self, target[0])

    def default_attack(self):
        from .Character import Character
        targets = self.map.find_around_objects(self)
        for target in targets.values():
            if isinstance(target[0], Character):
                return [target[0]]
        return None
    