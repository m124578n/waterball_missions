from ..HumanPlayerTemplate import HumanPlayerTemplate


class HumanPlayer(HumanPlayerTemplate):
    def _get_player_order(self):
        player_decide = input("請輸入卡片編號：")
        return player_decide

    def print_cards_you_have(self):
        for index, card in enumerate(self.hand):
            print("卡片%s, %s, %s" % (index, card.suits.name, card.rank.name))