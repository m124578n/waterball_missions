from .Content import Content
from game_v2.State import Invincible


class SuperStar(Content):
    def _set_name(self):
        self.name = "無敵星星"

    def _set_state(self):
        self.state = Invincible
