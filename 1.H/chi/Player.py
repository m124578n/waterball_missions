from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.hands = []
        self.done_exchange_hands_right = False
        self.point = 0
        self.name = ''

    @abstractmethod
    def name_self(self, name):
        pass

    def add_hands_card(self, card):
        self.hands.append(card)

    @abstractmethod
    def do_exchange_hands_right(self, player):
        pass

    def get_point(self):
        self.point += 1

