from __future__ import annotations
from Coord import Coord
from abc import ABC, abstractmethod


class CollisionHandler(ABC):
    def __init__(self, handler: "CollisionHandler" | None):
        self.next = handler

    def collision(self, world: list[Coord], x1: Coord, x2: Coord) -> list[Coord]:
        if x1.sprite is not None:
            if self.check_sprite_condition(x1, x2):
                world = self.do_sprite_collision(world, x1, x2)
                return world
            elif self.next is not None:
                self.next.collision(world, x1, x2)
                return world
        else:
            print("移動無效")
            return world

    @abstractmethod
    def check_sprite_condition(self, x1: Coord, x2: Coord) -> bool:
        return True

    @abstractmethod
    def do_sprite_collision(self, world: list[Coord], x1: Coord, x2: Coord) -> list[Coord]:
        pass

