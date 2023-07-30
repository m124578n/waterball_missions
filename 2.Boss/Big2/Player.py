from .HandCards import HandCards
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, index: int):
        self.name = None
        self.index = index
        self.hand_cards = HandCards()
        self.turn = 0

    @abstractmethod
    def name_himself(self):
        pass

    @abstractmethod
    def take_turn(self):
        pass

    @abstractmethod
    def yell_pass(self):
        pass

    @abstractmethod
    def play(self, player_decide_play):
        pass
