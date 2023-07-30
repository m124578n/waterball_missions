from ..AIPlayerTemplate import AIPlayerTemplate


class AIPlayer(AIPlayerTemplate):
    def __init__(self):
        super().__init__()
        self.showed_card_count = 0

    def _set_take_turn_rule(self):
        self.showed_card_count += 1
        if self.showed_card_count == self.hand_size:
            self.showed_card_count = 0
            return 'pass'
        else:
            return 0

