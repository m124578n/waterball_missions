from .State import State


class Accelerated(State):
    def _set_name(self):
        self.name = "加速"

    def _set_time_limit(self):
        self.time_limit = 3

    def state_trigger(self):
        from .Normal import Normal
        self.role.turn = 2
        if self.now_hp < self.role.hp:
            self.role.be_attacked_entry_state = Normal
