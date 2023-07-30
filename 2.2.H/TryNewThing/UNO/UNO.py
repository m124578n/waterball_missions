from .Deck import Deck


class UNO:
    def __init__(self, players: list):
        self.players = players
        self.deck = Deck()
        self.init_card = 0
        self.winner = None
        self.table = []
        self.now_card = None
        self.table.append(self.deck.draw_card())

    def start(self):
        self.players_name_himself()
        self.deck.shuffle()
        while not self.draw_card_conditional():
            self.players_draw_card()
        while not self.game_end_conditional():
            self.game_start_until_end()
        self.show_winner()

    def players_name_himself(self):
        for player in self.players:
            player.name_himself()

    def draw_card_conditional(self):
        return self.init_card == 5

    def players_draw_card(self):
        for player in self.players:
            player.hand.add_card(self.deck.draw_card())
        self.init_card += 1

    def game_end_conditional(self):
        return self.winner is not None

    def game_start_until_end(self):
        for player in self.players:
            self.show_table_card()
            print(self.deck.size)
            print(len(self.table))
            while True:
                make_decide = self.check_player_have_card(player)
                if make_decide == 'pass':
                    if self.deck.size == 0:
                        self.reload_card()
                    player.hand.add_card(self.deck.draw_card())
                    break
                else:
                    player_showed_card = player.hand.show(int(make_decide))
                    print(player_showed_card.color, player_showed_card.number)
                    if self.check_card_rule(player_showed_card):
                        self.table.append(player_showed_card)
                        break
                    else:
                        player.hand.add_card(player_showed_card)
                        print("您出的卡片不符合規則！！請重新選擇！！")
                        self.show_table_card()
            if player.hand.size == 0:
                self.winner = player
                break

    def check_player_have_card(self, player):
        for card in player.hand.card:
            if self.check_card_rule(card):
                return player.take_turn()
        return "pass"

    def show_table_card(self):
        print(f"現在場面上的卡為：{self.table[::-1][0].color} {self.table[::-1][0].number}")

    def reload_card(self):
        while len(self.table) != 1:
            self.deck.add_card(self.table.pop(0))

    def check_card_rule(self, card):
        self.now_card = self.table[::-1][0]
        return self.now_card.color == card.color or self.now_card.number == card.number

    def show_winner(self):
        print(f"玩家{self.winner.name}獲勝！")


