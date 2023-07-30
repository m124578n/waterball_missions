from .CollisionHandler import CollisionHandler
from game.MapObject import MapObject
from game.MapObject import Treasure


class CharacterTreasureHandler(CollisionHandler):
    def collision(self, player, target: MapObject):
        if isinstance(target.object, Treasure):
            return True
        if self.next is None:
            return False
        else:
            result = self.next.collision(player, target)
            return result
