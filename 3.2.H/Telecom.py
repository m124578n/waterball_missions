

class Telecom:
    def __init__(self):
        self.status = None

    def connect(self):
        self.status = "連接"
        print(f"通訊設備已 {self.status}")

    def disconnect(self):
        self.status = "中斷連接"
        print(f"通訊設備已 {self.status}")
