from typing import TYPE_CHECKING
from ..MapObject import MapObject
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from game_v2.Map import Map
    from game_v2.Handler import CollisionHandler


class Role(MapObject, ABC):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
        super().__init__(x, y, game_map)
        self.hp = 0
        self.damage = 0
        self.handler = None
        self.state = None
        self._set_hp()
        self._set_damage()
    
    @abstractmethod
    def _set_hp(self):
        pass

    @abstractmethod
    def _set_damage(self):
        pass

    def move(self, target):
        self.map.move_object_to_target(self, target)

    def attack(self, targets):
        for target in targets:
            target.be_attacked(self.damage)

    @abstractmethod
    def touch(self):
        pass

    @abstractmethod
    def take_turn(self):
        pass

    def set_collision_handler(self, handler: 'CollisionHandler'):
        self.handler = handler

    def be_attacked(self, damage):
        self.hp -= damage
        print(f"角色 {self.symbol} 受到 {damage} 攻擊！")
        if not self.check_is_alive():
            print(f"角色 {self.symbol} 已死亡")
            self.map.remove_object_with_coord(self.x, self.y)

    def check_is_alive(self) -> bool:
        return self.hp > 0
