

class Marco:
    def __init__(self):
        self.command = []

    def execute(self):
        for c in self.command:
            c.execute()

    def undo(self):
        for c in self.command:
            c.undo()

    def __repr__(self):
        string = ""
        for c in self.command:
            string += str(c)+" & "
        return string
