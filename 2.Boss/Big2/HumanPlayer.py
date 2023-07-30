from .Player import Player


class HumanPlayer(Player):
    def __init__(self, index):
        super().__init__(index)

    def name_himself(self):
        self.name = input("請輸入您的名字：")

    def take_turn(self):
        self.show_hand_cards()
        player_decide_play = input("選擇要打出的牌：")
        return self.play(player_decide_play)

    def show_hand_cards(self):
        if self.turn == 0:
            self.turn += 1
            card_index_str = ""
            card_str = ""
            for index, card in enumerate(self.hand_cards.cards):
                if len(str(card)) == 5:
                    if len(str(index)) == 2:
                        card_index_str += f"{index}    "
                    else:
                        card_index_str += f"{index}     "
                else:
                    if len(str(index)) == 2:
                        card_index_str += f"{index}   "
                    else:
                        card_index_str += f"{index}    "
                card_str += f"{str(card)} "
            print(card_index_str)
            print(card_str)

    def yell_pass(self):
        return 'pass'

    def play(self, player_decide_play):
        if player_decide_play == '-1':
            return self.yell_pass()
        elif "" in player_decide_play.split(" "):
            return "error01"
        else:
            play_card = self.hand_cards.show_card(player_decide_play)
            return play_card
