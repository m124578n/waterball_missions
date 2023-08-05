from typing import TYPE_CHECKING
from .Role import Role
from game_v2 import MapObject
from game_v2.Handler import CollisionHandler
if TYPE_CHECKING:
    from .Monster import Monster
    from game_v2.Map import Map


class Character(Role):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
        super().__init__(x, y, game_map)
    
    def _set_symbol(self):
        # ↑→↓←
        self.symbol = '↑'

    def _set_damage(self):
        self.damage = 1000

    def _set_hp(self):
        self.hp = 300

    def touch(self):
        pass

    def change_symbol(self, symbol):
        self.symbol = symbol
    
    def take_turn(self):
        print("玩家的回合~")
        choose = input("請選擇你的動作 (a)move (b)attack : ")
        if choose == 'a':
            around_objects: dict = self.map.find_around_objects(self)
            move_choose = input("請選擇要前進的方向 wasd : ")
            target = around_objects.get(move_choose, None)
            if target is None:
                print("你的移動不合法 ! ")
            else:
                self.handler.collision(self, target[0])
                self.change_symbol(target[1])
        elif choose == 'b':
            # targets = self.map.find_all_monsters()
            targets: list = self.map.find_attack_target_objects(self)
            print(f"攻擊了怪物 {targets}！")
            self.attack(targets)
            
