
class TankMoveForward:
    def __init__(self, tank: "Tank"):
        self.tank = tank

    def execute(self):
        self.tank.move_forward()

    def undo(self):
        self.tank.move_backward()

    def __repr__(self):
        return f"Tank Move Forward"
