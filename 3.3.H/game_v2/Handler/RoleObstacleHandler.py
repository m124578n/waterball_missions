from . import CollisionHandler


class RoleObstacleHandler(CollisionHandler):
    def collision_condition(self, player, target) -> bool:
        from game_v2.MapObject import Obstacle
        return isinstance(target, Obstacle)

    def collision_result(self, player, target):
        print(f"角色 {player.symbol} 遇上了 障礙物 {target.symbol} 無法前進 ~")
    