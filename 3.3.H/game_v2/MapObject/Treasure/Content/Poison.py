from .Content import Content
from game_v2.State import Poisoned


class Poison(Content):
    def _set_name(self):
        self.name = "毒藥"

    def _set_state(self):
        self.state = Poisoned
