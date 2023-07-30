from __future__ import annotations

from CollisionHandler import CollisionHandler
from Coord import Coord
from functions import change, set_world


class HeroWaterHandler(CollisionHandler):
    def __init__(self, handler: CollisionHandler | None):
        super().__init__(handler)
        self.sprites = "H", "W"

    def check_sprite_condition(self, x1: Coord, x2: Coord) -> bool:
        return x1.sprite.name in self.sprites and x2.sprite.name in self.sprites and x1.sprite.name != x2.sprite.name

    def do_sprite_collision(self, world: list[Coord], x1: Coord, x2: Coord) -> list[Coord]:
        print(f"生命：{x1.sprite} {x2.sprite}發生碰撞～英雄單位加10hp～")
        if x1.sprite.name == "H":
            x1.sprite.hp += 10
            x2.sprite = None
            print(f"生命{x1.sprite}已移動至{x2.x}")
            world = set_world(world, x1, x2)
            world = change(world, x1, x2)
        elif x2.sprite.name == "H":
            x2.sprite.hp += 10
            x1.sprite = None
            world = set_world(world, x1, x2)
        return world



