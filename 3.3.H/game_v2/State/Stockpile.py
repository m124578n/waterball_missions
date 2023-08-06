from .State import State


class Stockpile(State):
    def _set_next_state(self):
        from .Erupting import Erupting
        self.next_state = Erupting

    def _set_name(self):
        self.name = "蓄力"

    def _set_time_limit(self):
        self.time_limit = 2

    def state_trigger(self):
        from .Normal import Normal
        if self.now_hp < self.role.hp:
            self.role.be_attacked_entry_state = Normal

