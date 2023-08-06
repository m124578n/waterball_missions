from . import CollisionHandler


class RoleDifferentHandler(CollisionHandler):
    def collision_condition(self, player, target) -> bool:
        from game_v2.MapObject import Character, Monster
        class_t = (Character, Monster)
        return isinstance(player, class_t) and isinstance(target, class_t)

    def collision_result(self, player, target):
        print(f"角色 {player.symbol} 遇上了角色 {target.symbol} 無法移動 ~ ")
    