import random


class DeckTemplate:
    def __init__(self):
        self.deck = None
        self.size = None

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        self.size -= 1
        return self.deck.pop(0)
