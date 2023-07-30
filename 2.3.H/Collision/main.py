from World import World
from Water import Water
from Fire import Fire
from Hero import Hero


if __name__ == "__main__":
    world = World(Water(), Fire(), Hero())
    world.create_world()
    for index, x in enumerate(world.world):
        print(index, x.sprite)
    while True:
        input_coord = input("請選擇兩個座標：")
        x1, x2 = input_coord.split(" ")
        world.collision(int(x1), int(x2))

