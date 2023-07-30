from abc import ABC, abstractmethod


class CardPatternHandler(ABC):
    def __init__(self, handler: "CardPatternHandler" or None):
        self.next = handler

    # TODO 待抽取相同之處
    def check(self, cards):
        if self.set_cards_amount(cards):
            if self.next is not None:
                return self.next.check(cards)
            else:
                return False
        return self.set_check_card_pattern_rule(cards)

    @abstractmethod
    def set_cards_amount(self, cards):
        pass

    @abstractmethod
    def set_check_card_pattern_rule(self, cards):
        pass
