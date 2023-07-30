import random
from .Card import Card
from ..DeckTemplate import DeckTemplate


class Deck(DeckTemplate):
    color = ["Blue", "Red", "Yellow", "Green"]
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        super().__init__()
        self.deck = []
        for c in self.color:
            for n in self.number:
                self.deck.append(Card(c, n))
        self.size = len(self.deck)

    def add_card(self, card):
        self.deck.append(card)
        self.size += 1
