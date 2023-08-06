from .State import State


class Normal(State):
    def _set_name(self):
        self.name = "正常"

    def _set_time_limit(self):
        self.time_limit = 999999

    def state_trigger(self):
        from .Invincible import Invincible
        self.role.set_invincible(False)
        self.role.attack_targets = None
        self.role.be_attacked_entry_state = Invincible
        self.role.turn = 1
        self.role.set_move_step("wasd")
        self.role.set_can_choose("(a)move (b)attack")
