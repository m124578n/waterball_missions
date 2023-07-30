from abc import ABC, abstractmethod


class CollisionHandler(ABC):
    def __init__(self):
        self.next = None

    @abstractmethod
    def collision(self, player, target):
        pass
