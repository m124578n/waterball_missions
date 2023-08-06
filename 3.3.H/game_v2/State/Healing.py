from .State import State


class Healing(State):
    def __init__(self, role):
        super().__init__(role)
        self.healing = 0
        self._set_healing()

    def _set_healing(self):
        self.healing = 30

    def _set_name(self):
        self.name = "恢復"

    def _set_time_limit(self):
        self.time_limit = 5

    def state_trigger(self):
        if self.role.hp == self.role.max_hp:
            print(f"角色 {self.role.symbol} 因為寫滿了脫離 {self.name} 狀態")
            self.role.entry_state(self.next_state)
        else:
            self.role.get_healing(self.healing)
