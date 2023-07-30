

class TelecomDisconnect:
    def __init__(self, telecom: "Telecom"):
        self.telecom = telecom

    def execute(self):
        self.telecom.disconnect()

    def undo(self):
        self.telecom.connect()

    def __repr__(self):
        return f"Telecom Disconnect"
