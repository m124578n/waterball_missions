from ..Card import Card
from ..SortedCards import SortedCards


class CardPattern(SortedCards):
    def __init__(self, cards: list[Card]):
        super().__init__()
        self.cards = cards
        self.sort_spec_rule()
        self.name = None

