from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game_v2.Map import Map


class MapObject(ABC):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
        self.symbol = None
        self.map = game_map
        self.x = x
        self.y = y
        self._set_symbol()
    
    @abstractmethod
    def _set_symbol(self):
        pass

    def __repr__(self) -> str:
        return self.symbol
    