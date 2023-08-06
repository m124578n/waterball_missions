from typing import TYPE_CHECKING
from ..MapObject import MapObject
from abc import ABC, abstractmethod
from game_v2.State import Normal, Invincible

if TYPE_CHECKING:
    from game_v2.Map import Map
    from game_v2.Handler import CollisionHandler
    from game_v2.MapObject import Treasure
    from game_v2.State import State


class Role(MapObject, ABC):
    def __init__(self, x: int, y: int, game_map: 'Map') -> None:
        super().__init__(x, y, game_map)
        self.invincible = False
        self.max_hp = 0
        self.hp = 0
        self.damage = 0
        self.handler = None
        self.state: State | None = None
        self.attack_targets = None
        self.be_attacked_entry_state = Invincible
        self.turn = 1
        self.can_choose = "(a)move (b)attack"
        self.can_move_step = "wasd"
        self._set_hp()
        self._set_max_hp()
        self._set_damage()
        self._set_default_state()

    @abstractmethod
    def _set_hp(self):
        pass

    @abstractmethod
    def _set_max_hp(self):
        pass

    @abstractmethod
    def _set_damage(self):
        pass

    def _set_default_state(self):
        self.entry_state(Normal)

    def entry_state(self, state):
        state = state(self)
        print(f"角色 {self.symbol} 進入了 {state} 狀態")
        self.state = state

    def exit_state(self):
        print(f"角色 {self.symbol} 離開狀態 {self.state}")
        self.entry_state(self.state.next_state)

    def move(self, target):
        self.map.move_object_to_target(self, target)

    def attack(self, targets):
        for target in targets:
            target.be_attacked(self.damage)

    def touch(self, treasure: 'Treasure'):
        state = treasure.get_state()
        print(f"角色 {self.symbol} 獲得寶物 {treasure.content}")
        self.entry_state(state)
        self.map.remove_object_with_coord(treasure.x, treasure.y)

    def take_turn(self):
        self.state.trigger()
        self.show_status()
        choose = self.choose()
        if choose == "a":
            self.move_step()
        elif choose == "b":
            self.attack_step()

    def show_status(self):
        pass

    @abstractmethod
    def choose(self):
        pass

    @abstractmethod
    def move_step(self):
        pass

    def attack_step(self):
        targets: list = self.get_attack_targets()
        print(f"攻擊了 {targets}！")
        self.attack(targets)

    def get_attack_targets(self):
        if self.attack_targets is None:
            return self.default_attack()
        else:
            return self.attack_targets

    @abstractmethod
    def default_attack(self):
        pass

    def set_collision_handler(self, handler: 'CollisionHandler'):
        self.handler = handler

    def be_attacked(self, damage):
        if self.invincible:
            print(f"角色 {self.symbol} 現在是 {self.state} 狀態沒受到傷害")
            return
        self.hp -= damage
        print(f"角色 {self.symbol} 受到 {damage} 攻擊！")
        self.entry_state(self.be_attacked_entry_state)
        if not self.check_is_alive():
            self.role_death()

    def role_death(self):
        print(f"角色 {self.symbol} 已死亡")
        self.map.remove_object_with_coord(self.x, self.y)

    def check_is_alive(self) -> bool:
        return self.hp > 0

    def get_damage(self, damage):
        self.hp -= damage
        if not self.check_is_alive():
            self.role_death()

    def get_healing(self, healing):
        if (self.hp + healing) > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += healing

    def set_invincible(self, status: bool):
        self.invincible = status

    def set_move_step(self, step):
        self.can_move_step = step

    def set_can_choose(self, choose):
        self.can_choose = choose
