from __future__ import annotations

from Sprite import Sprite
from Hero import Hero
from Water import Water
from Fire import Fire
import random
from Coord import Coord
from CollisionHandler import CollisionHandler


class World:
    def __init__(self, sprites: list[Sprite], handler: CollisionHandler | None):
        self.length = 30
        self.world = None
        self.sprites = [sprite for sprite in sprites]
        self.handler = handler

    def create_world(self):
        self.world = [Coord(x) for x in range(30)]
        random_coord = random.sample(range(30), 10)
        for x in random_coord:
            self.world[x].set_sprite(random.choice(self.sprites))

    def move(self, x1: int, x2: int):
        self.world = self.handler.collision(self.world, self.world[x1], self.world[x2])
