from .Deck import Deck
from .Player import Player


class ShowDown:
    def __init__(self, players: list):
        self.players = players
        self.deck = Deck()
        self.round = 0
        self.round_winner = None

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
        return self.deck.size == 0

    def players_draw_card(self):
        for player in self.players:
            player.hand.add_card(self.deck.draw_card())

    def game_end_conditional(self):
        return self.round == 13

    def game_start_until_end(self):
        self.round_winner = None
        self.round += 1
        round_cards = []
        for player in self.players:
            round_cards.append(player.take_turn())
        self.show_round_cards(round_cards)
        self.round_show_down(round_cards)
        self.round_winner.point += 1

    def show_round_cards(self, cards):
        for index, card in enumerate(cards):
            print(f"玩家{index} {self.players[index].name}出的牌是：{card.suit.name} {card.rank.name}")

    def round_show_down(self, cards: list):
        round_winner_index = None
        round_winner_card = None
        for index, card in enumerate(cards):
            if round_winner_index is None:
                round_winner_index = index
                round_winner_card = card
            else:
                if round_winner_card.rank.value < card.rank.value:
                    round_winner_index = index
                    round_winner_card = card
                else:
                    if round_winner_card.suit.value < card.suit.value:
                        round_winner_index = index
                        round_winner_card = card
        print(f"本回合獲勝的是玩家{round_winner_index} {self.players[round_winner_index].name}")
        self.round_winner = self.players[round_winner_index]

    def show_winner(self):
        winner = None
        winner_index = None
        for index, player in enumerate(self.players):
            if winner is None:
                winner = player
                winner_index = index
            else:
                if winner.point < player.point:
                    winner = player
                    winner_index = index
        print(f"最終獲勝者為：玩家{winner_index} {winner.name}，分數為：{winner.point}")


