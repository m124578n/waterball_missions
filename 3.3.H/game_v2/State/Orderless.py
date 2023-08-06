import random

from .State import State


class Orderless(State):
    def _set_name(self):
        self.name = "混亂"

    def _set_time_limit(self):
        self.time_limit = 3

    def state_trigger(self):
        self.role.set_move_step(random.choice(["ws", "ad"]))
        self.role.set_can_choose("(a)move")
