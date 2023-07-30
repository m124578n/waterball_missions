from Player import *


class Human(Player):
    def __init__(self):
        super().__init__()

    def name_self(self, name):
        self.name = name

    def do_exchange_hands_right(self, player):
        temp_hands = self.hands
        self.hands = player.hands
        player.hands = temp_hands

    def show(self, choose):
        return self.hands.pop(choose)

    def show_hand(self):
        return {x + 1: self.hands[x].__str__() for x in range(len(self.hands))}
