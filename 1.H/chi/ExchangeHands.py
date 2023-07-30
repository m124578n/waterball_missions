class Exchange:
    def __init__(self):
        self.target_player = None
        self.start_player = None
        self.countdown = 3

    def reduce_countdown(self):
        self.countdown -= 1

    def get_start_player(self, player):
        self.start_player = player

    def get_target_player(self, target_player):
        self.target_player = target_player
