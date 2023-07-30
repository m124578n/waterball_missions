

class ResetMainController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.keys = None

    def execute(self):
        self.keys = self.main_controller.keys
        self.main_controller.reset()

    def undo(self):
        self.main_controller.keys = self.keys

    def __repr__(self):
        return f"Reset All Key"
