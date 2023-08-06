from .Content import Content
from game_v2.State import Stockpile


class KingsRock(Content):
    def _set_name(self):
        self.name = "王者之印"

    def _set_state(self):
        self.state = Stockpile
