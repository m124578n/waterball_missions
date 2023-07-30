

class TelecomConnect:
    def __init__(self, telecom: "Telecom"):
        self.telecom = telecom

    def execute(self):
        self.telecom.connect()

    def undo(self):
        self.telecom.disconnect()

    def __repr__(self):
        return f"Telecom Connect"
