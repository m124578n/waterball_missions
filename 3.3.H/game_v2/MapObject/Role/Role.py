from typing import TYPE_CHECKING
from ..MapObject import MapObject
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from game_v2.Map import Map


class Role(MapObject, ABC):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
        super().__init__(x, y, game_map)
        self._set_hp()
    
    @abstractmethod
    def _set_hp(self):
        pass

    @abstractmethod
    def move(self, map):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def touch(self):
        pass
