from Sprite import Sprite
from Hero import Hero
from Water import Water
from Fire import Fire
import random
from Coord import Coord


class World:
    def __init__(self, *sprites):
        self.length = 30
        self.world = None
        self.sprites = [sprite for sprite in sprites]

    def create_world(self):
        self.world = [Coord(x) for x in range(30)]
        random_coord = random.sample(range(30), 10)
        for x in random_coord:
            self.world[x].set_sprite(random.choice(self.sprites))

    def collision(self, x1, x2):
        sprite1 = type(self.world[x1].sprite)
        sprite2 = type(self.world[x2].sprite)
        print(sprite1, sprite2)
        if sprite1 == Water and sprite2 == Fire:
            self.world[x1].sprite = None
            self.world[x2].sprite = None
            print("水碰火，兩者皆消滅")
        elif sprite1 == Fire and sprite2 == Water:
            self.world[x1].sprite = None
            self.world[x2].sprite = None
            print("水碰火，兩者皆消滅")
        elif sprite1 == Water and sprite2 == Water:
            print("水碰水，移動無效")
        elif sprite1 == Fire and sprite2 == Fire:
            print("火碰火，移動無效")
        elif sprite1 == Hero and sprite2 == Fire:
            self.world[x1].sprite.hp -= 10
            self.world[x2].sprite = None
            if self.world[x1].sprite.hp == 0:
                self.world[x1].sprite.hp = None
                print("英雄碰火，英雄-10HP，英雄生命值歸零，ＧＧ")
            else:
                print("英雄碰火，英雄-10HP，並移動且消滅火")
            self.world[x1].sprite, self.world[x2].sprite = self.world[x2].sprite, self.world[x1].sprite
        elif sprite1 == Fire and sprite2 == Hero:
            self.world[x2].sprite.hp -= 10
            self.world[x1].sprite = None
            if self.world[x1].sprite.hp == 0:
                self.world[x1].sprite.hp = None
                print("火碰英雄，英雄-10HP，英雄生命值歸零，ＧＧ")
            else:
                print("火碰英雄，英雄-10HP，並移動且消滅火")
        elif sprite1 == Hero and sprite2 == Water:
            self.world[x1].sprite.hp += 10
            self.world[x2].sprite = None
            self.world[x1].sprite, self.world[x2].sprite = self.world[x2].sprite, self.world[x1].sprite
            print("英雄碰水，英雄+10HP，並移動且消滅水")
        elif sprite1 == Water and sprite2 == Hero:
            self.world[x2].sprite.hp += 10
            self.world[x1].sprite = None
            self.world[x1].sprite, self.world[x2].sprite = self.world[x2].sprite, self.world[x1].sprite
            print("英雄碰水，英雄+10HP，並移動且消滅水")
        elif sprite1 == Hero and sprite2 == Hero:
            print("英雄碰英雄，移動無效")
        elif sprite1 is not type(None):
            self.world[x1].sprite, self.world[x2].sprite = self.world[x2].sprite, self.world[x1].sprite
            print("移動成功")
        else:
            print("您所選區域死氣沈沈")



