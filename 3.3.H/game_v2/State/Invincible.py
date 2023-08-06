from .State import State


class Invincible(State):
    def _set_name(self):
        self.name = "無敵"

    def _set_time_limit(self):
        self.time_limit = 2

    def state_trigger(self):
        self.role.set_invincible(True)
