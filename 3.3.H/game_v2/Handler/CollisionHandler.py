from abc import ABC, abstractmethod


class CollisionHandler(ABC):
    def __init__(self):
        self.next = None
    
    def set_next(self, handler):
        if self.next is None:
            self.next = handler

    def collision(self, player, target, map):
        if self.collision_condition(player, target):
            self.collision_result(player, target, map)
        else:
            if self.next is None:
                print("無符合的碰撞發生 ! ")
            else:
                return self.next.collision(player, target, map)
    
    @abstractmethod
    def collision_condition(self, player, target):
        pass

    @abstractmethod
    def collision_result(self, player, target, map):
        pass
