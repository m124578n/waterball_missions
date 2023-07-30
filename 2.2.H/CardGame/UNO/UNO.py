from .Deck import Deck
from ..CardGameTemplate import CardGameTemplate


class UNO(CardGameTemplate):
    def __init__(self, players: list):
        super().__init__(players, Deck())

    def game_take_round(self):
        if not self.table:
            self.table.append(self.deck.draw_card())
        for player in self.players:
            card_check = None
            while card_check is None:
                target_card = self.table[::-1][0]
                print("現在場面上的卡片為：%s, %s" % (target_card.color, target_card.number))
                player_decide = player.take_turn()
                if player_decide == 'pass':
                    self.player_decide_pass(player)
                    card_check = True
                else:
                    player_showed_card = player.show(player_decide)
                    if self.check_card(player_showed_card):
                        card_check = True
                        player.showed_card_count = 0
                        self.table.append(player_showed_card)
                        target_card = self.table[::-1][0]
                        print("現在場面上的卡片為：%s, %s" % (target_card.color, target_card.number))
                    else:
                        player.add_hand(player_showed_card)
                    print("玩家手牌%s %s" % (player.name, player.hand_size))
                    if player.hand_size == 0:
                        self.winner = player
                        break

    def check_card(self, card):
        target_card = self.table[::-1][0]
        if target_card.color != card.color and target_card.number != card.number:
            print("你出的卡片 %s,%s 不符合遊戲規則！！" % (card.color, card.number))
            return False
        else:
            return True

    def deck_reload(self):
        self.table = self.table[::-1]
        while len(self.table) != 1:
            print("重新洗牌")
            self.deck.add_card((self.table.pop(0)))
        self.deck.shuffle()

    def player_decide_pass(self, player):
        player.pass_turn()
        print("牌堆剩餘數量%s" % self.deck.size)
        if self.deck.size == 0:
            self.deck_reload()
        player.add_hand(self.deck.draw_card())

    def show_winner(self):
        winner = None
        for player in self.players:
            if player.hand_size == 0:
                winner = player
        print(winner.name)

    def draw_card_conditional(self):
        return self.init_card != 5

    def game_over_conditional(self):
        return self.winner is None
