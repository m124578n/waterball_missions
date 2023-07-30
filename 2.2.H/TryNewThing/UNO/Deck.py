from .Card import Card
import random
from ..DeckTemplate import DeckTemplate


class Deck(DeckTemplate):
    colors = ["Red", "Blue", "Yellow", "Green"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self):
        super().__init__()
        for color in self.colors:
            for number in self.numbers:
                self.deck.append(Card(color, number))
        self.size = len(self.deck)

    def add_card(self, card):
        self.size += 1
        self.deck.append(card)
