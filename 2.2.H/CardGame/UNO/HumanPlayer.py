from ..HumanPlayerTemplate import HumanPlayerTemplate


class HumanPlayer(HumanPlayerTemplate):
    def _get_player_order(self):
        print("如沒有牌可以出請輸入：pass")
        player_decide = input("請輸入卡片編號或pass：")
        return player_decide

    def print_cards_you_have(self):
        for index, card in enumerate(self.hand):
            print("卡片%s, %s, %s" % (index, card.color, card.number))
