from .Role import Role
from game_v2 import Map
from game_v2.MapObject import (
        Space,
        Treasure,
        MapObject
    )
from game_v2.Handler import CollisionHandler


class Character(Role):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
    
    def _set_symbol(self):
        # ↑→↓←
        self.symbol = '↑'

    def _set_hp(self):
        self.hp = 300
    
    def move(self, target: MapObject, map: Map) -> bool:
        map.move_object_to_target(self, target)
        
    def attack(self):
        pass

    def touch(self):
        pass
    
    def take_turn(self, map: Map, collision_handler: CollisionHandler):
        print("玩家的回合~")
        choose = input("請選擇你的動作 (a)move (b)attack : ")
        if choose == 'a':
            around_objects: dict = map.find_around_objects(self)
            move_choose = input("請選擇要前進的方向 wasd : ")
            target = around_objects.get(move_choose, None)
            if target is None:
                print("你的移動不合法 ! ")
            else:
                collision_handler.collision(self, target, map)
        elif choose == 'b':
            pass
