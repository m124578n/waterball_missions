from MatchmakingStrategy import *


class DistanceBased(MatchmakingStrategy):
    def __init__(self, reverse=False):
        self.reverse = reverse

    # def find_match(self, individual, individuals):
    #     x, y = individual.coord
    #     individual_dict = {}
    #     for individual in individuals:
    #         x1, y1 = individual.coord
    #         distance = ((y1 - y) ** 2 + (x1 - x) ** 2) ** 0.5
    #         individual_dict[individual.id] = distance
    #     if self.reverse:
    #         return sorted(individual_dict.items(), key=lambda item: item[1])[::-1]
    #     else:
    #         return sorted(individual_dict.items(), key=lambda item: item[1])

    def find_match(self, individual, individuals):
        x, y = individual.coord
        individual_dict = {individual.id: ((individual.coord[1] - y) ** 2 + (individual.coord[0] - x) ** 2) ** 0.5 for individual in individuals}
        if self.reverse:
            return sorted(individual_dict.items(), key=lambda item: item[1])[::-1]
        else:
            return sorted(individual_dict.items(), key=lambda item: item[1])
