from .DeckTemplate import DeckTemplate
from abc import ABC, abstractmethod


class CardGameTemplate(ABC):
    def __init__(self, players: list, deck):
        self.players = players
        self.deck = deck
        self.round = 0
        self.winner = None
        self.init_card = 0
        self.table = []

    def start(self):
        # 流程Ａ
        self.player_name_himself()
        self.deck.shuffle()
        # 流程Ｂ
        while self.draw_card_conditional():
            self.player_draw_card()
        # 流程Ｃ
        while self.game_over_conditional():
            self.game_take_round()
        self.show_winner()

    def player_name_himself(self):
        for player in self.players:
            player.name_himself()

    def player_draw_card(self):
        for player in self.players:
            player.add_hand(self.deck.draw_card())
        self.init_card += 1

    @abstractmethod
    def game_take_round(self):
        pass

    @abstractmethod
    def show_winner(self):
        pass

    @abstractmethod
    def game_over_conditional(self):
        return True

    @abstractmethod
    def draw_card_conditional(self):
        return True
