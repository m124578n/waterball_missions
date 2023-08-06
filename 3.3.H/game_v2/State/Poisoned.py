from .State import State


class Poisoned(State):
    def __init__(self, role):
        super().__init__(role)
        self.damage = 0
        self._set_damage()

    def _set_name(self):
        self.name = "中毒"

    def _set_time_limit(self):
        self.time_limit = 3

    def _set_damage(self):
        self.damage = 15

    def state_trigger(self):
        print(f"角色 {self.role.symbol} 受到中毒傷害 {self.damage}")
        self.role.get_damage(self.damage)
        self.time_limit -= 1
