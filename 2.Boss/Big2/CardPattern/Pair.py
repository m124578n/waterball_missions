from .CardPattern import CardPattern
from ..Card import Card


class Pair(CardPattern):
    def __init__(self, cards: list[Card]):
        super().__init__(cards)
        self.name = '對子'

    def __gt__(self, other):
        return self.cards[1] > other.cards[1]
