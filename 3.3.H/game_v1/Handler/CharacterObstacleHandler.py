from .CollisionHandler import CollisionHandler
from game.MapObject import MapObject
from game.MapObject import Obstacle


class CharacterObstacleHandler(CollisionHandler):
    def collision(self, player, target: MapObject):
        if isinstance(target.object, Obstacle):
            return False
        if self.next is None:
            return False
        else:
            result = self.next.collision(player, target)
            return result
