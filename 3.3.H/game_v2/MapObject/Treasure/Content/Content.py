from abc import ABC, abstractmethod


class Content(ABC):
    def __init__(self):
        self.state = None
        self.name = ""
        self._set_state()
        self._set_name()

    @abstractmethod
    def _set_state(self):
        pass

    @abstractmethod
    def _set_name(self):
        pass

    def __repr__(self):
        return self.name
