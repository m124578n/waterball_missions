from Coord import Coord


def change(world: list[Coord], x1: Coord, x2: Coord) -> list[Coord]:
    index1 = world.index(x1)
    index2 = world.index(x2)
    world[index1], world[index2] = world[index2], world[index1]
    return world


def set_world(world: list[Coord], x1: Coord, x2: Coord) -> list[Coord]:
    index1 = world.index(x1)
    index2 = world.index(x2)
    world[index1], world[index2] = x1, x2
    return world
