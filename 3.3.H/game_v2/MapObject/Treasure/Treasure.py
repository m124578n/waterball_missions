from typing import TYPE_CHECKING
import random
from game_v2.MapObject import MapObject
if TYPE_CHECKING:
    from game_v2.Map import Map
from game_v2 import config


class Treasure(MapObject):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
        super().__init__(x, y, game_map)
        self.content = None
        self._set_content()

    def _set_symbol(self) -> None:
        self.symbol = 'X'

    def _set_content(self) -> None:
        contents_list = [c[0] for c in config.contents]
        contents_weights = [c[1] for c in config.contents]
        content = random.choices(contents_list, weights=contents_weights, k=1)
        self.content = content[0]

    def get_state(self):
        return self.content.state
