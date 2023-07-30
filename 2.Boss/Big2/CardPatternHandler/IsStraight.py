from .CardPatternHandler import CardPatternHandler
from ..Card import Card
from ..CardPattern import Straight
from ..SortedCards import SortedCards


class IsStraight(CardPatternHandler, SortedCards):

    def set_cards_amount(self, cards):
        return len(cards) != 5

    def set_check_card_pattern_rule(self, cards):
        self.cards = cards
        self.sort_spec_rule()
        cards = self.cards
        card_reduce_list = []
        for i in range(len(cards) - 1):
            card_rule = cards[i].rank.value - cards[i + 1].rank.value
            card_reduce_list.append(card_rule)
            if card_reduce_list.count(9) > 1 or card_reduce_list.count(1) < 3:
                if card_rule not in (1, 9):
                    if self.next is not None:
                        return self.next.check(cards)
                    else:
                        return False
        return Straight(cards)
