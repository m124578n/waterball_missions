from Individual import Individual
from MatchmakingSystem import *
from DistanceBased import *
from HabitBased import *

if __name__ == '__main__':
    individual = Individual(1, 'MALE', 24, '安安', '玩電腦, 看動畫, 看電影, 聽音樂', (5, 10))

    individual_list = [Individual(2, 'FEMALE', 21, '安安 你好', '看動畫, 看電影, 逛街, 收集化妝品', (11, 9)),
                       Individual(3, 'FEMALE', 29, '我是魚', '逛街, 收集化妝品, 看小說, 運動', (4, 6)),
                       Individual(4, 'FEMALE', 18, '我是蠍', '玩電腦, 看動畫, 看電影, 聽音樂', (10, 5)),
                       Individual(5, 'FEMALE', 23, '我是射', '看動畫, 看電影, 聽音樂', (5, 11))]
    
    matchmaking_system = MatchmakingSystem(DistanceBased(reverse=True))
    best_list = matchmaking_system.match(individual, individual_list)
    print(best_list)

