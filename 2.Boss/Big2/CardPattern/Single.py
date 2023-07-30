from .CardPattern import CardPattern
from ..Card import Card


class Single(CardPattern):
    def __init__(self, cards: list[Card]):
        super().__init__(cards)
        self.name = '單張'

    def __gt__(self, other):
        return self.cards[0] > other.cards[0]
