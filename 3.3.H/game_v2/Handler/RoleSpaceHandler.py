from . import CollisionHandler


class RoleSpaceHandler(CollisionHandler):
    def collision_condition(self, player, target) -> bool:
        from game_v2.MapObject import Space
        return isinstance(target, Space)

    def collision_result(self, player, target):
        print(f"角色 {player.symbol} 碰到了空地 角色移動 ~ ")
        player.move(target)
    