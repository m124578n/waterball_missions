from __future__ import annotations

import random

from game_v1.Map import Map
from game_v1.MapObject import (
    Obstacle,
    Character,
    Monster,
    MapObject,
    Treasure,
)
from game_v1.Handler import CollisionHandler


class Game:
    def __init__(self, handler):
        self.set_map_x = 10
        self.set_map_y = 10
        self.map: Map | None = None
        self.round: int = 0
        self.obstacle_count = 10
        self.character_count = 1
        self.monster_count = 10
        self.treasure_count = 10
        self.player_move_state = False
        self.handler: CollisionHandler | None = handler

    def start(self):
        self._init_map()
        while self.game_over_condition():
            self.take_round()

    def _init_map(self):
        self._create_map()
        self._create_obstacle()
        self._create_character()
        self._create_monster()
        self._create_treasure()

    def _create_map(self):
        self.map = Map(self.set_map_x, self.set_map_y)

    def _create_obstacle(self):
        for obstacle in range(self.obstacle_count):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            while self.map.map[x][y].object is None:
                self.map.map[x][y].object = Obstacle()

    def _create_character(self):
        for character in range(self.character_count):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            while self.map.map[x][y].object is None:
                self.map.map[x][y].object = Character()

    def _create_monster(self):
        for monster in range(self.monster_count):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            while self.map.map[x][y].object is None:
                self.map.map[x][y].object = Monster()

    def _create_treasure(self):
        for treasure in range(self.treasure_count):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            while self.map.map[x][y].object is None:
                self.map.map[x][y].object = Treasure()

    def take_round(self):
        self.show_map()
        self.round += 1
        self.player_move_state = False
        print(f"現在是第 {self.round} 回合")
        self.character_turn()
        self.monster_turn()

    def show_map(self):
        print(self.map)

    def character_turn(self):
        print("現在是玩家的回合")
        player_choose = input("請選擇動作 (a) 往一個方向移動一格 (b) 攻擊：")
        player = self.find_character()
        print(player.x, player.y)
        if player_choose == 'a':
            while not self.player_move_success():
                player_choose = input("請輸入想往哪邊走 wasd：")
                target = self.get_target_map_object(player, player_choose)
                self.player_move(player, target, player_choose)
        if player_choose == 'b':
            targets = self.find_all_attack_target(player)
            self.player_attack(targets)

    def player_attack(self, targets):
        for target in targets:
            target.object = None
        print("已清出所有怪物！")

    def find_all_attack_target(self, player):
        # ↑→↓←
        if player.object.symbol == "↑":
            targets = []
            for x in range(player.x, 0, -1):
                target = self.map.map[x][player.y]
                if isinstance(target.object, Obstacle):
                    break
                if isinstance(target.object, Monster):
                    targets.append(target)
            return targets
        if player.object.symbol == "←":
            targets = []
            for y in range(player.y, 0, -1):
                target = self.map.map[player.x][y]
                if isinstance(target.object, Obstacle):
                    break
                if isinstance(target.object, Monster):
                    targets.append(target)
            return targets
        if player.object.symbol == "↓":
            targets = []
            for x in range(player.x, self.set_map_x):
                target = self.map.map[x][player.y]
                if isinstance(target.object, Obstacle):
                    break
                if isinstance(target.object, Monster):
                    targets.append(target)
            return targets
        if player.object.symbol == "→":
            targets = []
            for y in range(player.y, self.set_map_y):
                target = self.map.map[player.x][y]
                if isinstance(target.object, Obstacle):
                    break
                if isinstance(target.object, Monster):
                    targets.append(target)
            return targets

    def get_target_map_object(self, player, player_choose) -> MapObject:
        target = None
        if player_choose == 'w':
            target = self.map.map[player.x - 1][player.y]
        if player_choose == 'a':
            target = self.map.map[player.x][player.y - 1]
        if player_choose == 's':
            target = self.map.map[player.x + 1][player.y]
        if player_choose == 'd':
            target = self.map.map[player.x][player.y + 1]
        if target is None:
            raise ValueError
        else:
            return target

    def player_move(self, player, target, player_choose):
        if not self.check_player_can_move(player, target):
            print(f"前方有 {target.object} 擋住了你的路！")
            return
        else:
            player.object.move(player_choose)
            player.object, target.object = target.object, player.object
            self.player_move_state = True

    def player_move_success(self) -> bool:
        return self.player_move_state

    def check_player_can_move(self, player, target) -> bool:
        return self.handler.collision(player, target)

    def find_character(self):
        for x in self.map.map:
            for y in x:
                if isinstance(y.object, Character):
                    return y

    def monster_turn(self):
        pass

    def game_over_condition(self):
        return self.round != 10
