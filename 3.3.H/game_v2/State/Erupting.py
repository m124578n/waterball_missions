from .State import State


class Erupting(State):
    def _set_next_state(self):
        from .Teleport import Teleport
        self.next_state = Teleport

    def _set_name(self):
        self.name = "爆發"

    def _set_time_limit(self):
        self.time_limit = 3

    def state_trigger(self):
        self.role.attack_targets = self.role.map.find_all_different_role(self.role)
