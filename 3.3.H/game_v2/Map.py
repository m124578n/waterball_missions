from .MapObject import Space, MapObject, Character


class Map:
    def __init__(self, x, y):
        self.map = []
        self.x_len = x
        self.y_len = y
        for x1 in range(x):
            temp1 = []
            for y1 in range(y):
                map_object = Space(x1, y1)
                temp1.append(map_object)
            self.map.append(temp1)
    
    def __str__(self):
        for x in self.map:
            print(f"{x}")
        return "this is a map"
    
    def find_object_by_coord(self, x, y) -> MapObject:
        try:
            return self.map[x][y]
        except:
            return None
    
    def set_object_with_coord(self, x, y, map_object):
        self.map[x][y] = map_object(x, y)
    
    def move_object_with_coord(self, x, y, map_object):
        self.map[x][y] = map_object
    
    def remove_object_with_coord(self, x, y):
        self.map[x][y] = Space(x, y)
    
    def move_object_to_target(self, player, target):
        self.map[player.x][player.y], self.map[target.x][target.y] = target, player
        player.x, target.x = target.x, player.x
        player.y, target.y = target.y, player.y

    def find_around_objects(self, role) -> dict:
        # ↑→↓←
        around = {
            "w":[self.find_object_by_coord(role.x-1, role.y), "↑"],
            "a":[self.find_object_by_coord(role.x, role.y-1), "←"],
            "s":[self.find_object_by_coord(role.x+1, role.y), "↓"],
            "d":[self.find_object_by_coord(role.x, role.y+1), "→"],
            }
        return around
    
    def find_character(self) -> Character:
        for x in self.map:
            for y in x:
                if isinstance(y, Character):
                    return y