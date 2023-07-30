from .CardPatternHandler import CardPatternHandler
from ..Card import Card
from Big2.CardPattern import Pair


class IsPair(CardPatternHandler):

    def set_cards_amount(self, cards):
        return len(cards) != 2

    def set_check_card_pattern_rule(self, cards):
        if cards[0] != cards[1]:
            if self.next is not None:
                return self.next.check(cards)
            else:
                return False
        else:
            return Pair(cards)
