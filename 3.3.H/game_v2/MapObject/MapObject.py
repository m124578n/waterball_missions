from abc import ABC, abstractmethod



class MapObject(ABC):
    def __init__(self, x ,y) -> None:
        self.symbol = None
        self.x = x
        self.y = y
        self._set_symbol()
    
    @abstractmethod
    def _set_symbol(self):
        pass

    def __repr__(self) -> str:
        return self.symbol
    