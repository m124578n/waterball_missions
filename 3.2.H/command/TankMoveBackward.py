

class TankMoveBackward:
    def __init__(self, tank: "Tank"):
        self.tank = tank

    def execute(self):
        self.tank.move_backward()

    def undo(self):
        self.tank.move_forward()

    def __repr__(self):
        return f"Tank Move Backward"
