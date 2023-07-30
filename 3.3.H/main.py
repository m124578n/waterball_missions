# from game_v1.Game import Game
# from game_v1.Handler import (
#     CharacterTreasureHandler,
#     CharacterObstacleHandler,
#     CharacterMonsterHandler,
#     CharacterNoneHandler
# )

# if __name__ == "__main__":
#     game = Game(CharacterNoneHandler(CharacterTreasureHandler(CharacterObstacleHandler(CharacterMonsterHandler(None)))))
#     game.start()

from game_v2 import Game
from game_v2.MapObject import (
        Character,
        Obstacle,
        Monster,
        Treasure
    )

from game_v2.Handler import (
        RoleTreasureHandler,
        RoleDifferentHandler,
        RoleObstacleHandler,
        RoleSameHandler,
        RoleSpaceHandler
    )

if __name__ == "__main__":
    map_obejcts = [
            [Obstacle, 10],
            [Treasure, 10],
            [Character, 1],
            [Monster, 10]
        ]
    handlers = [
        RoleSpaceHandler(), 
        RoleTreasureHandler(), 
        RoleObstacleHandler(), 
        RoleDifferentHandler(), 
        RoleSameHandler()
        ]
    game = Game(map_obejcts, handlers)
    game.start()
