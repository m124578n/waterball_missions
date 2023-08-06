from .Content import Content
from game_v2.State import Orderless


class DevilFruit(Content):
    def _set_name(self):
        self.name = "惡魔果實"

    def _set_state(self):
        self.state = Orderless
