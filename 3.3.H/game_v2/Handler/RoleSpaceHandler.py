from . import CollisionHandler


class RoleSpaceHandler(CollisionHandler):
    def collision_condition(self, player, target):
        from game_v2.MapObject import Space
        return isinstance(target, Space)

    def collision_result(self, player, target, map):
        print(f"角色 {player.symbol} 碰到了空地 角色移動 ~ ")
        # TODO 移動
    