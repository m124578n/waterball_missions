from .Card import Card
from .Ranks import Ranks
from .Suits import Suits
import random
from ..DeckTemplate import DeckTemplate


class Deck:
    def __init__(self):
        self.deck = []
        for rank in Ranks:
            for suit in Suits:
                self.deck.append(Card(suit, rank))
        self.size = len(self.deck)

