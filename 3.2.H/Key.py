

class Key:
    def __init__(self, name):
        self.name = name
        self.key = None

    def execute(self):
        self.key.execute()

    def undo(self):
        self.key.undo()

    def __repr__(self):
        return f"{self.key}"
