from .CardPatternHandler import CardPatternHandler
from ..Card import Card
from Big2.CardPattern import Single


class IsSingle(CardPatternHandler):

    def set_cards_amount(self, cards):
        return len(cards) != 1

    def set_check_card_pattern_rule(self, cards):
        return Single(cards)
