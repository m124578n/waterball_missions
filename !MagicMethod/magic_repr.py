

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name}, age:{self.age}"

    def __repr__(self):
        return f"姓名：{self.name}，年齡：{self.age}"


p = Person("John", 25)
p
print(p)
print(str(p))
print(repr(p))

# output:
# 姓名：John，年齡：25
# Name:John, age:25
# Name:John, age:25
# 姓名：John，年齡：25


