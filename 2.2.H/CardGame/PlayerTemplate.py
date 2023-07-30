from abc import ABC, abstractmethod
from .CardTemplate import CardTemplate


class PlayerTemplate(ABC):
    def __init__(self):
        self.name = None
        self.hand = []
        self.hand_size = 0
        self.point = 0

    @abstractmethod
    def take_turn(self):
        pass

    @abstractmethod
    def name_himself(self):
        pass

    @abstractmethod
    def add_hand(self, card: CardTemplate):
        pass

    @abstractmethod
    def show(self, want_to_show_card) -> CardTemplate:
        pass
