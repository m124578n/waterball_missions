from .PlayerTemplate import PlayerTemplate


class AIPlayerTemplate(PlayerTemplate):
    def take_turn(self):
        return self._set_take_turn_rule()

    def name_himself(self):
        self.name = "Bot"

    def add_hand(self, card):
        self.hand.append(card)
        self.hand_size += 1

    def show(self, want_to_show_card=0):
        self.hand_size -= 1
        return self.hand.pop(int(want_to_show_card))

    def pass_turn(self):
        pass

    def _set_take_turn_rule(self):
        pass
