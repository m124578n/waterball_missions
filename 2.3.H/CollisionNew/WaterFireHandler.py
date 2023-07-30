from __future__ import annotations

from CollisionHandler import CollisionHandler
from Coord import Coord
from functions import set_world


class WaterFireHandler(CollisionHandler):
    def __init__(self, handler: CollisionHandler | None):
        super().__init__(handler)
        self.sprites = "W", "F"

    def check_sprite_condition(self, x1: Coord, x2: Coord) -> bool:
        return x1.sprite.name in self.sprites and x2.sprite.name in self.sprites and x1.sprite.name != x2.sprite.name

    def do_sprite_collision(self, world: list[Coord], x1: Coord, x2: Coord) -> list[Coord]:
        print(f"生命：{x1.sprite} {x1.sprite}碰撞，水火交融，雙方消散")
        x1.sprite = None
        x2.sprite = None
        return set_world(world, x1, x2)
