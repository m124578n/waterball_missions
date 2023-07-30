from .Player import Player
import random


class AIPlayer(Player):
    def __init__(self):
        super().__init__()

    def name_himself(self):
        self.name = "AI_bot"

    def take_turn(self):
        hand_index = random.sample(range(self.hand.size), 1)[0]
        return self.hand.show(hand_index)
