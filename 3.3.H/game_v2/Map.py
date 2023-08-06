import random

from .MapObject import Space, MapObject, Character, Monster, Obstacle, Role


class Map:
    def __init__(self, x: int, y: int) -> None:
        self.map = []
        self.x_len = x
        self.y_len = y
        for x1 in range(x):
            temp1 = []
            for y1 in range(y):
                map_object = Space(x1, y1, self)
                temp1.append(map_object)
            self.map.append(temp1)

    def __str__(self) -> str:
        for x in self.map:
            print(f"{x}")
        return "this is a map"

    def find_object_by_coord(self, x: int, y: int) -> MapObject | None:
        try:
            if x < 0 or y < 0:
                raise
            return self.map[x][y]
        except:
            return None

    def set_object_with_coord(self, x: int, y: int, map_object) -> None:
        self.map[x][y] = map_object(x, y, self)

    def remove_object_with_coord(self, x: int, y: int) -> None:
        self.map[x][y] = Space(x, y, self)

    def move_object_to_target(self, player: Role, target: Space) -> None:
        self.map[player.x][player.y], self.map[target.x][target.y] = target, player
        player.x, target.x = target.x, player.x
        player.y, target.y = target.y, player.y

    def find_around_objects(self, role: Role) -> dict:
        # ↑→↓←
        around = {
            "w": [self.find_object_by_coord(role.x - 1, role.y), "↑"],
            "a": [self.find_object_by_coord(role.x, role.y - 1), "←"],
            "s": [self.find_object_by_coord(role.x + 1, role.y), "↓"],
            "d": [self.find_object_by_coord(role.x, role.y + 1), "→"],
        }
        return around

    def find_line_targets(self, start: int, stop: int, reverse: int, direction: str, role: Character):
        target_line = []
        for i in range(start, stop, reverse):
            if direction == 'updown':
                target = self.find_object_by_coord(i, role.y)
            elif direction == 'rightleft':
                target = self.find_object_by_coord(role.x, i)
            else:
                target = None
            if isinstance(target, Monster):
                target_line.append(target)
            elif isinstance(target, Obstacle):
                break
        return target_line

    def find_attack_target_objects(self, role: Character) -> list:
        if role.symbol == "↑":
            target_line = self.find_line_targets(role.x - 1, 0 - 1, -1, 'updown', role)
        elif role.symbol == "←":
            target_line = self.find_line_targets(role.y - 1, 0 - 1, -1, 'rightleft', role)
        elif role.symbol == "↓":
            target_line = self.find_line_targets(role.x + 1, self.x_len, 1, 'updown', role)
        elif role.symbol == "→":
            target_line = self.find_line_targets(role.y + 1, self.y_len, 1, 'rightleft', role)
        else:
            target_line = []
        return target_line

    def find_character(self) -> Character:
        for x in self.map:
            for y in x:
                if isinstance(y, Character):
                    return y

    def find_all_monsters(self) -> list:
        monsters = []
        for x in self.map:
            for y in x:
                if isinstance(y, Monster):
                    monsters.append(y)
        return monsters

    def find_all_different_role(self, role) -> list:
        if isinstance(role, Character):
            return self.find_all_monsters()
        if isinstance(role, Monster):
            return [self.find_character()]

    def find_random_space(self) -> Space:
        while True:
            x = random.randint(0, self.x_len - 1)
            y = random.randint(0, self.y_len - 1)
            target = self.find_object_by_coord(x, y)
            if isinstance(target, Space):
                return target
