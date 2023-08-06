from .Content import Content
from game_v2.State import Accelerated


class AcceleratingPotion(Content):
    def _set_name(self):
        self.name = "加速藥水"

    def _set_state(self):
        self.state = Accelerated
