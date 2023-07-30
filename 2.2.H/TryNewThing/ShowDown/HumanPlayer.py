from .Player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def name_himself(self):
        name = input("請幫自己取名：")
        self.name = name
        print(f"您的名字為：{self.name}")

    def take_turn(self):
        print("您現在的手牌有：")
        for index, card in enumerate(self.hand.card):
            print(f"第{index}張：{card.suit.name} {card.rank.name}")
        hand_index = int(input("您要出第幾張牌："))
        return self.hand.show(hand_index)

