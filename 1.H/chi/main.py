from Deck import *
from HumanPlayer import *
from AIPlayer import *
from ExchangeHands import *


class Game:
    def __init__(self):
        self.deck = Deck()
        self.round = 0
        self.exchange_list = []
        self.players = []
        self.bot_players = 4

    def start(self):
        while True:
            try:
                real_player = int(input("請輸入有幾個真實玩家："))
                if 0 < real_player < 4:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("請輸入數字且不能為0或大於4")

        self.bot_players = 4 - real_player
        for i in range(real_player):
            name = input("請輸入你的名字 : ")
            human = Human()
            human.name_self(name)
            self.players.append(human)

        for i in range(self.bot_players):
            ai = AI()
            ai.name_self("ai_bot0" + str(i + 1))
            self.players.append(ai)

        print("洗牌")
        self.deck.shuffle()
        print("發牌")
        for player in self.players:
            for i in range(13):
                player.add_hands_card(self.deck.draw())

        while self.round != 13:
            print("回合開始")

            card_list = []
            print("確認所有玩家是否要交換手牌！！")
            for player in self.players:
                if isinstance(player, Human):
                    if not player.done_exchange_hands_right:
                        print(player.name + "的手牌：")
                        print(player.show_hand())
                        des = input("請問是否有要跟別人交換牌：y/n")
                        if des == 'y' or des == 'Y':
                            for x in self.players:
                                print(x.name)
                            exchange_name = input("請問要跟誰交換：")

                            while exchange_name not in [x.name for x in self.players]:
                                exchange_name = input('請選擇一個存在的人：')
                                for x in self.players:
                                    print(x.name)
                            target_player = None
                            for p in self.players:
                                if p.name == exchange_name:
                                    target_player = p
                                    break
                            if target_player is not None:
                                player.do_exchange_hands_right(target_player)
                                print('交換成功，只能持續３回合')
                                player.done_exchange_hands_right = True
                                exchange = Exchange()
                                exchange.get_start_player(player)
                                exchange.get_target_player(target_player)
                                self.exchange_list.append(exchange)
                                print(player.show_hand())
            print("開始出牌")
            for player in self.players:
                if isinstance(player, Human):
                    print(player.name + "的手牌：")
                    print(player.show_hand())
                    choose = ''
                    while not isinstance(choose, int) or choose > len(player.hands):
                        try:
                            choose = int(input("請選擇你的牌：（請輸入數字）")) - 1
                            if choose > len(player.hands):
                                print("你沒有那麼多張牌")
                                continue
                        except ValueError:
                            print("請輸入數字")
                            continue
                    card_list.append(player.show(choose))
                else:
                    card_list.append(player.show())

            if len(self.exchange_list) != 0:
                for exchange in self.exchange_list:
                    exchange.reduce_countdown()
                    if exchange.countdown == 0:
                        exchange.start_player.do_exchange_hands_right(exchange.target_player)
                        print("交換結束，轉換回來")
                        self.exchange_list.remove(exchange)

            if len(self.exchange_list) != 0:
                for exchange in self.exchange_list:
                    print("玩家 %s 和玩家 %s 的換牌時間還有 %s 回合" %
                          (exchange.start_player.name,
                           exchange.target_player.name, str(exchange.countdown)))

            print("開牌")
            for card in card_list:
                print(card.__str__())
            winner_number = self.compare_cards(card_list)
            self.players[winner_number].get_point()
            print("本回合" + self.players[winner_number].name + "勝利")

            input("按enter鍵往下回合")

            self.round += 1

        winner = self.check_winner(self.players)
        print("--------------------------")
        print("最終勝利者為：%s" % winner)
        print("--------------------------")

    @staticmethod
    def check_winner(players_list):
        winner_point = 0
        winner = ''
        for player in players_list:
            if player.point > winner_point:
                winner = player
        return winner.name

    @staticmethod
    def compare_cards(card_list):
        winner = 0
        big_card = 0
        for i in range(len(card_list)):
            if big_card == 0:
                big_card = card_list[i]
                winner = i
            if big_card.rank.value < card_list[i].rank.value:
                big_card = card_list[i]
                winner = i
            elif big_card.rank.value == card_list[i].rank.value:
                if big_card.suit.value < card_list[i].suit.value:
                    big_card = card_list[i]
                    winner = i
            else:
                pass
        return winner


if __name__ == "__main__":
    game = Game()
    game.start()

