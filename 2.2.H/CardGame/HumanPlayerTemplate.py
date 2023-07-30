from .PlayerTemplate import PlayerTemplate


class HumanPlayerTemplate(PlayerTemplate):
    def __init__(self):
        super().__init__()

    def take_turn(self):
        print("您的卡片有：")
        self.print_cards_you_have()
        player_decide = self._get_player_order()
        return player_decide

    def name_himself(self):
        self.name = input("請輸入你的名稱：")

    def add_hand(self, card):
        self.hand.append(card)
        self.hand_size += 1

    def show(self, want_to_show_card_index):
        self.hand_size -= 1
        return self.hand.pop(int(want_to_show_card_index))

    def pass_turn(self):
        pass

    def _get_player_order(self) -> str:
        pass

    def print_cards_you_have(self):
        pass

