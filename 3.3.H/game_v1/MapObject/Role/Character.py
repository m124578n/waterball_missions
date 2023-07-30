from .Role import Role


class Character(Role):
    def __init__(self):
        super().__init__()
        self.set_symbol()
        self.set_hp()

    def set_symbol(self):
        # ↑→↓←
        self.symbol = "↑"

    def set_hp(self):
        self.hp = 300

    def move(self, goal: str):
        if goal == 'w':
            self.symbol = "↑"
        elif goal == 'a':
            self.symbol = "←"
        elif goal == 's':
            self.symbol = "↓"
        elif goal == 'd':
            self.symbol = "→"
