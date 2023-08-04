from ..MapObject import MapObject
from abc import ABC, abstractmethod


class Role(MapObject, ABC):
    def __init__(self, x, y, game_map) -> None:
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
