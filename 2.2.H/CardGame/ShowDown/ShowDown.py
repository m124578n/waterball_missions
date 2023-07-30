from .Deck import Deck
from .Card import Card
from ..CardGameTemplate import CardGameTemplate


class ShowDown(CardGameTemplate):
    def __init__(self, players: list):
        super().__init__(players, Deck())

    def game_take_round(self):
        for player in self.players:
            player_decide = player.take_turn()
            self.table.append(player.show(player_decide))
        index = Card.show_down(self.table)
        print(index)
        winner_card = self.table[index]
        round_winner = self.players[index]
        round_winner.point += 1
        print("本回合卡片最大為：%s %s，勝利者為：玩家 %s %s" % (winner_card.suits.name, winner_card.rank.name, index, round_winner.name))
        self.round += 1
        self.table = []

    def show_winner(self):
        winner = None
        index = None
        for index, player in enumerate(self.players):
            if winner is None:
                winner = player
                index = index
            elif winner.point < player.point:
                winner = player
                index = index
        print("遊戲結束！！")
        print("贏家為：玩家 %s %s，分數有：%s 分" % (index, winner.name, winner.point))

    def game_over_conditional(self):
        return self.round != 13

    def draw_card_conditional(self):
        return self.init_card != 13
