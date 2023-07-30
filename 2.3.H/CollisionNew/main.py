from World import World
from Water import Water
from Fire import Fire
from Hero import Hero
from WaterFireHandler import WaterFireHandler
from HeroFireHandler import HeroFireHandler
from HeroWaterHandler import HeroWaterHandler
from IsSameHandler import IsSameHandler


if __name__ == "__main__":
    sprites = [Water(), Fire(), Hero()]
    world = World(sprites, WaterFireHandler(HeroWaterHandler(HeroFireHandler(IsSameHandler(None)))))
    world.create_world()
    for index, x in enumerate(world.world):
        if x.sprite is not None:
            print(index, x.sprite.name)
        else:
            print(index, None)
    while True:
        input_coord = input("請選擇兩個座標：")
        x1, x2 = input_coord.split(" ")
        world.move(int(x1), int(x2))
        for index, x in enumerate(world.world):
            if x.sprite is not None:
                print(index, x.sprite.name)
            else:
                print(index, None)

