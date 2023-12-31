from . import CollisionHandler


class RoleTreasureHandler(CollisionHandler):
    def collision_condition(self, player, target) -> bool:
        from game_v2.MapObject import Treasure
        return isinstance(target, Treasure)

    def collision_result(self, player, target):
        print(f"角色 {player.symbol} 遇到了寶物 {target.symbol} !!")
        player.touch(target)
    