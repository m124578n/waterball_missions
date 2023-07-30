

class MagicInit:
    def __init__(self, name: str, age: int, default: str = "I am default"):
        self.name = name
        self.age = age
        self.default = default


p1 = MagicInit("John", 25)
p2 = MagicInit("John", 25, "change the default")
print(p1.name, p1.age, p1.default)
print(p2.name, p2.age, p2.default)
