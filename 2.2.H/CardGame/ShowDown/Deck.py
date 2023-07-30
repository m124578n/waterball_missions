import random
from .Rank import Rank
from .Suits import Suits
from .Card import Card
from ..DeckTemplate import DeckTemplate


class Deck(DeckTemplate):
    def __init__(self):
        super().__init__()
        self.deck = []
        for s in Rank:
            for r in Suits:
                self.deck.append(Card(s, r))
        self.size = len(self.deck)

