from typing import TYPE_CHECKING
from .Role import Role
if TYPE_CHECKING:
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

    def _set_max_hp(self):
        self.max_hp = 300

    def change_symbol(self, symbol):
        self.symbol = symbol

    def show_status(self):
        print(self.map)
        print(f"玩家現在血量 {self.hp} 狀態 {self.state}")

    def choose(self):
        while True:
            choose = input(f"請選擇你的動作 {self.can_choose} : ")
            if choose in self.can_choose:
                break
        return choose

    def move_step(self):
        around_objects: dict = self.map.find_around_objects(self)
        while True:
            move_choose = input(f"請選擇要前進的方向 {self.can_move_step} : ")
            target = around_objects.get(move_choose, None)
            if move_choose not in self.can_move_step:
                print("你的移動不合法 ! ")
            elif target is None:
                print("你的移動不合法 ! ")
            else:
                break
        self.handler.collision(self, target[0])
        self.change_symbol(target[1])

    def default_attack(self):
        return self.map.find_attack_target_objects(self)
