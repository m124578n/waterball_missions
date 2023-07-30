from Player import *


class AI(Player):
    def __init__(self):
        super().__init__()

    def name_self(self, name):
        self.name = name

    def do_exchange_hands_right(self, player):
        pass

    def show(self):
        return self.hands.pop()
