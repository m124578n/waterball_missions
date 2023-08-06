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

from game_v2.MapObject.Treasure.Content import (
    AcceleratingPotion,
    DevilFruit,
    DokodemoDoor,
    Poison,
    KingsRock,
    SuperStar,
    HealingPotion
)

map_objects = [
            [Obstacle, 10],
            [Treasure, 20],
            [Character, 1],
            [Monster, 5]
        ]

handlers = [
    RoleSpaceHandler(),
    RoleSameHandler(),
    RoleObstacleHandler(),
    RoleTreasureHandler(),
    RoleDifferentHandler()
    ]

contents = [
    [SuperStar(), 0.1],
    [Poison(), 0.25],
    [AcceleratingPotion(), 0.2],
    [HealingPotion(), 0.15],
    [DevilFruit(), 0.1],
    [KingsRock(), 0.1],
    [DokodemoDoor(), 0.1],
]
