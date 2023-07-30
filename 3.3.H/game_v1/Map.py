from .MapObject.MapObject import MapObject


class Map:
    def __init__(self, x, y):
        self.map = []
        for x1 in range(x):
            temp1 = []
            for y1 in range(y):
                map_object = MapObject()
                map_object.set_coord(x1, y1)
                temp1.append(map_object)
            self.map.append(temp1)

    def __str__(self):
        for x in self.map:
            print(f"{x}")
            # for y in x:
            #     print(type(y.object))
        return "this is a map"
