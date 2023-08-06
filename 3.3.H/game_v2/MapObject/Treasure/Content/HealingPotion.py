from .Content import Content
from game_v2.State import Healing


class HealingPotion(Content):
    def _set_name(self):
        self.name = "補血罐"

    def _set_state(self):
        self.state = Healing
