from .Rank import Rank
from .Suit import Suit
from .Card import Card
import random


class Deck:
    def __init__(self, deck_input: str or None):
        self.deck = []
        if deck_input is None:
            for r in Rank:
                for s in Suit:
                    self.deck.append(Card(s.name+"["+r.name[1:]+"]"))
        else:
            deck = deck_input.split(' ')
            for card in deck:
                self.deck.append(Card(card))
        self.size = len(self.deck)

    def deal(self) -> Card:
        self.size -= 1
        card = self.deck.pop(self.size)
        return card

    def shuffle(self):
        random.shuffle(self.deck)

