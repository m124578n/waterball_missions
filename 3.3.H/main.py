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

from game_v2.config import handlers


if __name__ == "__main__":
    map_objects = [
            [Obstacle, 10],
            [Treasure, 20],
            [Character, 1],
            [Monster, 5]
        ]
    handlers = handlers
    print(map_objects)
    game = Game(map_objects, handlers)
    game.start()
