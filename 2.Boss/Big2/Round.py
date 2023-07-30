from __future__ import annotations
from .Player import Player
from .Card import Card
from .CardPatternHandler.CardPatternHandler import CardPatternHandler


class Round:
    def __init__(self):
        self.players = None
        self.top_player = None
        self.top_play = None
        self.count = 0
        self.now_player: Player | None = None
        self.pass_count = 0
        self.check_can_pass = False
        self.handler: CardPatternHandler | None = None
        self.without_winner = True
        self.winner_player = None

    def start(self, players, handler):
        self.handler = handler
        self.players = players
        print("新的回合開始了。")
        self.count += 1
        self.pass_count = 0
        if self.count == 1:
            self.find_c3(players)
        self.now_player_play()
        if not self.without_winner:
            return self.winner_player
        self.end()

    def find_c3(self, players: list[Player]):
        for player in players:
            for card in player.hand_cards.cards:
                if str(card) == 'C[3]':
                    self.now_player = player

    # TODO 待優化流程
    def now_player_play(self):
        while self.pass_count < 3:
            if not self.without_winner:
                break
            print(f"輪到 {self.now_player.name} 了")
            player_decide: list[Card] | str = self.now_player.take_turn()
            if player_decide == 'pass':
                if self.top_play is None:
                    print(f"你不能在新的回合喊 PASS")
                else:
                    self.pass_count += 1
                    self.now_player.turn = 0
                    print(f"玩家 {self.now_player.name} PASS")
                    self.now_player = self.get_next_player()
            elif player_decide == 'error01':
                print(f"你的輸入格式有誤。")
            else:
                self.check_can_play(player_decide)
        self.now_player = self.top_player
        if not self.without_winner:
            self.winner_player = self.now_player

    # TODO 待優化流程 驗證過再移除手牌 出牌條件為符合牌型和比較大
    def check_can_play(self, player_decide: list[Card]):
        result = self.handler.check(player_decide)
        if not result:
            self.rollback_cards(player_decide)
            print("此牌型不合法，請再嘗試一次。")
        else:
            if self.count == 1:
                check_c3 = False
            else:
                check_c3 = True
            if self.count == 1 and self.top_play is None:
                for card in player_decide:
                    if str(card) == 'C[3]':
                        check_c3 = True
                        break
                if not check_c3:
                    self.rollback_cards(player_decide)
                    print("此牌型不合法，請再嘗試一次。必須包含梅花三 C[3]")
            if self.top_play is None:
                if check_c3:
                    self.play(result)
            else:
                if type(result) == type(self.top_play):
                    if result > self.top_play:
                        self.play(result)
                    else:
                        self.rollback_cards(player_decide)
                        print("此牌型不合法，請再嘗試一次。")
                else:
                    self.rollback_cards(player_decide)
                    print("此牌型不合法，請再嘗試一次。")

    def play(self, result):
        print(f"玩家 {self.now_player.name} 打出了 {result.name} {result}")
        self.top_play = result
        self.top_player = self.now_player
        self.now_player.turn = 0
        self.pass_count = 0
        if self.now_player.hand_cards.size == 0:
            self.without_winner = False
        else:
            self.now_player = self.get_next_player()

    def next_player_play(self):
        self.now_player.turn = 0
        self.now_player = self.get_next_player()

    def rollback_cards(self, player_decide):
        for card in player_decide:
            self.now_player.hand_cards.add_card(card)
        self.now_player.hand_cards.sort_spec_rule()

    def get_next_player(self):
        index = self.now_player.index
        next_index = (index + 1) % 4
        for player in self.players:
            if player.index == next_index:
                return player

    def end(self):
        self.top_player = None
        self.top_play = None
        self.pass_count = 0
        self.check_can_pass = False
