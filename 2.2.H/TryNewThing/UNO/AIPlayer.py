from .Player import Player


class AIPlayer(Player):
    def __init__(self):
        super().__init__()
        self.count = 0

    def name_himself(self):
        self.name = "AI_Bot"

    def take_turn(self):
        self.count += 1
        if self.hand.size <= self.count:
            self.count = 0
            return "pass"
        else:
            return 0
