from __future__ import annotations

from CollisionHandler import CollisionHandler
from Coord import Coord


class IsSameHandler(CollisionHandler):
    def __init__(self, handler: CollisionHandler | None):
        super().__init__(handler)

    def check_sprite_condition(self, x1: Coord, x2: Coord) -> bool:
        return x1.sprite.name == x2.sprite.name

    def do_sprite_collision(self, world: list[Coord], x1: Coord, x2: Coord) -> list[Coord]:
        print(f"生命：{x1.sprite} {x1.sprite}碰撞，沒發生任何事")
        return world




