from .CardPatternHandler import CardPatternHandler
from ..Card import Card
from Big2.CardPattern import FullHouse


class IsFullHouse(CardPatternHandler):

    def set_cards_amount(self, cards):
        return len(cards) != 5

    def set_check_card_pattern_rule(self, cards):
        temp_1 = []
        temp_2 = []
        for card in cards:
            if not temp_1:
                temp_1.append(card)
            elif temp_1[0] != card:
                if not temp_2:
                    temp_2.append(card)
                elif temp_2[0] != card:  # 判斷有第三種rank卡 group by
                    if self.next is not None:
                        return self.next.check(cards)
                    else:
                        return False
                else:
                    temp_2.append(card)
            else:
                temp_1.append(card)
        if len(temp_2) not in [2, 3] and len(temp_1) not in [2, 3]:
            if self.next is not None:
                return self.next.check(cards)
            else:
                return False
        else:
            return FullHouse(cards)
