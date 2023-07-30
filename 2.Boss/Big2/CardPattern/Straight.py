from .CardPattern import CardPattern
from ..Card import Card


class Straight(CardPattern):
    def __init__(self, cards: list[Card]):
        super().__init__(cards)
        self.name = '順子'

    def set_sort_rank_reverse(self):
        return False

    def sort_spec_rule(self):
        check = None
        for card in self.cards:
            if card.rank.name == '_J':
                check = True
        if check:
            self.cards = self.to_sort_rank(self.cards)
        else:
            temp = []
            rank = ['_A', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_10', '_J', '_Q', '_K']
            for r in rank:
                for card in self.cards:
                    if card.rank.name == r:
                        temp.append(card)
                        break
            self.cards = temp

    def __gt__(self, other):
        big_card_in_self = None
        big_card_in_other = None
        for self_card in self.cards:
            if big_card_in_self is None:
                big_card_in_self = self_card
            else:
                if self_card > big_card_in_self:
                    big_card_in_self = self_card
        for other_card in other.cards:
            if big_card_in_other is None:
                big_card_in_other = other_card
            else:
                if other_card > big_card_in_other:
                    big_card_in_other = other_card
        return big_card_in_self > big_card_in_other


