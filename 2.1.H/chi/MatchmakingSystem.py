class MatchmakingSystem:
    def __init__(self, strategy):
        self.strategy = strategy

    def match(self, individual, individuals):
        return self.strategy.find_match(individual, individuals)
