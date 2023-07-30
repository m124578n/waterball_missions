from .CollisionHandler import CollisionHandler
from game.MapObject import MapObject


class CharacterNoneHandler(CollisionHandler):
    def collision(self, player, target: MapObject):
        if target.object is None:
            return True
        if self.next is None:
            return False
        else:
            result = self.next.collision(player, target)
            return result
