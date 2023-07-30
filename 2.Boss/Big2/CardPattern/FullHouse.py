from .CardPattern import CardPattern
from ..Card import Card


class FullHouse(CardPattern):
    def __init__(self, cards: list[Card]):
        super().__init__(cards)
        self.name = '葫蘆'

    def sort_spec_rule(self):
        temp_1 = []
        temp_2 = []
        for card in self.cards:
            if not temp_1:
                temp_1.append(card)
            else:
                if temp_1[0].rank == card.rank:
                    temp_1.append(card)
                else:
                    temp_2.append(card)
        temp_1 = self.to_sort_suit(temp_1)
        temp_2 = self.to_sort_suit(temp_2)
        if len(temp_1) > len(temp_2):
            self.cards = temp_1 + temp_2
        else:
            self.cards = temp_2 + temp_1

    def __gt__(self, other):
        return self.cards[0] > other.cards[0]
