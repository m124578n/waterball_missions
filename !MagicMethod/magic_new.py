class MagicNew:
    def __new__(cls, *args, **kwargs):
        print("here is new")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print("here is init")
        self.name = name


c = MagicNew("John")


# output:
# here is new
# here is init


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
# output:
# <__main__.Singleton object at 0x104808d90>
# <__main__.Singleton object at 0x104808d90>
