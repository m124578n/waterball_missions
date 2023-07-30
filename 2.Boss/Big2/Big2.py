from .Round import Round
from .Player import Player
from .CardPatternHandler.CardPatternHandler import CardPatternHandler
from .Deck import Deck


class Big2:
    def __init__(self, players: list[Player], card_pattern_handle: CardPatternHandler):
        self.deck = None
        self.players: list[Player] = players
        self.next_turn_player: Player or None = None
        self.card_pattern_handler: CardPatternHandler = card_pattern_handle
        self.round = Round()
        self.winner_player = None

    def start(self):
        self.players_name_themself()
        self.deck_create()
        self.deck_deal()
        self.sorted_them_hand_cards()
        self.game_start()
        self.end()

    def players_name_themself(self):
        for player in self.players:
            player.name_himself()

    def deck_create(self):
        deck_decide = input("請選擇要自訂牌堆還是預設牌堆 e.g.no為預設牌堆：")
        if deck_decide.lower() == 'no':
            self.deck = Deck(None)
            self.deck.shuffle()
        else:
            self.deck = Deck(deck_decide)

    def deck_deal(self):
        while self.deck.size != 0:
            for player in self.players:
                player.hand_cards.add_card(self.deck.deal())

    def sorted_them_hand_cards(self):
        print("整理手牌～")
        for player in self.players:
            player.hand_cards.sort_spec_rule()

    def game_start(self):
        while self.round.without_winner:
            self.winner_player = self.round.start(self.players, self.card_pattern_handler)

    def end(self):
        self.show_winner()

    def show_winner(self):
        print(f"遊戲結束，遊戲的勝利者為 {self.winner_player.name}")
