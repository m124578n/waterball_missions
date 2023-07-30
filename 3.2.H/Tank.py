

class Tank:
    def __init__(self):
        self.step = 0

    def move_forward(self):
        self.step += 1
        print("Tank 向前移動一步")

    def move_backward(self):
        self.step -= 1
        print("Tank 向後移動一步")
