import random


class DeckTemplate:
    def __init__(self):
        self.deck = []
        self.size = len(self.deck)

    def shuffle(self):
        print("－－－－洗牌－－－－")
        random.shuffle(self.deck)

    def draw_card(self):
        self.size -= 1
        return self.deck.pop(0)
