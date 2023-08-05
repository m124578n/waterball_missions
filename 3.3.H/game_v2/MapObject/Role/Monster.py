from typing import TYPE_CHECKING
import random
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

    def _set_damage(self):
        self.damage = 50

    def touch(self):
        pass

    def take_turn(self):
        targets = self.map.find_around_objects(self)
        character = self.find_character_in(targets)
        if character:
            self.attack(character)
        else:
            step = 'wasd'
            target = targets.get(random.choice(step), None)
            if target is not None:
                self.handler.collision(self, target[0])

    def find_character_in(self, targets):
        from .Character import Character
        for target in targets.values():
            if isinstance(target[0], Character):
                return [target[0]]
        return None

    