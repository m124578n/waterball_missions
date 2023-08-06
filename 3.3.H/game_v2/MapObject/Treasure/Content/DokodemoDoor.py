from .Content import Content
from game_v2.State import Teleport


class DokodemoDoor(Content):
    def _set_name(self):
        self.name = "任意門"

    def _set_state(self):
        self.state = Teleport
