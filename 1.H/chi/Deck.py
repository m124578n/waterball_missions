import random
from Card import *
from Suits import *
from Ranks import *


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suits for rank in Ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()