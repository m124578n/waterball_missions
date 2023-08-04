from . import CollisionHandler


class RoleSameHandler(CollisionHandler):
    def collision_condition(self, player, target) -> bool:
        return type(player) == type(target)

    def collision_result(self, player, target):
        print(f"角色 {player.symbol} 碰撞了 {target.symbol} 無法前進 ~ ")
    