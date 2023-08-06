from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game_v2.MapObject.Role import Role


class State(ABC):
    def __init__(self, role: 'Role'):
        self.role = role
        self.time_limit = 0
        self.name = ""
        self.next_state = None
        self.now_hp = role.hp
        self._set_name()
        self._set_time_limit()
        self._set_next_state()

    def _set_next_state(self):
        from .Normal import Normal
        self.next_state = Normal

    @abstractmethod
    def _set_name(self):
        pass

    @abstractmethod
    def _set_time_limit(self):
        pass

    def trigger(self):
        self.time_limit -= 1
        if self.time_limit < 0:
            self.role.exit_state()
        else:
            self.state_trigger()

    @abstractmethod
    def state_trigger(self):
        pass

    def __repr__(self):
        return self.name
