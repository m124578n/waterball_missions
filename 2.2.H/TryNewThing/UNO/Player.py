from abc import ABC, abstractmethod
from .Hand import Hand


class Player(ABC):
    def __init__(self):
        self.name = None
        self.hand = Hand()

    @abstractmethod
    def name_himself(self):
        pass

    @abstractmethod
    def take_turn(self):
        pass
