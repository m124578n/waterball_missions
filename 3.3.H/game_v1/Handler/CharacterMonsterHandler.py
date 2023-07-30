from .CollisionHandler import CollisionHandler
from game.MapObject import MapObject
from game.MapObject import Monster


class CharacterMonsterHandler(CollisionHandler):
    def collision(self, player, target: MapObject):
        if isinstance(target.object, Monster):
            return False
        if self.next is None:
            return False
        else:
            result = self.next.collision(player, target)
            return result
