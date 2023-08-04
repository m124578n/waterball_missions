from typing import TYPE_CHECKING
from .MapObject import MapObject
if TYPE_CHECKING:
    from game_v2.Map import Map


class Space(MapObject):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
        super().__init__(x, y, game_map)

    def _set_symbol(self) -> None:
        self.symbol = '-'
