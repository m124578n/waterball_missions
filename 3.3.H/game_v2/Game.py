import random

from .Map import Map
from .MapObject import Space, MapObject
from .Handler import CollisionHandler


class Game:
    def __init__(self, 
                 map_objects: list[list[MapObject, int]],
                 handlers: list[CollisionHandler]
                 ) -> None:
        self.__range_x = 10
        self.__range_y = 10
        self.__map_objects = map_objects
        self.__handlers = handlers
        self.collision_handler = None
        self.map: Map | None = None
        self.character = None
        self.monsters = []
        self.__set_handler()
        self.__init_map()

    def start(self) -> None:
        while self.__win_condition():
            self.__start_round()
    
    def __start_round(self) -> None:
        if self.__win_condition():
            self.character.take_turn()
        if self.__win_condition():
            self.__monsters_take_turn()
        self.__show_map()

    def __monsters_set_handler(self):
        for monster in self.monsters:
            monster.set_collision_handler(self.collision_handler)

    def __monsters_take_turn(self):
        for monster in self.monsters:
            monster.take_turn()
    
    def __show_map(self) -> None:
        print(self.map)
    
    def __init_map(self) -> None:
        self.map = Map(self.__range_x, self.__range_y)
        for map_object in self.__map_objects:
            self.__create_map_object(map_object[0], map_object[1])
        self.__show_map()
        self.character = self.map.find_character()
        self.character.set_collision_handler(self.collision_handler)
        self.monsters = self.map.find_all_monsters()
        self.__monsters_set_handler()
    
    def __create_map_object(self, map_object: MapObject, amount: int) -> None:
        while amount != 0:
            x = random.randint(0, self.__range_x - 1)
            y = random.randint(0, self.__range_y - 1)
            map_object_ = self.map.find_object_by_coord(x, y)
            if isinstance(map_object_, Space):
                self.map.set_object_with_coord(x, y, map_object)
                amount -= 1
                
    def __win_condition(self) -> bool:
        self.character = self.map.find_character()
        self.monsters = self.map.find_all_monsters()
        if self.character is None:
            print(f"主角 已死亡 遊戲結束")
            return False
        elif not self.monsters:
            print(f"主角 已擊敗所有怪物 遊戲結束")
            return False
        return True
    
    def __set_handler(self) -> None:
        pointer = None
        for handler in self.__handlers:
            if self.collision_handler is None:
                self.collision_handler = handler
            else:
                pointer.next = handler
            pointer = handler
