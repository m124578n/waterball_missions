from MatchmakingStrategy import *


class HabitBased(MatchmakingStrategy):
    def __init__(self, reverse=False):
        self.reverse = reverse

    # def find_match(self, individual, individuals):
    #     individual1_habits_set = individual.get_habits_set()
    #     individual_dict = {}
    #     for individual in individuals:
    #         individual2_habits_set = individual.get_habits_set()
    #         intersection_set = individual1_habits_set.intersection(individual2_habits_set)
    #         individual_dict[individual.id] = len(intersection_set)
    #     if self.reverse:
    #         return sorted(individual_dict.items(), key=lambda item: item[1])
    #     else:
    #         return sorted(individual_dict.items(), key=lambda item: item[1])[::-1]

    def find_match(self, individual, individuals):
        individual1_habits_set = individual.get_habits_set()
        individual_dict = {individual.id: len(individual1_habits_set.intersection(individual.get_habits_set())) for individual in individuals}
        if self.reverse:
            return sorted(individual_dict.items(), key=lambda item: item[1])
        else:
            return sorted(individual_dict.items(), key=lambda item: item[1])[::-1]
