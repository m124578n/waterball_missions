import random

from .Map import Map
from .MapObject import Space, MapObject
from .Handler import CollisionHandler, HandlerChain


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
        self.map = None
        self.__init_map()
        self.__set_handler()

    def start(self):
        while self.__win_condition():
            self.__start_round()
    
    def __start_round(self):
        character = self.map.find_character()
        while self.__win_condition():
            character.take_turn(self.map, self.collision_handler)
            self.__show_map()
    
    def __show_map(self):
        print(self.map)
    
    def __init_map(self):
        self.map = Map(self.__range_x, self.__range_y)
        for map_object in self.__map_objects:
            self.__create_map_object(map_object[0], map_object[1])
        self.__show_map()
    
    def __create_map_object(self, map_object, amount):
        while amount != 0:
            x = random.randint(0, self.__range_x -1)
            y = random.randint(0, self.__range_y -1)
            map_object_ = self.map.find_object_by_coord(x, y)
            if isinstance(map_object_, Space):
                self.map.set_object_with_coord(x, y, map_object)
                amount -= 1
                
    def __win_condition(self):
        return True
    
    def __set_handler(self):
        collision_handler = HandlerChain()
        for handler in self.__handlers:
            collision_handler.set_next(handler)
        self.collision_handler = collision_handler