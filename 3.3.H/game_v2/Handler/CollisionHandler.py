from abc import ABC, abstractmethod


class CollisionHandler(ABC):
    def __init__(self):
        self.next = None
    
    def set_next(self, handler):
        if self.next is None:
            self.next = handler

    def collision(self, player, target):
        if self.collision_condition(player, target):
            self.collision_result(player, target)
        else:
            if self.next is None:
                print(f"{player.symbol} 呆呆地站在原地 ! ")
            else:
                return self.next.collision(player, target)
    
    @abstractmethod
    def collision_condition(self, player, target):
        pass

    @abstractmethod
    def collision_result(self, player, target):
        pass
