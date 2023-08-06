from typing import TYPE_CHECKING
import random
from .Content import (
    AcceleratingPotion,
    DevilFruit,
    DokodemoDoor,
    Poison,
    KingsRock,
    SuperStar,
    HealingPotion
)
from game_v2.MapObject import MapObject
if TYPE_CHECKING:
    from game_v2.Map import Map

# contents = [
#     [SuperStar(), 0.1],
#     [Poison(), 0.25],
#     [AcceleratingPotion(), 0.2],
#     [HealingPotion(), 0.15],
#     [DevilFruit(), 100],
#     [KingsRock(), 0.1],
#     [DokodemoDoor(), 0.1],
# ]
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
