from .Player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def name_himself(self):
        name = input("請輸入姓名：")
        self.name = name

    def take_turn(self):
        print("您手中的卡有：")
        for index, card in enumerate(self.hand.card):
            print(f"第{index}張 {card.color} {card.number}")
        player_decide = input("請選擇要出的卡片，如果沒得出請輸入pass：")
        return player_decide
