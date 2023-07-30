from abc import ABC, abstractmethod


class CollisionHandler(ABC):
    def __init__(self, handler):
        self.next = handler

    @abstractmethod
    def collision(self, player, target):
        pass
